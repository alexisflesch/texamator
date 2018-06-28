#!/usr/bin/python3
# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os
from random import shuffle
from partielatormods import *

from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import time

_translate = QtCore.QCoreApplication.translate

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class MonApplication(Ui_MainWindow):
    
    def __init__(self, settings):
        super(Ui_MainWindow, self).__init__()
        self.first_time, self.tags, self.settings, self.compile_seq, self.preamblesPostambles = settings
        #self.first_time, self.tags, self.header, self.footer, self.settings, self.compile_seq, self.generate = settings
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
        topdir = self.lineEdit.text()
        if topdir[-1] == "/":
            topdir = topdir[0:-1]
        nb_ex, self.treeTeX = crazyparser(topdir,self.tags)
        self.fillTheTree(self.treeTeX,nb_ex)
        self.actionExpand_Collapse.setEnabled(True)
        #if the search line is not empty, update the tree
        string = self.lineEdit_search.text()
        if string:
            self.search()


    def search(self):
        """Search for a string in folder/file names and in the exercices using treeTeX"""
        string = self.lineEdit_search.text()
        string = string.lower()
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
            self.treeWidget.setHeaderLabel(_translate("Dialog", "No exercise found"))
        elif nb_ex == 1:
            self.treeWidget.setHeaderLabel(_translate("Dialog", "1 exercise found"))
        else:
            self.treeWidget.setHeaderLabel(str(nb_ex) + " " + _translate("Dialog","exercises found"))
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
                itemDict[fullpath] = QtWidgets.QTreeWidgetItem(itemDict[parent])
                itemDict[fullpath].setText(0, nom)
                itemDict[fullpath].setIcon(0, folderIcon)

                for i in c:#TeX file
                    nb = len(i[1]) #number of exercices in the file
                    nom_tex = i[0][:-4]
                    nom2 = nom_tex + " (" + str(nb) + ")"
                    nom_element = os.path.join(fullpath,i[0])
                    itemDict[nom_element] = QtWidgets.QTreeWidgetItem(itemDict[fullpath])
                    itemDict[nom_element].setText(0, nom2)
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
                            elif 9 < compteur_exos < 100:
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
                        itemDict[nom_cp_exo] = QtWidgets.QTreeWidgetItem(itemDict[nom_element])
                        itemDict[nom_cp_exo].setText(0, nom_exo)
                        itemDict[nom_cp_exo].enonce = j
                        itemDict[nom_cp_exo].titre = nom_tex + " - ex " + str(compteur_exos)
                        itemDict[nom_cp_exo].filename = os.path.join(fullpath, i[0])
        self.treeWidget.sortItems(0,QtCore.Qt.AscendingOrder)


    def show_preview(self, enonce, inside=1):
        if enonce == self.enonce and inside:  #only run LaTeX if necessary
            return False
        self.enonce = enonce
        if inside:
            a = codecs.open("/tmp/texamator/file.tex","w","utf-8")
        else:
            a = codecs.open("/tmp/texamator/export.tex","w","utf-8")
        if inside:
            a.write(self.preamblesPostambles[self.settings["preferred preamble"]][0])
            if "\\begin{document}" not in self.preamblesPostambles[self.settings["preferred preamble"]][0]:
                a.write("\n\\begin{document}\n")
            a.write(enonce)
            a.write(self.preamblesPostambles[self.settings["preferred preamble"]][1])
            a.write("\n\\end{document}")
        else:
            a.write(enonce)
        a.close()
        if inside:
            for cmd in self.compile_seq[self.settings["preferred compile sequence"]]:
                os.system(str(cmd))
        else:
            for cmd in self.compile_seq[self.settings["preferred compile sequence for exportation"]]:
                os.system(str(cmd).replace("file","export"))
        return True

    def show_preview_outside(self, enonce):
        if self.show_preview(enonce, 0):
            sequence = self.settings["preferred compile sequence for exportation"]
            os.system(self.settings["file_viewer"] + " /tmp/texamator/export.pdf &")

    def show_preview_inside(self, enonce):
        if self.show_preview(enonce):
            self.showPdf()

    def showPdf(self):
        """Changes the pdf of self.pdfwidget and shows it"""
        print("Updating pdf")
        self.pdfwidget.createPdf("/tmp/texamator/file.pdf")
        self.pdfScrollBar.setSliderPosition(0)

    def recompile(self):
        """Recompile tex file e.g. to get references right"""
        if self.enonce == "None":
            return
        for cmd in self.compile_seq[self.settings["preferred compile sequence"]]['sequence']:
            os.system(str(cmd))
        self.showPdf()

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
            item = self.tableWidget.item(i,0)
            whole_thing += self.tableWidget.item(i,0).enonce + "\n\n"
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
        dirName = QtWidgets.QFileDialog.getExistingDirectory(MainWindow,\
                  _translate("Form", "Pick a folder"), self.settings["tex_path"])
        if dirName:
            self.settings["tex_path"] = dirName
            self.lineEdit.setText(self.settings["tex_path"])

    ################### Moving elements in the tableWidget #########################
    def gouptable(self):
        """Move selected element up in the list"""
        tuple_selected = [(self.tableWidget.row(item),item) for item in self.tableWidget.selectedItems()\
                            if not self.tableWidget.column(item)]
        tuple_selected = sorted(tuple_selected, key=lambda tup: tup[0]) #sort by position in the table
        if tuple_selected:
            if tuple_selected[0][0] == 0:
                return
            else:
                self.tableWidget.selectionModel().clearSelection()
                #Set tableWidget to accept multiselection withouth pressing shift or control
                self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
                for tup in tuple_selected:
                    goingup = self.tableWidget.takeItem(tup[0],0)
                    goingdown = self.tableWidget.takeItem(tup[0]-1,0)
                    self.tableWidget.setItem(tup[0],0,goingdown)
                    self.tableWidget.setItem(tup[0]-1,0,goingup)
                    self.tableWidget.setCurrentCell(tup[0]-1,0)                
                #Set tableWidget back to single selection
                self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)

    def godowntable(self):
        """Move selected element down in the list"""
        tuple_selected = [(self.tableWidget.row(item),item) for item in self.tableWidget.selectedItems()\
                            if not self.tableWidget.column(item)]
        tuple_selected = sorted(tuple_selected, key=lambda tup: -tup[0]) #sort by position in the table
        if tuple_selected:
            if tuple_selected[0][0] == self.tableWidget.rowCount()-1:
                return
            else:
                self.tableWidget.selectionModel().clearSelection()
                #Set tableWidget to accept multiselection withouth pressing shift or control
                self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
                for tup in tuple_selected:
                    goingdown = self.tableWidget.takeItem(tup[0],0)
                    goingup = self.tableWidget.takeItem(tup[0]+1,0)
                    #self.tableWidget.insertRow(tup[0])
                    self.tableWidget.setItem(tup[0]+1,0,goingdown)
                    self.tableWidget.setItem(tup[0],0,goingup)
                    self.tableWidget.setCurrentCell(tup[0]+1,0)
            #Set tableWidget back to single selection
            self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)

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
            self.actionCompile[key] = QtWidgets.QAction(MainWindow)
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
        for key in list(self.compile_seq.keys()):
            self.actionCompile[key].triggered.connect(plop(key))
            #QtCore.SIGNAL("triggered()"),plop(key))
                
    def change_compile(self,key):
        """A new compile sequence has been clicked"""
        #updating settings
        self.settings["preferred compile sequence"] = key
        for key in sorted(self.compile_seq):
            icon = QtGui.QIcon()
            if self.settings["preferred compile sequence"] == key:
                icon.addPixmap(QtGui.QPixmap(":/all/icones/apply.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.actionCompile[key].setIcon(icon)


    ################# Preamble menu ###################################

    def populate_preamble(self):
        """Flush preamble menu, populate it and add slots"""
        for key in self.actionPreamble:
            self.menuPreamble.removeAction(self.actionPreamble[key])
        for key in sorted(self.preamblesPostambles):
            self.actionPreamble[key] = QtWidgets.QAction(MainWindow)
            self.actionPreamble[key].setObjectName(key)
            self.actionPreamble[key].setText(key)
            icon = QtGui.QIcon()
            if self.settings["preferred preamble"] == key:
                icon.addPixmap(QtGui.QPixmap(":/all/icones/apply.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.actionPreamble[key].setIcon(icon)
            self.menuPreamble.addAction(self.actionPreamble[key])
            #Adding slots to the compile submenu
        def plop(key):
            """lambda function inside a loop acts oddly (to me)"""
            return lambda:self.change_preamble(key)
        for key in list(self.preamblesPostambles.keys()):
            self.actionPreamble[key].triggered.connect(plop(key))
            #QtCore.SIGNAL("triggered()"),plop(key))
                
    def change_preamble(self,key):
        """A new preamble sequence has been clicked"""
        #updating settings
        self.settings["preferred preamble"] = key
        for key in sorted(self.preamblesPostambles):
            icon = QtGui.QIcon()
            if self.settings["preferred preamble"] == key:
                icon.addPixmap(QtGui.QPixmap(":/all/icones/apply.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.actionPreamble[key].setIcon(icon)


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
           Finally, we want to enable/disable the Preview button and enable/disable the shuffle list function
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
            if self.settings['AMC']=='False':
                self.button_remove.setEnabled(True)
                if rows[0]==0:#one of the element is at the top of the table
                    self.button_up.setEnabled(False)
                else:
                    self.button_up.setEnabled(True)
                if rows[-1]==self.tableWidget.rowCount()-1:#one of the element is at the bottom of the table
                    self.button_down.setEnabled(False)
                else:
                    self.button_down.setEnabled(True)
            elif self.tableWidget.item(rows[0],0).isSelected():
                #selection includes an exercise name (and maybe an element name)
                self.button_remove.setEnabled(True)
                if rows[0]==0:#one of the element is at the top of the table
                    self.button_up.setEnabled(False)
                else:
                    self.button_up.setEnabled(True)
                if rows[-1]==self.tableWidget.rowCount()-1:#one of the element is at the bottom of the table
                    self.button_down.setEnabled(False)
                else:
                    self.button_down.setEnabled(True)
            else:
                #selection concerns only element names
                self.button_remove.setEnabled(False)
                self.button_up.setEnabled(False)
                self.button_down.setEnabled(False)
        #Enable/disable preview button + shuffle action
        if self.tableWidget.rowCount():
            self.pushButton_preview.setEnabled(True)
            self.actionShuffle_list.setEnabled(True)
        else:
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
            newitem = QtWidgets.QTableWidgetItem()
            newitem.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled )
            nom = item.titre
            newitem.enonce = item.enonce
            newitem.setText(str(nom))
            self.tableWidget.setItem(nb_exercises,0,newitem)
            self.tableWidget.setCurrentItem(newitem)

    def findAMCGroup(self,enonce):
        """When given an item from the treeWidget,
           try to find its AMC group name (if it has one)
        """
        firstLine = enonce.split('%')[0]
        firstLine = enonce.split('\n')[0]
        if r'\begin{'+self.settings['AMC-env']+'}' in firstLine:
            a = firstLine.split(self.settings['AMC-env']+'}')[1]
            res = ''
            cpt = 1
            for i in a[1:]:
                if i=='}':
                    cpt -= 1
                elif i=='{':
                    cpt += 1
                if cpt==0:
                    break
                res += i
            return res
        else:
            return ''
        
    def add_ex_to_table(self):
        """Add selected exercise to the tableWidget
           Show a warning when trying to add (at least) an entire folder
           to the project (that's the first for loop)
        """
        items = self.treeWidget.selectedItems()
        for item in items:
            if item.childCount() and item.child(0).childCount():
                Dialog_warning = QtWidgets.QDialog()
                ui_warning = guidepthwarning.Ui_Dialog()
                ui_warning.setupUi(Dialog_warning)
                res = Dialog_warning.exec_()
                if not res:
                    return
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.tableWidget.selectionModel().clearSelection()
        for item in items:
            self.add_items(item)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tableSelectionChanged()
                
    def add_ex_to_table_from_double_click(self):
        """An item has been double clicked on the tree
           add exercise to the table iff it is a leaf
        """
        items = self.treeWidget.selectedItems()
        if len(items)>1 or items[0].childCount():
            return
        else:
            self.add_ex_to_table()
            self.tableSelectionChanged()
            self.tableWidget.itemSelectionChanged.emit()

    def remove_exercises(self):
        """Delete selected elements from the tableWidget"""
        for item in self.tableWidget.selectedItems():
            try:
                self.tableWidget.removeRow(self.tableWidget.row(item))
            except:
                print("Error removing item from table")
                pass
        self.tableSelectionChanged()


    ############################# ABOUT #######################################
    def apropos(self):
        Dialog_apropos = QtWidgets.QDialog()
        ui_apropos = guiabout.Ui_Dialog()
        ui_apropos.setupUi(Dialog_apropos)
        guiaboutplus.updateUi(ui_apropos)
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
        self.Dialog_prefs = QtWidgets.QDialog()
        self.ui_prefs = guiprefs.Ui_Dialog()
        self.ui_prefs.setupUi(self.Dialog_prefs)
        guiprefsplus.updateUi(self, MyHighlighter)
        res = self.Dialog_prefs.exec_()
        guiprefsplus.close_prefs(self, res)

    def randomize(self):
        """Open a dialog to generate a random exam"""
        #First, let's show the dialog :
        Dialog_random = QtWidgets.QDialog()
        self.ui_random = guirandomize.Ui_Dialog()
        self.ui_random.setupUi(Dialog_random)
        res = Dialog_random.exec_()
        guirandomizeplus.close(self, res)

    def shuffle_list(self):
        """Open a dialog to shuffle the list of exercises"""
        #First, let's show the dialog :
        Dialog_shuffle = QtWidgets.QDialog()
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
            if parent.isExpanded():
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
        #Or, if element is an AMC group name, pass to the next handler
        if self.tableWidget.selectedItems()[0].column():
            self.tableWidget.editItem(self.tableWidget.selectedItems()[0])
        else:
            #First, let's show the dialog :
            Dialog_edit = QtWidgets.QDialog()
            self.ui_edit = guiedit.Ui_Dialog()
            self.ui_edit.setupUi(Dialog_edit)
            #Window geometry
            w = self.settings["edit width"]
            h = self.settings["edit height"]
            Dialog_edit.resize(int(w), int(h))
            #Highlighter
            self.ui_edit.textEdit.setFont(self.myfont)
            self.highlighter4 = MyHighlighter(self.ui_edit.textEdit)
            self.ui_edit.textEdit.setText(self.tableWidget.currentItem().enonce)
            res = Dialog_edit.exec_()
            #Keep window ratio for next time 
            self.settings["edit width"] = str(Dialog_edit.width())
            self.settings["edit height"] = str(Dialog_edit.height())
            #Then, depending on whether the user clicked ok or cancel...
            if res:
                self.tableWidget.currentItem().enonce = self.ui_edit.textEdit.toPlainText()
                if self.settings['AMC']=='True':
                    row = self.tableWidget.currentRow()
                    item = self.tableWidget.item(row,1)
                    item.setText(self.findAMCGroup(self.tableWidget.currentItem().enonce))
                if self.whatson == "list":
                    self.show_preview_list()
    
    def itemChangedTable(self, item):
        """This function is called whenever the data of an item
           has changed in the tableWidget.
        """
        if self.settings['AMC']=='True' and not item.column():
            row = item.row()
            itemEnonce = self.tableWidget.item(row,0)
            itemAMC = self.tableWidget.item(row,1)
            if not itemAMC:
                itemAMC = QtWidgets.QTableWidgetItem()
                itemAMC.setFlags( QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled )
                itemAMC.setText(self.findAMCGroup(itemEnonce.enonce))
                self.tableWidget.setItem(row,1,itemAMC)
            itemAMC.setText(self.findAMCGroup(itemEnonce.enonce))
        elif self.settings['AMC']=='True' and item.column():
            if item.text():
                self.changeElement(self.tableWidget.item(item.row(),0),item.text())
            else:
                item.setText(self.findAMCGroup(self.tableWidget.item(item.row(),0).enonce))
    
    def editExerciseTreeWidget(self):
        """Opens a dialog to edit the source of an exercise so as to
           modify an existing tex file on the drive
        """
        item = self.treeWidget.selectedItems()[0]
        oldtext = item.enonce
        Dialog_edit = QtWidgets.QDialog()
        ui_edit = guieditsource.Ui_Dialog()
        ui_edit.setupUi(Dialog_edit)
        #Window geometry
        w = self.settings["edit width"]
        h = self.settings["edit height"]
        Dialog_edit.resize(int(w), int(h))
        #Highlighter
        ui_edit.textEdit.setFont(self.myfont)
        highlighter4 = MyHighlighter(ui_edit.textEdit)
        ui_edit.textEdit.setText(oldtext)
        ui_edit.label_source.setText(item.filename)
        res = Dialog_edit.exec_()
        #Keep window ratio for next time 
        self.settings["edit width"] = str(Dialog_edit.width())
        self.settings["edit height"] = str(Dialog_edit.height())
        #Then, depending on whether the user clicked ok or cancel...
        if res:
            newtext = ui_edit.textEdit.toPlainText()
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

    def create_document(self, key):
        return guiexportplus.create_document(self, key)

    def compile_export(self):
        return guiexportplus.compile_export(self)
    
    def source_export(self):
        return guiexportplus.source_export(self)

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

    def createAMCMacros(self, elementsList, spinBoxes):
        guiexportamcplus.createAMCMacros(self, elementsList, spinBoxes)

    def export(self):
        """Export the tableWidget to an exercise sheet
           If AMC is enabled, look for groups of questions
           and show the corresponding Dialog
        """
        if self.settings['AMC']=='True':
            elementsList = self.listAMCGroups()
            if elementsList and elementsList!=['']:
                Dialog_AMC = QtWidgets.QDialog()
                ui_AMC = guiexportamc.Ui_dialog()
                ui_AMC.setupUi(Dialog_AMC)
                guiexportamcplus.updateUi(self, ui_AMC, elementsList)
                res = Dialog_AMC.exec_()
                if res:
                    self.createAMCMacros(elementsList, self.spinBoxes)
                else:
                    self.AMC_texte = ''
        #Create the dialog
        self.Dialog_export = QtWidgets.QDialog()
        self.ui_export = guiexport.Ui_Dialog()
        self.ui_export.setupUi(self.Dialog_export)
        guiexportplus.updateUi(self, MyHighlighter)
        #Opening dialog
        self.Dialog_export.exec_()


    ############################## SHUFFLE ##############################
    
    def shuffleFromContext(self):
        guishuffleplus.shuffleFromContext(self)
    
    def shuffleTable(self, itemsList, fullList):
        guishuffleplus.shuffleTable(self, itemsList, fullList)

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
        self.Dialog_wizard = QtWidgets.QDialog()
        self.ui_wizard = guiwizard.Ui_Dialog()
        self.ui_wizard.setupUi(self.Dialog_wizard)
        guiwizardplus.updateUi(self, MyHighlighter, self.Dialog_wizard)
        #Opening dialog
        res = self.Dialog_wizard.exec_()
        guiwizardplus.wizard_apply(self, res)

    def warningNewVersion(self):
        #Create the dialog
        self.Dialog_warningNewVersion = QtWidgets.QDialog()
        self.ui_warningNewVersion = guiwarningNewVersion.Ui_Dialog()
        self.ui_warningNewVersion.setupUi(self.Dialog_warningNewVersion)
        #Opening dialog
        res = self.Dialog_warningNewVersion.exec_()

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
        Dialog_lang = QtWidgets.QDialog()
        ui_lang = guilangchange.Ui_Dialog()
        ui_lang.setupUi(Dialog_lang)
        Dialog_lang.exec_()
    
    ########################### EVENT FILTERING ####################################
    def close_Event(self, e):
        """Will be executed when user tries to close the main window"""
        Dialog_quit = QtWidgets.QDialog()
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
        """Will be executed before the main window is shown"""
        if not self.first_time:
            return
        elif self.first_time == "partielator":
            self.warningNewVersion()
        else:
            self.wizard()


    def eventFilter(self, object, event):
        """filtering ctrl+C event on treeWidget/tableWidget"""
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
            elif event.matches(QtGui.QKeySequence.Delete):
                self.remove_exercises()
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
                    to_clipboard += item.enonce
                    to_clipboard += "\n"
                except:
                    to_clipboard += item.enonce
        QtWidgets.QApplication.clipboard().setText(to_clipboard)

    def copyToClipboardFromTable(self):
        """copy the source code of the selected exercises in the Table."""
        tuple_selected = [(self.tableWidget.row(item),item) for item in self.tableWidget.selectedItems()]
        tuple_selected = sorted(tuple_selected, key=lambda tup: tup[0]) #sort by position in the table
        to_clipboard = ""
        for tup in tuple_selected:
            try:
                to_clipboard += tup[1].enonce
                to_clipboard += "\n"
            except:
                to_clipboard += tup[1].enonce
        QtWidgets.QApplication.clipboard().setText(to_clipboard)

    ########################### LEAVING TEXAMATOR ######################################
    def nettoyage(self):
        try:
            for fichier in os.listdir("/tmp/texamator"):
                os.remove(os.path.join("/tmp/texamator",fichier))
            os.rmdir("/tmp/texamator")
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
        f = codecs.open(os.path.join(home_dir,".texamator","preferences.txt"),'w',"utf-8")
        for key, value in self.settings.items():
            f.write(key+"="+str(value)+"\n")
        f.close()

    ######################### CONTEXT MENU ON TREEWIDGET/LISTWIDGET #################
    def openMenuTree(self, position):
        """Context menu on the treeWidget"""
        selectedItems = self.treeWidget.selectedItems()
        if not selectedItems:
            return
        elif len(selectedItems)>1 or not self.treeWidget.currentItem().childCount() or not self.treeWidget.currentItem().child(0).childCount():
            menu = QtWidgets.QMenu()
            copyToClipboard = menu.addAction(_translate("Tree context menu", "Copy to clipboard"))
            copyToClipboard.setShortcut(QtGui.QKeySequence.Copy)
            copyToClipboard.triggered.connect(self.copyToClipboardFromTree)
            addToTable = menu.addAction(_translate("Tree context menu", "Add"))
            addToTable.triggered.connect(self.add_ex_to_table)
            editAction = menu.addAction(_translate("Tree context menu", "Edit..."))
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
            self.expand_collapse_me()


    def openMenuTable(self, position):
        """Context menu on the TableWidget"""
        n = len(self.tableWidget.selectedItems())
        if n>0:
            menu = QtWidgets.QMenu()
            copyToClipboard = menu.addAction(_translate("Table context menu", "Copy to clipboard"))
            copyToClipboard.setShortcut(QtGui.QKeySequence.Copy)
            copyToClipboard.triggered.connect(self.copyToClipboardFromTable)
            editAction = menu.addAction(_translate("Table context menu", "Edit..."))
            editAction.triggered.connect(self.editExerciceTableWidget)
            moveUp = menu.addAction(_translate("Table context menu", "Move up"))
            moveUp.triggered.connect(self.gouptable)
            moveDown = menu.addAction(_translate("Table context menu", "Move down"))
            moveDown.triggered.connect(self.godowntable)
            shuffle = menu.addAction(_translate("Table context menu", "Shuffle"))
            shuffle.triggered.connect(self.shuffleFromContext)
            remove = menu.addAction(_translate("Table context menu", "Remove"))
            remove.setShortcut(QtGui.QKeySequence.Delete)
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
            if self.settings['AMC']=='True':
                AMC = menu.addMenu(_translate("AMC-Menu", "Set element name (AMC)"))
                action = AMC.addAction(_translate("AMC-Menu", "New element..."))
                action.triggered.connect(self.newElement)
                def plop(i):
                    return lambda:self.setElementName(i)
                for i in self.listAMCGroups():
                    action = AMC.addAction(i)
                    action.triggered.connect(plop(i))
            menu.exec_(self.tableWidget.viewport().mapToGlobal(position)+QtCore.QPoint(3,0))

    def newElement(self):
        """Creates a new element name and set it to the tableWidget.selectedItems()"""
        Dialog_newelt = QtWidgets.QDialog()
        ui_newelt = guinewconf.Ui_Dialog()
        ui_newelt.setupUi(Dialog_newelt)
        ui_newelt.label.setText(_translate("AMC-Menu", "Enter the new element name"))
        Dialog_newelt.setWindowTitle(_translate("AMC-Menu", "New element"))
        res = Dialog_newelt.exec_()
        if res:
            element = ui_newelt.lineEdit.text()
            self.setElementName(element)
        

    def setElementName(self,i):
        """set the element name of an exercise to i"""
        rows = [self.tableWidget.row(item) for item in self.tableWidget.selectedItems()]
        for row in rows:
            itemElement = self.tableWidget.item(row,1)
            itemElement.setText(i)
            item = self.tableWidget.item(row,0)
            self.changeElement(item,i)
            
    def changeElement(self,item,newElement):
        """Edit an exercise and change the element name (AMC)"""
        oldElement = self.findAMCGroup(item.enonce)
        newEnonce = ''
        old = item.enonce.split('\n')
        for line in old:
            splitted = line.split('%')
            noComment = splitted[0]
            if r'\begin{'+self.settings['AMC-env']+'}' in noComment:
                noComment = noComment.replace(oldElement,newElement)
                if len(splitted)>1:
                    comment = ''.join(splitted[1:])
                else:
                    comment = ''
                newEnonce += noComment
                newEnonce += comment
            else:
                newEnonce += line
            newEnonce += '\n'
        item.enonce = newEnonce
                
                
    def listAMCGroups(self):
        """list AMC Groups from tableWidget"""
        a = []
        for i in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(i,1)
            if item and item.text() not in a:
                a.append(item.text())
        a.sort()
        return a

    ######################### CREATING THE PDF WIDGET ##################
    def initiatePdf(self):
        """Creates the pdf Area and loads the help.pdf file into it"""
        self.pdfScrollArea.setWidgetResizable(True)
        self.pdfScrollBar = self.pdfScrollArea.verticalScrollBar()
        w = int(self.settings["big_splitter_s2"])
        self.pdfWidgetContainer = QtWidgets.QWidget()
        self.pdfScrollArea.fun = self.repaintPdf
        self.pdfScrollArea.setWidget(self.pdfWidgetContainer)
        self.pdfWidgetContainer.setStyleSheet("background-color:white;")
        self.pdfwidget = PDFWidget(None,parent=self.pdfWidgetContainer, width=w-1)
        #Initiate horizontal scroll bar to be notified when pdfscrollArea is shrinked
        self.pdfScrollBarh = self.pdfScrollArea.horizontalScrollBar()

    
    def repaintPdf(self):
        #Recalculate size of the pdf and repaint
        w = self.big_splitter.sizes()[1]-self.pdfScrollBar.width()-4
        self.pdfwidget.repaint(w)
        
        
        
    ######################### COMPLETING MAIN WINDOW #################################
    def setupUi2(self,Form):
        """Adds what's missing to the main Window"""
        Ui_MainWindow.setupUi(self, Form)
        Form.closeEvent = self.close_Event
        Form.showEvent = self.show_Event
        self.actionCompile = {} #dictionnary containing the QAction in the Compile submenu
        self.populate_compile()
        self.actionPreamble = {}
        self.populate_preamble()
        #Context menus on treeWidget and tableWidget
        self.treeWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.treeWidget.customContextMenuRequested.connect(self.openMenuTree)
        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget.customContextMenuRequested.connect(self.openMenuTable)
        #AMC 
        self.AMC_texte = ''
        if self.settings['AMC']=='True':
            self.tableWidget.setColumnCount(2)
            self.tableWidget.setHorizontalHeaderLabels([_translate('Form','Exercise'),_translate('Form','Element (AMC)')])
        #lineEdit
        self.lineEdit.setText(self.settings["tex_path"])
        self.actionShuffle_list.triggered.connect(self.shuffle_list)
        self.actionGenerate_Random_Exam.triggered.connect(self.randomize)
        self.treeWidget.itemDoubleClicked.connect(self.add_ex_to_table_from_double_click)
        self.button_add.clicked.connect(self.add_ex_to_table)
        self.button_remove.clicked.connect(self.remove_exercises)
        self.button_up.clicked.connect(self.gouptable)
        self.button_down.clicked.connect(self.godowntable)
        self.button_refresh.clicked.connect(self.create_main_tree)
        self.treeWidget.itemClicked.connect(self.show_preview_tree)  
        self.tableWidget.itemSelectionChanged.connect(self.tableSelectionChanged)
        self.treeWidget.itemSelectionChanged.connect(self.treeSelectionChanged)
        self.tableWidget.itemDoubleClicked.connect(self.editExerciceTableWidget)
        self.tableWidget.itemChanged.connect(self.itemChangedTable)
        self.button_save.clicked.connect(self.export)
        self.button_recompile.clicked.connect(self.recompile)
        self.actionQuitter.triggered.connect(MainWindow.close)
        self.actionStart_Wizard.triggered.connect(self.wizard)
        self.actionPrefs.triggered.connect(self.prefs)
        self.actionExport.triggered.connect(self.export)
        self.actionA_propos.triggered.connect(self.apropos)
        self.actionEdit_exercise.triggered.connect(self.editExerciceTableWidget)
        self.actionFrench.triggered.connect(self.to_french)
        self.actionEnglish.triggered.connect(self.to_english)
        self.actionCzech.triggered.connect(self.to_czech)
        self.actionUkrainian.triggered.connect(self.to_ukrainian)
        self.actionGerman.triggered.connect(self.to_german)
        self.actionExpand_Collapse.triggered.connect(self.expand_collapse_me)
        self.pushButton_parcourir.clicked.connect(self.parcourir)
        self.pushButton_preview.clicked.connect(self.show_preview_list)
        self.lineEdit_search.textChanged[str].connect(self.search)
        #eventFilter to detect Ctrl+C and Del
        Form.eventFilter = self.eventFilter
        self.treeWidget.installEventFilter(Form)
        self.tableWidget.installEventFilter(Form)
        ##Splitter sizes :
        self.windowHeight = Form.height
        self.windowWidth = Form.width
        l = int(self.settings["width"])
        w = int(self.settings["height"])
        l1 = [int(self.settings["little_splitter_s1"]) , int(self.settings["little_splitter_s2"])]
        l2 = [int(self.settings["big_splitter_s1"]), int(self.settings["big_splitter_s2"])]
        Form.resize(l,w)
        self.big_splitter.setSizes(l2)
        self.little_splitter.setSizes(l1)
        #Table sizes
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setColumnWidth(0,.6*l1[1])
        self.initiatePdf()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    #Translate app ?
    settings = getSettings()
    x = settings[2]
    if x["lang"] != "en":
        p = os.path.abspath(sys.argv[0])
        while os.path.islink(p): #get rid of simlinks
            p = os.path.abspath(os.readlink(p))
        full_path = os.path.split(p)[0] #get the path where the program is
        t = QtCore.QTranslator()
        t.load(os.path.join(full_path, "ts_files/TeXamator_"+x["lang"]))
        QtCore.QCoreApplication.installTranslator(t)
    #chdir and create temp directory 
    try:
        os.mkdir("/tmp/texamator")
    except:
        print("couldn't create texamator dir or texamator dir already exists")
    os.chdir("/tmp/texamator")
    #Let's go !
    MainWindow = QtWidgets.QMainWindow()
    ui = MonApplication(settings)
    ui.setupUi2(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
