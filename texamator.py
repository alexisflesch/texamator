#!/usr/bin/python
# -*- coding: utf-8 -*-


from PyQt4 import QtCore, QtGui
import sys, os
from random import shuffle
from partielatormods import *

from PyQt4.QtGui import *
from PyQt4.QtCore import Qt


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class MonApplication(Ui_MainWindow):

    def __init__(self, settings):
        self.first_time, self.tags, self.header, self.footer, self.settings, self.compile_seq, self.generate = settings
        self.treeTeX = False
        self.enonce = "None" #last exercise
        self.whatson = "tree" #what is being previewed ? tree or list ?
        #Default font for editing TeX code
        self.myfont = QtGui.QFont()
        self.myfont.setFamily("Monospace")
        self.myfont.setFixedPitch(True)
        self.myfont.setPointSize(10)

    def create_main_tree(self):
        """Ask crazyparser to create a tree, then fills up the QtreeWidget with it"""
        topdir = str(self.lineEdit.text())
        if topdir[-1] == "/":
            topdir = topdir[0:-1]
        nb_ex, self.treeTeX = crazyparser(topdir,self.tags)
        self.fillTheTree(self.treeTeX,nb_ex)
        self.actionExpand_Collapse.setEnabled(True)
        #if the search line is not empty, update the tree
        string = unicode(self.lineEdit_search.text())
        if string:
            self.search()


    def search(self):
        """Search for a string in folder/file names and in the exercices using treeTeX"""
        string = unicode(self.lineEdit_search.text())
        string = string.encode("utf-8").lower()
        string2 = power_rangers(string) #to allow a search with accents of the form \'e instead of é (see crazyparser.py)
        s1 = smart_cut(string)   #to allow searching for more than one keyword
        s2 = smart_cut(string2)

        if self.treeTeX:
            self.treeTeX.reverse()
            self.treeTeX2 = []
            nb_ex = 0
            for root,dirs,files in self.treeTeX:
                dossiers_a_ajouter = []
                fichiers_a_ajouter = []


                #Keep only interesting exercises
                for feuille_dexo in files:
                    liste_dexo = []
                    for exo in feuille_dexo[1]:
                        allin = True
                        for i in range(len(s1)):
                            if s1[i][0] != "-":
                                if not ((s1[i] in exo.lower()) or (s2[i] in exo.lower()) \
                                  or (s1[i] in root.lower()) or (s1[i] in feuille_dexo[0])):
                                    allin = False
                            if s1[i][0] == "-" and len(s1[i])>1:
                                if ((s1[i][1:] in exo.lower()) or (s2[i][1:] in exo.lower()) \
                                  or (s1[i][1:] in root.lower()) or (s1[i][1:] in feuille_dexo[0])):
                                    allin = False
                        if allin:
                            liste_dexo.append(exo)
                    if liste_dexo:
                        nb_ex += len(liste_dexo)
                        fichiers_a_ajouter.append((feuille_dexo[0],liste_dexo))

                #Look for folders containing "interesting" sub-folders
                for dossier in dirs:
                    for a in self.treeTeX2:
                        if os.path.join(root,dossier) == a[0]:
                            dossiers_a_ajouter.append(dossier)

                #If exercises or intersting sub-folders where found , give them
                if dossiers_a_ajouter or fichiers_a_ajouter:
                    self.treeTeX2.append((root,dossiers_a_ajouter,fichiers_a_ajouter))
            self.treeTeX.reverse()
            self.treeTeX2.reverse()
            self.fillTheTree(self.treeTeX2,nb_ex)


    def fillTheTree(self, someTree, nb_ex):
        """Fills the QtreeWidget with someTree"""
        self.treeWidget.clear()
        if nb_ex == 0:
            self.treeWidget.setHeaderLabel(QtGui.QApplication.translate("Dialog", "No exercise found", None, QtGui.QApplication.UnicodeUTF8))
        elif nb_ex == 1:
            self.treeWidget.setHeaderLabel(QtGui.QApplication.translate("Dialog", "1 exercise found", None, QtGui.QApplication.UnicodeUTF8))
        else:
            self.treeWidget.setHeaderLabel(str(nb_ex) + " " + \
                QtGui.QApplication.translate("Dialog","exercises found", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.header().show()
        if someTree:
            itemDict = {}
            topdir = someTree[0][0]
            topname = topdir.split('/')[-1]
            racine = os.path.split(topdir)[0]
            itemDict[racine] = self.treeWidget
            folderIcon = QtGui.QIcon()
            folderIcon.addPixmap(QtGui.QPixmap(_fromUtf8(":/all/icones/folder.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            fileIcon = QtGui.QIcon()
            fileIcon.addPixmap(QtGui.QPixmap(_fromUtf8(":/all/icones/tex.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)

            for fullpath, b, c in someTree:
                nom = fullpath.split("/")[-1]
                parent = os.path.split(fullpath)[0]
                itemDict[fullpath] = QtGui.QTreeWidgetItem(itemDict[parent])
                itemDict[fullpath].setText(0,QtGui.QApplication.translate("Form", nom, None,\
                    QtGui.QApplication.UnicodeUTF8))
                itemDict[fullpath].setIcon(0, folderIcon)

                for i in c:#TeX file
                    nb = len(i[1]) #number of exercices in the file
                    nom_tex = i[0][:-4]
                    nom2 = nom_tex + " (" + str(nb) + ")"
                    nom_element = os.path.join(fullpath,i[0])
                    itemDict[nom_element] = QtGui.QTreeWidgetItem(itemDict[fullpath])
                    itemDict[nom_element].setText(0,QtGui.QApplication.translate("Form", nom2, None,\
                    QtGui.QApplication.UnicodeUTF8))
                    itemDict[nom_element].setIcon(0, fileIcon)

                    compteur_exos = 0
                    for j in i[1]:#Exercises
                        compteur_exos += 1
                        #What comes next is to ensure exercices will be displayed alphabetically :
                        # "Ex 2" > "Ex 20" which is annoying that's why "Ex 2" becomes
                        # "Ex 02" when needed
                        if nb > 99:
                            if compteur_exos < 10:
                                nom_exo = " Ex 00" + str(compteur_exos)
                            elif 10 < compteur_exos < 100:
                                nom_exo = " Ex 0" + str(compteur_exos)
                            else:
                                nom_exo = " Ex " + str(compteur_exos)
                        elif nb > 9:
                            if compteur_exos < 10:
                                nom_exo = " Ex 0" + str(compteur_exos)
                            else:
                                nom_exo = " Ex " + str(compteur_exos)
                        else:
                            nom_exo = " Ex " + str(compteur_exos)

                        nom_cp_exo = nom_element + nom_exo
                        itemDict[nom_cp_exo] = QtGui.QTreeWidgetItem(itemDict[nom_element])
                        itemDict[nom_cp_exo].setText(0,QtGui.QApplication.translate("Form",\
                                             nom_exo, None, QtGui.QApplication.UnicodeUTF8))
                        itemDict[nom_cp_exo].enonce = j
                        itemDict[nom_cp_exo].titre = nom_tex + " - ex "+str(compteur_exos)
                        itemDict[nom_cp_exo].filename = os.path.join(fullpath,i[0])
        self.treeWidget.sortItems(0,QtCore.Qt.AscendingOrder)


    def show_preview(self,enonce,inside=1):
        if enonce == self.enonce and inside:  #only run LaTeX if necessary
            return False
        self.enonce = enonce
        try:
            os.mkdir("/tmp/partielator")
            os.chdir("/tmp/partielator")
        except:
            print("couldn't create partielator dir or partielator dir already exists")
        a = codecs.open("/tmp/partielator/file.tex","w","utf-8")
        if inside and self.settings["use_preview"] == "True":
            replace = "\n\usepackage[active,graphics]{preview}"
            replace += "\n\\begin{document}\n"
            replace += "\\begin{preview}\n"
            if "\\begin{document}" in self.header:
                a.write(self.header.replace("\\begin{document}",replace))
            else:
                a.write(self.header)
                a.write(replace)
            a.write(unicode(enonce,"utf-8"))
            if "\\end{document}" in self.footer:
                a.write(self.footer.replace("\\end{document}","\\end{preview}\n\\end{document}"))
            else:
                a.write(self.footer)
                a.write("\n\\end{preview}\n")
                a.write("\n\\end{document}")
        elif inside:
            a.write(self.header)
            if "\\begin{document}" not in self.header:
                a.write("\n\\begin{document}\n")
            a.write(unicode(enonce,"utf-8"))
            a.write(self.footer)
            a.write("\n\\end{document}")
        else:
            a.write(enonce)
        a.close()
        if inside:
            for cmd in self.compile_seq[self.settings["preferred compile sequence"]]:
                os.system(str(cmd).replace("!file", "/tmp/partielator/file"))
        else:
            for cmd in self.compile_seq[self.settings["preferred compile sequence for exportation"]]:
                os.system(str(cmd).replace("!file", "/tmp/partielator/file"))
        return True


    def show_preview_outside(self, enonce):
        if self.show_preview(enonce, 0):
            os.system(self.settings["file_viewer"] + " /tmp/partielator/file." + self.settings["preferred type of export"] + " &")

    def show_preview_inside(self, enonce):
        if self.show_preview(enonce):
            if self.settings["embedded viewer"] == "embedded (with dvipng)":
                self.preview.setPixmap(QtGui.QPixmap("/tmp/partielator/file.png"))
                if self.whatson == "tree":
                    self.verticalScrollBar.setValue(0)
            else:
                self.okupart.openDocument("/tmp/partielator/file."  + self.settings["type_of_file"])
                self.okupart.goToPage(0)

    def recompile(self):
        """Recompile tex file e.g. to get references right"""
        if self.enonce == "None":
            return
        os.chdir('/tmp/partielator')
        for cmd in self.compile_seq[self.settings["preferred compile sequence"]]:
            os.system(str(cmd).replace("!file", "/tmp/partielator/file"))
        if self.settings["embedded viewer"] == "embedded (with dvipng)":
            self.preview.setPixmap(QtGui.QPixmap("/tmp/partielator/file.png"))
        else:
            self.okupart.openDocument("/tmp/partielator/file."  + self.settings["type_of_file"])

    def show_preview_tree(self):
        """Show preview of the current tex file in the tree"""
        if not self.treeWidget.currentItem().childCount():
            item = self.treeWidget.currentItem().parent()
        else:
            item = self.treeWidget.currentItem()
        if not item.child(0).childCount():
            enonce = ""
            for i in range(item.childCount()):
                enonce += item.child(i).enonce
            self.show_preview_inside(enonce)
            self.whatson = "tree"

    def whole_thing(self):
        """Exercises in the tableWidget"""
        whole_thing = ""
        for i in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(0,i)
            whole_thing += self.tableWidget.item(0,i).enonce + "\n\n"
        return whole_thing

    def show_preview_list(self):
        whole_thing = self.whole_thing()
        if whole_thing:
            self.show_preview_inside(whole_thing)
            self.whatson = "list"

    def list_child_exercises(self, parent, l=[]):
        """List all child exercises of parent item"""
        if parent.childCount():
            for i in range(parent.childCount()):
                item = parent.child(i)
                self.list_child_exercises(item,l)
        else:
            l.append({'titre':parent.titre,'enonce':parent.enonce})
        return l

    def list_children(self, parent, l=[]):
        """List all children of a parent item"""
        if parent.childCount():
            for i in range(parent.childCount()):
                item = parent.child(i)
                self.list_children(item,l)
        else:
            l.append(parent)
        return l

    def parcourir(self):
        dirName = QtGui.QFileDialog.getExistingDirectory(MainWindow,\
                  QtGui.QApplication.translate("Form", "Pick a folder", None, QtGui.QApplication.UnicodeUTF8),
                  self.settings["tex_path"])
        if dirName:
            self.settings["tex_path"] = dirName
            self.lineEdit.setText(self.settings["tex_path"])

    ################### Moving elements in the tableWidget #########################
    def gouptable(self):
        """Move selected element up in the list"""
        tuple_selected = [(self.tableWidget.row(item),item) for item in self.tableWidget.selectedItems()]
        tuple_selected = sorted(tuple_selected, key=lambda tup: tup[0]) #sort by position in the table
        if tuple_selected:
            if tuple_selected[0][0] == 0:
                return
            else:
                self.tableWidget.selectionModel().clearSelection()
                #Set tableWidget to accept multiselection withouth pressing shift or control
                self.tableWidget.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
                for tup in tuple_selected:
                    goingup = self.tableWidget.takeItem(tup[0],0)
                    goingdown = self.tableWidget.takeItem(tup[0]-1,0)
                    #self.tableWidget.insertRow(tup[0])
                    self.tableWidget.setItem(tup[0],0,goingdown)
                    self.tableWidget.setItem(tup[0]-1,0,goingup)
                    self.tableWidget.setCurrentCell(tup[0]-1,0)
                #Set tableWidget back to single selection
                self.tableWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)

    def godowntable(self):
        """Move selected element down in the list"""
        tuple_selected = [(self.tableWidget.row(item),item) for item in self.tableWidget.selectedItems()]
        tuple_selected = sorted(tuple_selected, key=lambda tup: -tup[0]) #sort by position in the table
        if tuple_selected:
            if tuple_selected[0][0] == self.tableWidget.rowCount()-1:
                return
            else:
                self.tableWidget.selectionModel().clearSelection()
                #Set tableWidget to accept multiselection withouth pressing shift or control
                self.tableWidget.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
                for tup in tuple_selected:
                    goingdown = self.tableWidget.takeItem(tup[0],0)
                    goingup = self.tableWidget.takeItem(tup[0]+1,0)
                    #self.tableWidget.insertRow(tup[0])
                    self.tableWidget.setItem(tup[0]+1,0,goingdown)
                    self.tableWidget.setItem(tup[0],0,goingup)
                    self.tableWidget.setCurrentCell(tup[0]+1,0)
            #Set tableWidget back to single selection
            self.tableWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)

    ################### Moving elements in a listWidget #########################
    def goup(self, listWidget):
        """Move selected element up in the list"""
        numero = listWidget.currentRow()
        if numero > 0:
            item = listWidget.item(numero)
            listWidget.takeItem(numero)
            listWidget.insertItem(numero-1,item)
            listWidget.setCurrentItem(item)

    def godown(self, listWidget):
        """Move selected element down in the list"""
        numero = listWidget.currentRow()
        if numero > -1 and (numero < listWidget.count()-1):
            item = listWidget.item(numero)
            listWidget.takeItem(numero)
            listWidget.insertItem(numero+1,item)
            listWidget.setCurrentItem(item)


    ################# Compile menu ###################################

    def populate_compile(self):
        """Flush compile menu, populate it and add slots"""
        for key in self.actionCompile:
            self.menuCompilation.removeAction(self.actionCompile[key])
        for key in sorted(self.compile_seq):
            self.actionCompile[key] = QtGui.QAction(MainWindow)
            self.actionCompile[key].setObjectName(key)
            self.actionCompile[key].setText(key)
            icon = QtGui.QIcon()
            if self.settings["preferred compile sequence"] == key:
                icon.addPixmap(QtGui.QPixmap(":/all/icones/apply.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.actionCompile[key].setIcon(icon)
            self.menuCompilation.addAction(self.actionCompile[key])
            #Adding slots to the compile submenu
        def plop(key):
            """lambda function inside a loop acts oddly (to me)"""
            return lambda:self.change_compile(key)
        for key in self.compile_seq.keys():
            QtCore.QObject.connect(self.actionCompile[key],QtCore.SIGNAL("triggered()"),plop(key))
                
    def change_compile(self,key):
        """A new compile sequence has been clicked"""
        #updating settings
        self.settings["preferred compile sequence"] = key
        for key in sorted(self.compile_seq):
            icon = QtGui.QIcon()
            if self.settings["preferred compile sequence"] == key:
                icon.addPixmap(QtGui.QPixmap(":/all/icones/apply.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.actionCompile[key].setIcon(icon)

    ################# TreeWidget stuff  #######################################################
    
    def treeSelectionChanged(self):
        """When the selection changes in the treeWidget, we need to
           enable/disable the "+" button
           The "+" button is disable when:
              - nothing is selected
              - the selection contains a parent and one of his children
        """
        selectedItems = self.treeWidget.selectedItems()
        if not selectedItems:
            self.button_add.setEnabled(False)
        else:
            noAmbiguity = True
            for item in selectedItems:
                if item.parent() in selectedItems:
                    noAmbiguity = False
                    break
            if noAmbiguity:
                self.button_add.setEnabled(True)
            else:
                self.button_add.setEnabled(False)

    ################# Dealing with MainWindow's tableWidget ###################################
    
    def tableSelectionChanged(self):
        """When the selection changes in the tableWidget, we need to
           enable/disable the "Edit" button (depending on the number of
           elements selected)
           We also want to enable/disable the remove (-) button
        """
        selectedItems = self.tableWidget.selectedItems()
        if len(selectedItems)==1:
            self.actionEdit_exercise.setEnabled(True)
            self.pushButton_edit.setEnabled(True)
        else:
            self.actionEdit_exercise.setEnabled(False)
            self.pushButton_edit.setEnabled(False)
        rows = [self.tableWidget.row(item) for item in selectedItems]
        rows.sort()
        if not rows:#no selection
            self.button_up.setEnabled(False)
            self.button_down.setEnabled(False)
            self.button_remove.setEnabled(False)
        else:
            self.button_remove.setEnabled(True)
            if rows[0]==0:#one of the element is at the top of the table
                self.button_up.setEnabled(False)
            else:
                self.button_up.setEnabled(True)
            if rows[-1]==self.tableWidget.rowCount()-1:#one of the element is at the bottom of the table
                self.button_down.setEnabled(False)
            else:
                self.button_down.setEnabled(True)    
    
    def enable_stuff(self):
        """When there are exercises in the tableWidget,
           some buttons/actions need to be enabled.
           This function is started whenever the tableWidget
           emits the "notempty()" signal
        """
        self.pushButton_preview.setEnabled(True)
        self.actionShuffle_list.setEnabled(True)
    
    def disable_stuff(self):
        """When there are no exercise in the tableWidget,
           some buttons/actions need to be disabled.
           This function is started whenever the tableWidget
           emits the "empty()" signal
        """
        self.pushButton_preview.setEnabled(False)
        self.actionShuffle_list.setEnabled(True)
    
    def add_items(self,item):
        """Add items to the tableWidget"""
        if item.childCount():
            for k in range(item.childCount()):
                self.add_items(item.child(k))
        else:
            nb_exercises = self.tableWidget.rowCount()
            self.tableWidget.insertRow(nb_exercises)
            newitem = QtGui.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(nb_exercises+1, newitem)
            newitem.setText(str(nb_exercises+1))
            newitem = QtGui.QTableWidgetItem()
            nom = item.titre
            newitem.enonce = item.enonce
            newitem.setText(str(nom))
            self.tableWidget.setItem(nb_exercises,0,newitem)
            self.tableWidget.setCurrentItem(newitem)   
        
    def add_ex_to_table(self):
        """Add selected exercise to the tableWidget"""
        items = self.treeWidget.selectedItems()
        if items:
            self.tableWidget.emit(QtCore.SIGNAL("notempty()"))
        self.tableWidget.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.tableWidget.selectionModel().clearSelection()
        for item in items:
            self.add_items(item)
        self.tableWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
                
    def add_ex_to_table_from_double_click(self):
        """An item has been double clicked on the tree
           add exercise to the table iff it is a leaf
        """
        items = self.treeWidget.selectedItems()
        if len(items)>1 or items[0].childCount():
            return
        else:
            self.add_ex_to_table()
            self.tableWidget.emit(QtCore.SIGNAL("notempty()"))

    def remove_exercises(self):
        """Delete selected elements from the tableWidget"""
        selected_items = self.tableWidget.selectedItems()
        for item in selected_items:
            self.tableWidget.removeRow(self.tableWidget.row(item))
        if not self.tableWidget.rowCount():
            self.tableWidget.emit(QtCore.SIGNAL("empty()"))


    ############################# ABOUT #######################################
    def apropos(self):
        Dialog_apropos = QtGui.QDialog()
        ui_apropos = guiabout.Ui_Dialog()
        ui_apropos.setupUi(Dialog_apropos)
        #guiaboutplus.updateUi(ui_apropos)
        Dialog_apropos.exec_()


    ############################# PREFERENCES WINDOW ##########################

    def parcourir_tex_path(self):
        guiprefsplus.parcourir_tex_path(self)

    def parcourir_sav(self):
        guiprefsplus.parcourir_sav(self)

    def removetags(self):
        guiprefsplus.removetags(self)

    def addtags(self):
        guiprefsplus.addtags(self)

    def addtocompileseq(self):
        guiprefsplus.addtocompileseq(self)

    def removefromcompileseq(self):
        self.ui_prefs.listWidget_comp.takeItem(self.ui_prefs.listWidget_comp.currentRow())

    def goup2(self):
        self.goup(self.ui_prefs.listWidget_comp)

    def godown2(self):
        self.godown(self.ui_prefs.listWidget_comp)

    def add_generate_config(self):
        guiprefsplus.add_generate_config(self)

    def add_compile_config(self):
        guiprefsplus.add_compile_config(self)

    def combo(self, text):
        guiprefsplus.combo(self, text)

    def comboCompile(self,text):
        guiprefsplus.comboCompile(self,text)

    def comboViewer(self,text):
        guiprefsplus.comboViewer(self,text)

    def update_generate_header(self):
        guiprefsplus.update_generate_header(self)
        
    def update_generate_footer(self):
        guiprefsplus.update_generate_footer(self)

    def prefs_delete(self):
        guiprefsplus.prefs_delete(self)
        
    def delete_compile_config(self):
        guiprefsplus.delete_compile_config(self)

    def prefs(self):
        self.Dialog_prefs = QtGui.QDialog()
        self.ui_prefs = guiprefs.Ui_Dialog()
        self.ui_prefs.setupUi(self.Dialog_prefs)
        guiprefsplus.updateUi(self, MyHighlighter)
        res = self.Dialog_prefs.exec_()
        guiprefsplus.close_prefs(self, res)

    def randomize(self):
        """Open a dialog to generate a random exam"""
        #First, let's show the dialog :
        Dialog_random = QtGui.QDialog()
        self.ui_random = guirandomize.Ui_Dialog()
        self.ui_random.setupUi(Dialog_random)
        res = Dialog_random.exec_()
        guirandomizeplus.close(self, res)

    def shuffle_list(self):
        """Open a dialog to shuffle the list of exercises"""
        #First, let's show the dialog :
        Dialog_shuffle = QtGui.QDialog()
        self.ui_shuffle = guishuffle.Ui_Dialog()
        self.ui_shuffle.setupUi(Dialog_shuffle)
        res = Dialog_shuffle.exec_()
        guishuffleplus.close(self, res)    

    def expand_collapse_me(self):
        """Expand or collapse the subtree under
           selected item
           Don't do anything if selected item is a leaf or an exercise sheet
        """
        liste = self.treeWidget.selectedItems()
        if liste:
            parent = liste[0]
            if self.treeWidget.isItemExpanded(parent):
                self.collapse(parent)
            elif parent.childCount(): #Don't do anything if parent is an exercise
                self.expand(parent)

    def collapse(self, parent):
        """Collapses the tree under the current item"""
        self.treeWidget.collapseItem(parent)
        for i in range(parent.childCount()):
            self.collapse(parent.child(i))


    def expand(self, parent):
        """Expands the tree under the current item and don't expand if no grand-children"""
        if not parent.child(0).childCount():
            return
        else:
            self.treeWidget.expandItem(parent)
            for i in range(parent.childCount()):
                self.expand(parent.child(i))


    ############################## EDITING EXERCISES #############################
    def editExerciceTableWidget(self):
        """Opens a dialog to edit an exercise"""
        #If, for some reason, there is more than one exercise selected, don't do anything
        if len(self.tableWidget.selectedItems())!=1:
            return
        #First, let's show the dialog :
        Dialog_edit = QtGui.QDialog()
        self.ui_edit = guiedit.Ui_Dialog()
        self.ui_edit.setupUi(Dialog_edit)
        self.ui_edit.textEdit.setFont(self.myfont)
        self.highlighter4 = MyHighlighter(self.ui_edit.textEdit)
        self.ui_edit.textEdit.setText(unicode(self.tableWidget.currentItem().enonce,"utf8"))
        res = Dialog_edit.exec_()
        #Then, depending on whether the user clicked ok or cancel...
        if res:
            self.tableWidget.currentItem().enonce = unicode(self.ui_edit.textEdit.toPlainText()).encode("utf8")
            if self.whatson == "list":
                self.show_preview_list()
    
    def editExerciseTreeWidget(self):
        """Opens a dialog to edit the source of an exercise so as to
           modify an existing tex file on the drive
        """
        item = self.treeWidget.selectedItems()[0]
        oldtext = item.enonce
        Dialog_edit = QtGui.QDialog()
        ui_edit = guieditsource.Ui_Dialog()
        ui_edit.setupUi(Dialog_edit)
        ui_edit.textEdit.setFont(self.myfont)
        highlighter4 = MyHighlighter(ui_edit.textEdit)
        ui_edit.textEdit.setText(unicode(oldtext,"utf8"))
        ui_edit.label_source.setText(unicode(item.filename,"utf8"))
        res = Dialog_edit.exec_()
        #Then, depending on whether the user clicked ok or cancel...
        if res:
            newtext = unicode(ui_edit.textEdit.toPlainText()).encode("utf8")
            if newtext == oldtext:
                print("Nothing to do, exercise wasn't changed")
            else:
                print("Writing changes to file...")
                f = open(item.filename,'r+')
                lines = f.read()
                lines = lines.replace(item.enonce,newtext)
                f.seek(0)
                f.write(lines)
                f.truncate()
                f.close()
                #Change the exercise in the tree according to changes made
                item.enonce = newtext
                #Update preview
                self.show_preview_tree()
        else:
            print("Aborting")

    
    ############################## EXPORTING ###############################
    def close_export(self):
        guiexportplus.close_export(self)

    def gen_next(self):
        guiexportplus.gen_next(self)

    def gen_back(self):
        guiexportplus.gen_back(self)

    def export_sources(self, key):
        return guiexportplus.export_sources(self, key)

    def update_header(self,text):
        guiexportplus.update_header(self, text)

    def update_type(self,text):
        guiexportplus.update_type(self, text)
        
    def update_compile(self,text):
        guiexportplus.update_compile(self, text)
        
    def update_generate2(self):
        guiexportplus.update_generate2(self)

    def save(self, tex_code):
        guiexportplus.save(self, tex_code, MainWindow)

    def fin_export(self):
        guiexportplus.fin_export(self)

    def export(self):
        #Create the dialog
        self.Dialog_export = QtGui.QDialog()
        self.ui_export = guiexport.Ui_Dialog()
        self.ui_export.setupUi(self.Dialog_export)
        self.ui_export.frame1.hide()
        guiexportplus.updateUi(self, MyHighlighter)
        #Opening dialog
        self.Dialog_export.exec_()


    ############################## WIZARD ###############################
    def wizard_allow_next(self):
        guiwizardplus.wizard_allow_next(self)

    def wizard_next(self):
        guiwizardplus.wizard_next(self)

    def wizard_back(self):
        guiwizardplus.wizard_back(self)

    def wizard_browse(self):
        guiwizardplus.wizard_browse(self, self.Dialog_wizard)

    def wizard_addtags(self):
        guiwizardplus.wizard_addtags(self)

    def wizard_removetags(self):
        guiwizardplus.wizard_removetags(self)

    def wizard_guess(self):
        f = self.ui_wizard.lineEdit.text()
        self.gtags, self.gheader = get_tags_header(f)
        guiwizardplus.wizard_guess(self)

    def wizard(self):
        #Create the dialog
        self.Dialog_wizard = QtGui.QDialog()
        self.ui_wizard = guiwizard.Ui_Dialog()
        self.ui_wizard.setupUi(self.Dialog_wizard)
        guiwizardplus.updateUi(self, MyHighlighter, self.Dialog_wizard)
        #Opening dialog
        res = self.Dialog_wizard.exec_()
        guiwizardplus.wizard_apply(self, res)

    ########################### TRANSLATING ########################################

    def to_french(self):
        self.settings["lang"] = "fr"
        self.show_lang_dialog()

    def to_english(self):
        self.settings["lang"] = "en"
        self.show_lang_dialog()

    def to_czech(self):
        self.settings["lang"] = "cs"
        self.show_lang_dialog()

    def to_ukrainian(self):
        self.settings["lang"] = "uk"
        self.show_lang_dialog()

    def to_german(self):
        self.settings["lang"] = "de"
        self.show_lang_dialog()

    def show_lang_dialog(self):
        Dialog_lang = QtGui.QDialog()
        ui_lang = guilangchange.Ui_Dialog()
        ui_lang.setupUi(Dialog_lang)
        Dialog_lang.exec_()
    
    ########################### EVENT FILTERING ####################################
    def close_Event(self, e):
        """Will be executed when user tries to close the main window"""
        Dialog_quit = QtGui.QDialog()
        ui_quit = guiquit.Ui_Dialog()
        ui_quit.setupUi(Dialog_quit)
        res = Dialog_quit.exec_()
        if res:
            self.nettoyage()
            self.save_size()
            e.accept()
        else:
            e.ignore()

    def show_Event(self, e):
        """Will be executed before the window is shown"""
        if self.first_time:
            self.wizard()


    def eventFilter(self, object, event):
        """filtering right click on treeWidget 
        and ctrl+C event on treeWidget/tableWidget"""
        if event.type() == 82 and object == self.treeWidget:
            object.emit(QtCore.SIGNAL("right_clicked()"))
        # If ctrl+C : copy to clipboard the source code of the selected exercise
        if event.type() == QtCore.QEvent.KeyPress:
            if event.matches(QtGui.QKeySequence.Copy):
                #ctrl+C detected
                #Is the treeWidget selected?
                if object == self.treeWidget and self.treeWidget.currentItem():
                    self.copyToClipboardFromTree()
                    return 1 #Do not pass event to next handler
                #Or is the tableWidget selected ?
                elif object == self.tableWidget and self.tableWidget.selectedItems() is not None:
                    self.copyToClipboardFromTable()
                    return 1 #Do not pass event to next handler
        return 0 #pass event to the next handler

    def copyToClipboardFromTree(self):
        """copy the source code of the selected exercises in the Tree.
           Ignores entire folders/files.
        """
        items = self.treeWidget.selectedItems()
        to_clipboard = ""
        for item in items:
            if not item.childCount():
                try:
                    to_clipboard += item.enonce.decode("utf8")
                    to_clipboard += unicode("\n","utf8")
                except:
                    to_clipboard += item.enonce
        QtGui.QApplication.clipboard().setText(to_clipboard)

    def copyToClipboardFromTable(self):
        """copy the source code of the selected exercises in the Table."""
        tuple_selected = [(self.tableWidget.row(item),item) for item in self.tableWidget.selectedItems()]
        tuple_selected = sorted(tuple_selected, key=lambda tup: tup[0]) #sort by position in the table
        to_clipboard = ""
        for tup in tuple_selected:
            try:
                to_clipboard += unicode(tup[1].enonce,"utf8")
                to_clipboard += unicode("\n","utf8")
            except:
                to_clipboard += tup[1].enonce
        QtGui.QApplication.clipboard().setText(to_clipboard)

    ########################### LEAVING TEXAMATOR ######################################
    def nettoyage(self):
        try:
            for fichier in os.listdir("/tmp/partielator"):
                os.remove(os.path.join("/tmp/partielator",fichier))
            os.rmdir("/tmp/partielator")
        except:
            print("Couldn't clean up or nothing to clean")

    def save_size(self):
        print("Leaving")
        home_dir = os.path.expanduser("~")
        self.settings["width"], self.settings["height"] = self.windowWidth(), self.windowHeight()
        self.settings["little_splitter_s1"] = self.little_splitter.sizes()[0]
        self.settings["little_splitter_s2"] = self.little_splitter.sizes()[1]
        self.settings["big_splitter_s1"] = self.big_splitter.sizes()[0]
        self.settings["big_splitter_s2"] = self.big_splitter.sizes()[1]
        f = codecs.open(os.path.join(home_dir,".partielator","basics"),'w',"utf-8")
        for key, value in self.settings.iteritems():
            f.write(key+"="+str(value)+"\n")
        f.close()

    ######################### CONTEXT MENU ON TREEWIDGET/LISTWIDGET #################
    def openMenuTree(self, position):
        """Context menu on the treeWidget"""
        selectedItems = self.treeWidget.selectedItems()
        if not selectedItems:
            return
        if len(selectedItems)>1 or not self.treeWidget.currentItem().childCount() or not self.treeWidget.currentItem().child(0).childCount():
            menu = QMenu()
            copyToClipboard = menu.addAction(QtGui.QApplication.translate("Dialog", "Copy to clipboard", None, QtGui.QApplication.UnicodeUTF8))
            copyToClipboard.setShortcut(QtGui.QKeySequence.Copy)
            copyToClipboard.triggered.connect(self.copyToClipboardFromTree)
            addToTable = menu.addAction(QtGui.QApplication.translate("Dialog", "Add", None, QtGui.QApplication.UnicodeUTF8))
            addToTable.triggered.connect(self.add_ex_to_table)
            editAction = menu.addAction(QtGui.QApplication.translate("Dialog", "Edit...", None, QtGui.QApplication.UnicodeUTF8))
            editAction.triggered.connect(self.editExerciseTreeWidget)
            if len(self.treeWidget.selectedItems())!=1 or self.treeWidget.currentItem().childCount():
                editAction.setEnabled(False)
            if not self.button_add.isEnabled():
                addToTable.setEnabled(False)
            for item in self.treeWidget.selectedItems():
                if item.childCount():
                    copyToClipboard.setEnabled(False)
                    break
            menu.exec_(self.treeWidget.viewport().mapToGlobal(position)+QtCore.QPoint(3,0))
        else:
            self.treeWidget.emit(QtCore.SIGNAL("right_clicked()"))


    def openMenuTable(self, position):
        """Context menu on the TableWidget"""
        n = len(self.tableWidget.selectedItems())
        if n>0:
            menu = QMenu()
            copyToClipboard = menu.addAction(QtGui.QApplication.translate("Dialog", "Copy to clipboard", None, QtGui.QApplication.UnicodeUTF8))
            copyToClipboard.setShortcut(QtGui.QKeySequence.Copy)
            copyToClipboard.triggered.connect(self.copyToClipboardFromTable)
            editAction = menu.addAction(QtGui.QApplication.translate("Dialog", "Edit...", None, QtGui.QApplication.UnicodeUTF8))
            editAction.triggered.connect(self.editExerciceTableWidget)
            moveUp = menu.addAction(QtGui.QApplication.translate("Dialog", "Move up", None, QtGui.QApplication.UnicodeUTF8))
            moveUp.triggered.connect(self.gouptable)
            moveDown = menu.addAction(QtGui.QApplication.translate("Dialog", "Move down", None, QtGui.QApplication.UnicodeUTF8))
            moveDown.triggered.connect(self.godowntable)
            shuffle = menu.addAction(QtGui.QApplication.translate("Dialog", "Shuffle", None, QtGui.QApplication.UnicodeUTF8))
            shuffle.triggered.connect(lambda:guishuffleplus.shuffleFromContext(self.tableWidget))
            remove = menu.addAction(QtGui.QApplication.translate("Dialog", "Remove", None, QtGui.QApplication.UnicodeUTF8))
            remove.triggered.connect(self.remove_exercises)
            if n<2:
                shuffle.setEnabled(False)
            if not self.button_remove.isEnabled():
                remove.setEnabled(False)
            if not self.pushButton_edit.isEnabled():
                editAction.setEnabled(False)
            if not self.button_down.isEnabled():
                moveDown.setEnabled(False)
            if not self.button_up.isEnabled():
                moveUp.setEnabled(False)
                
            menu.exec_(self.tableWidget.viewport().mapToGlobal(position)+QtCore.QPoint(3,0))


    ######################### COMPLETING MAIN WINDOW #################################
    def setupUi2(self,Form):
        """Adds what's missing to the main Window"""
        Ui_MainWindow.setupUi(self, Form)
        Form.closeEvent = self.close_Event
        Form.showEvent = self.show_Event
        self.actionCompile = {} #dictionnary containing the QAction in the Compile submenu
        self.populate_compile()
        #Context menus on treeWidget and tableWidget
        self.treeWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.treeWidget.customContextMenuRequested.connect(self.openMenuTree)
        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget.customContextMenuRequested.connect(self.openMenuTable)
        #lineEdit
        self.lineEdit.setText(self.settings["tex_path"])
        #Table
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        QtCore.QObject.connect(self.actionShuffle_list,QtCore.SIGNAL("triggered()"),self.shuffle_list)
        QtCore.QObject.connect(self.actionGenerate_Random_Exam,QtCore.SIGNAL("triggered()"),self.randomize)
        QtCore.QObject.connect(self.tableWidget,QtCore.SIGNAL("notempty()"),self.enable_stuff)
        QtCore.QObject.connect(self.tableWidget,QtCore.SIGNAL("empty()"),self.disable_stuff)
        QtCore.QObject.connect(self.treeWidget,QtCore.SIGNAL("itemDoubleClicked(QTreeWidgetItem*,int)")\
        ,self.add_ex_to_table_from_double_click)
        QtCore.QObject.connect(self.button_add,QtCore.SIGNAL("clicked()"),self.add_ex_to_table)
        QtCore.QObject.connect(self.button_remove,QtCore.SIGNAL("clicked()"),self.remove_exercises)
        QtCore.QObject.connect(self.button_up,QtCore.SIGNAL("clicked()"),self.gouptable)
        QtCore.QObject.connect(self.button_down,QtCore.SIGNAL("clicked()"),self.godowntable)
        QtCore.QObject.connect(self.button_refresh,QtCore.SIGNAL("clicked()"),self.create_main_tree)
        QtCore.QObject.connect(self.treeWidget,QtCore.SIGNAL("itemClicked(QTreeWidgetItem*,int)")\
        ,self.show_preview_tree)        
        QtCore.QObject.connect(self.tableWidget,QtCore.SIGNAL("itemSelectionChanged()")\
        ,self.tableSelectionChanged)
        QtCore.QObject.connect(self.treeWidget,QtCore.SIGNAL("itemSelectionChanged()")\
        ,self.treeSelectionChanged)
        QtCore.QObject.connect(self.tableWidget,QtCore.SIGNAL("itemDoubleClicked(QTableWidgetItem*)")\
        ,self.editExerciceTableWidget)
        QtCore.QObject.connect(self.button_save,QtCore.SIGNAL("clicked()"),self.export)
        QtCore.QObject.connect(self.button_recompile,QtCore.SIGNAL("clicked()"),self.recompile)
        QtCore.QObject.connect(self.actionQuitter,QtCore.SIGNAL("triggered()"),MainWindow.close)
        QtCore.QObject.connect(self.actionStart_Wizard,QtCore.SIGNAL("triggered()"),self.wizard)
        QtCore.QObject.connect(self.actionPrefs,QtCore.SIGNAL("triggered()"),self.prefs)
        QtCore.QObject.connect(self.actionExport,QtCore.SIGNAL("triggered()"),self.export)
        QtCore.QObject.connect(self.actionA_propos,QtCore.SIGNAL("triggered()"),self.apropos)
        QtCore.QObject.connect(self.actionEdit_exercise,QtCore.SIGNAL("triggered()"),self.editExerciceTableWidget)
        QtCore.QObject.connect(self.actionFrench,QtCore.SIGNAL("triggered()"),self.to_french)
        QtCore.QObject.connect(self.actionEnglish,QtCore.SIGNAL("triggered()"),self.to_english)
        QtCore.QObject.connect(self.actionCzech,QtCore.SIGNAL("triggered()"),self.to_czech)
        QtCore.QObject.connect(self.actionUkrainian,QtCore.SIGNAL("triggered()"),self.to_ukrainian)
        QtCore.QObject.connect(self.actionGerman,QtCore.SIGNAL("triggered()"),self.to_german)
        QtCore.QObject.connect(self.pushButton_edit,QtCore.SIGNAL("clicked()"), self.editExerciceTableWidget)
        QtCore.QObject.connect(self.actionExpand_Collapse,QtCore.SIGNAL("triggered()"),self.expand_collapse_me)
        QtCore.QObject.connect(self.pushButton_parcourir,QtCore.SIGNAL("clicked()"),self.parcourir)
        QtCore.QObject.connect(self.pushButton_preview,QtCore.SIGNAL("clicked()"),self.show_preview_list)
        QtCore.QObject.connect(self.lineEdit_search,QtCore.SIGNAL("textChanged(QString)"),self.search)
        #eventFilter to detect right click on the treeWidget and copy event on an exercise
        Form.eventFilter = self.eventFilter
        self.treeWidget.installEventFilter(Form)
        self.tableWidget.installEventFilter(Form)
        QtCore.QObject.connect(self.treeWidget,QtCore.SIGNAL("right_clicked()"),self.expand_collapse_me)       
        #Okular preview
        if self.settings["embedded viewer"] == "okular":
            try:
                from PyKDE4.kdecore import KUrl
                from PyKDE4.kdecore import ki18n, KAboutData, KCmdLineArgs
                from PyKDE4.kdecore import KLibLoader as ll
                from PyKDE4.kdeui import KApplication
                import PyKDE4.kparts as kp
                self.okupart = ll.self().factory('okularpart').create()
                self.okularlayout.setWidget(self.okupart.widget())
            except:
                print("Error trying to load PyKDE4 module")
                print("Please install python-kde4 and try again or select embedded viewer (dvipng) in the preferences window")
        else:
            self.okularlayout.setBackgroundRole(QtGui.QPalette.Light)
            self.preview = QtGui.QLabel()
            self.okularlayout.setWidget(self.preview)
            self.verticalScrollBar = self.okularlayout.verticalScrollBar()
        #Splitter sizes :
        self.windowHeight = Form.height
        self.windowWidth = Form.width
        l = int(self.settings["width"])
        w = int(self.settings["height"])
        l1 = [int(self.settings["little_splitter_s1"]) , int(self.settings["little_splitter_s2"])]
        l2 = [int(self.settings["big_splitter_s1"]), int(self.settings["big_splitter_s2"])]
        Form.resize(l,w)
        self.big_splitter.setSizes(l2)
        self.little_splitter.setSizes(l1)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    #Translate app ?
    settings = gimme_my_settings()
    x = settings[4]
    if x["lang"] != "en":
        p = os.path.abspath(sys.argv[0])
        while os.path.islink(p): #get rid of simlinks
            p = os.path.abspath(os.readlink(p))
        full_path = os.path.split(p)[0] #get the path where the program is
        t = QtCore.QTranslator()
        t.load(os.path.join(full_path, "ts_files/TeXamator_"+x["lang"]))
        #t.load(os.path.join(full_path, "ts_files/TeXamator_de"))
        QtCore.QCoreApplication.installTranslator(t)
    #Let's go !
    MainWindow = QtGui.QMainWindow()
    ui = MonApplication(settings)
    ui.setupUi2(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

