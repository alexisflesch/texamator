#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import os, codecs
import guinewconf, guidelete, guiwarning


def updateUi(self, MyHighlighter):
    """Updates self.ui_prefs"""
    #Set geometry
    self.ui_prefs.splitter.setSizes([int(self.settings["prefs splitter one"]), int(self.settings["prefs splitter two"])])
    w = self.settings["prefs width"]
    h = self.settings["prefs height"]
    self.Dialog_prefs.resize(int(w),int(h))
    for child in range(self.ui_prefs.splitter.count()):
        self.ui_prefs.splitter.setCollapsible(child,False)
    #To know whether okularlayout should be reloaded when user exits
    self.okularchange = False
    #Change font of textEdits
    self.ui_prefs.textEdit.setFont(self.myfont)
    self.ui_prefs.textEdit1.setFont(self.myfont)
    self.ui_prefs.textEdit_generate.setFont(self.myfont)
    self.ui_prefs.textEdit_generate_footer.setFont(self.myfont)
    #Set up highlighting
    self.highlighter1 = MyHighlighter(self.ui_prefs.textEdit)
    self.highlighter11 = MyHighlighter(self.ui_prefs.textEdit1)
    self.highlighter2 = MyHighlighter(self.ui_prefs.textEdit_generate)
    self.highlighter3 = MyHighlighter(self.ui_prefs.textEdit_generate_footer)
    #Fill everything
    self.ui_prefs.lineEdit_ex_folder.setText(self.settings["tex_path"])
    self.ui_prefs.lineEdit_save_folder.setText(self.settings["save_location"])
    self.ui_prefs.textEdit.setText(self.header)
    self.ui_prefs.textEdit1.setText(self.footer)
    #About the generate exam button :
    self.ui_prefs.lineEdit_dvi_viewer.setText(self.settings["file_viewer"])
    for k in range(self.ui_prefs.comboBox.count()):
        if self.ui_prefs.comboBox.itemText(k) == self.settings["type_of_file"]:
            self.ui_prefs.comboBox.setCurrentIndex(k)
            break
    #About the embedded viewer comboBox:
    for k in range(self.ui_prefs.comboBox_viewer.count()):
        if self.ui_prefs.comboBox_viewer.itemText(k) == self.settings["embedded viewer"]:
            self.ui_prefs.comboBox_viewer.setCurrentIndex(k)
            break
    #Add tags to the listWidget :
    for i in range(len(self.tags[0])):
        t1 = self.tags[0][i]
        t2 = self.tags[1][i]
        item = QtGui.QListWidgetItem(self.ui_prefs.listWidget)
        item.setText(t1+u" ... "+t2)
        item.t1 = t1
        item.t2 = t2
    #Make a copy of the settings
    self.new_generate = self.generate.copy()
    self.new_compile_seq = self.compile_seq.copy()
    #Add compile commands to the listWidget_comp
    for i in range(len(self.compile_seq[self.settings["preferred compile sequence"]])):
        item = QtGui.QListWidgetItem(self.ui_prefs.listWidget_comp)
        item.setText(self.compile_seq[self.settings["preferred compile sequence"]][i].replace("/tmp/partielator/file","!file"))
        #item.c = self.compile_seq[self.settings["preferred compile sequence"]][i].replace("/tmp/partielator/file","!file")
    self.last_compile = self.settings["preferred compile sequence"]   #config being displayed
    #Populate comboBox_compile
    for key in sorted(self.compile_seq):
        self.ui_prefs.comboBox_compile.addItem(key,key)
    #Set focus on preferred compile sequence
    num = self.ui_prefs.comboBox_compile.findText(self.settings["preferred compile sequence"])
    self.ui_prefs.comboBox_compile.setCurrentIndex(num)
    #Disable buttons if compile sequence is protected
    if self.settings["preferred compile sequence"] in ["Default (dvi no okular)","Alternative 1 (dvi + okular)","Alternative 2 (pdf + okular)"]:
        self.ui_prefs.pushButton_delete_compile_config.setEnabled(False)
        self.ui_prefs.pushButton_addc.setEnabled(False)
        self.ui_prefs.pushButton_removec.setEnabled(False)
        self.ui_prefs.pushButton_up.setEnabled(False)
        self.ui_prefs.pushButton_down.setEnabled(False)
    #Add elements to the generate comboBox and fills the textEdit_generate header and footer
    keys = self.new_generate.keys()
    keys.sort(key=str.lower)
    for key in keys:
        self.ui_prefs.comboBox_gen.addItem(key)     #add key to the combobox
    self.last_generate = keys[0]                    #config being displayed
    if self.last_generate == "Same header/footer":
        self.ui_prefs.pushButton_delete.setEnabled(False)
    text = QtCore.QString((self.new_generate[self.last_generate][0]))
    text1 = QtCore.QString((self.new_generate[self.last_generate][1]))
    self.ui_prefs.textEdit_generate.setText(text)
    self.ui_prefs.textEdit_generate_footer.setText(text1)
    self.combo(self.last_generate)
    #Is preview package used ?
    if self.settings["use_preview"] == "True":
        self.ui_prefs.radioButton_yes.setChecked(True)
        self.ui_prefs.radioButton_no.setChecked(False)
    else:
        self.ui_prefs.radioButton_no.setChecked(True)
        self.ui_prefs.radioButton_yes.setChecked(False)
    #Signals and slots
    QtCore.QObject.connect(self.ui_prefs.pushButton_parcourir_tex_path,QtCore.SIGNAL("clicked()"),self.parcourir_tex_path)
    QtCore.QObject.connect(self.ui_prefs.pushButton_parcourir_sav,QtCore.SIGNAL("clicked()"),self.parcourir_sav)
    QtCore.QObject.connect(self.ui_prefs.pushButton_remove,QtCore.SIGNAL("clicked()"),self.removetags)
    QtCore.QObject.connect(self.ui_prefs.pushButton_add,QtCore.SIGNAL("clicked()"),self.addtags)
    QtCore.QObject.connect(self.ui_prefs.pushButton_addc,QtCore.SIGNAL("clicked()"),self.addtocompileseq)
    QtCore.QObject.connect(self.ui_prefs.pushButton_removec,QtCore.SIGNAL("clicked()"),self.removefromcompileseq)
    QtCore.QObject.connect(self.ui_prefs.pushButton_up,QtCore.SIGNAL("clicked()"),self.goup2)
    QtCore.QObject.connect(self.ui_prefs.pushButton_down,QtCore.SIGNAL("clicked()"),self.godown2)
    QtCore.QObject.connect(self.ui_prefs.comboBox_gen,QtCore.SIGNAL("currentIndexChanged(QString)"),self.combo)
    QtCore.QObject.connect(self.ui_prefs.comboBox_compile,QtCore.SIGNAL("currentIndexChanged(QString)"),self.comboCompile)
    QtCore.QObject.connect(self.ui_prefs.comboBox_viewer,QtCore.SIGNAL("currentIndexChanged(QString)"),self.comboViewer)
    QtCore.QObject.connect(self.ui_prefs.textEdit1,QtCore.SIGNAL("textChanged()"),self.update_generate_footer)
    QtCore.QObject.connect(self.ui_prefs.textEdit,QtCore.SIGNAL("textChanged()"),self.update_generate_header)
    QtCore.QObject.connect(self.ui_prefs.pushButton_delete,QtCore.SIGNAL("clicked()"),self.prefs_delete)
    QtCore.QObject.connect(self.ui_prefs.pushButton_delete_compile_config,QtCore.SIGNAL("clicked()"),self.delete_compile_config)
    QtCore.QObject.connect(self.ui_prefs.pushButton_newconfig,QtCore.SIGNAL("clicked()"),self.add_generate_config)
    QtCore.QObject.connect(self.ui_prefs.pushButton_new_compile_config,QtCore.SIGNAL("clicked()"),self.add_compile_config)

def comboViewer(self,text):
    if text == "okular":
        try:
            from PyKDE4.kdecore import KUrl
            from PyKDE4.kdecore import ki18n, KAboutData, KCmdLineArgs
            from PyKDE4.kdecore import KLibLoader as ll
            from PyKDE4.kdeui import KApplication
            import PyKDE4.kparts as kp
            self.okupart = ll.self().factory('okularpart').create()
            self.okularchange = True
        except:
            Dialog_warning = QtGui.QDialog()
            self.ui_warning = guiwarning.Ui_Dialog()
            self.ui_warning.setupUi(Dialog_warning)
            res = Dialog_warning.exec_()
            self.ui_prefs.comboBox_viewer.setCurrentIndex(0)
    else:
        self.okularchange = True       

def close_prefs(self, res):
    """When the prefs window is closed"""
    if res:
        #If user cliked ok, change settings and write it in the config file
        #Basic settings
        self.settings["prefs width"] = str(self.Dialog_prefs.width())
        self.settings["prefs height"] = str(self.Dialog_prefs.height())
        self.settings["prefs splitter one"], self.settings["prefs splitter two"] = self.ui_prefs.splitter.sizes()
        self.settings["tex_path"] = unicode(self.ui_prefs.lineEdit_ex_folder.text())
        self.settings["save_location"] = unicode(self.ui_prefs.lineEdit_save_folder.text())
        self.settings["file_viewer"] = unicode(self.ui_prefs.lineEdit_dvi_viewer.text())
        self.settings["type_of_file"] = unicode(self.ui_prefs.comboBox.currentText())
        self.header = unicode(self.ui_prefs.textEdit.toPlainText())
        self.footer = unicode(self.ui_prefs.textEdit1.toPlainText())
        self.settings["embedded viewer"] = unicode(self.ui_prefs.comboBox_viewer.currentText())
        if self.ui_prefs.radioButton_yes.isChecked():
            self.settings["use_preview"] = "True"
        else:
            self.settings["use_preview"] = "False"
        home_dir = os.path.expanduser("~")
        f = codecs.open(os.path.join(home_dir, ".partielator", "basics"), 'w', "utf-8")
        for key, value in self.settings.iteritems():
            f.write(key + "=" + str(value) + "\n")
        f.close()
        #Change okular layout if needed
        if self.okularchange and self.settings["embedded viewer"] == "okular":
            self.okularlayout.setWidget(self.okupart.widget())
            self.okupart.slotHideFindBar()
        elif self.okularchange and self.settings["embedded viewer"] == "embedded (with dvipng)":
            self.okularlayout.setBackgroundRole(QtGui.QPalette.Light)
            self.preview = QtGui.QLabel()
            self.okularlayout.setWidget(self.preview)
            self.verticalScrollBar = self.okularlayout.verticalScrollBar() 
        #Header
        g = codecs.open(os.path.join(home_dir, ".partielator", "header"), 'w', "utf-8")
        g.write(unicode(self.ui_prefs.textEdit.toPlainText()))
        g.close()
        self.header = unicode(self.ui_prefs.textEdit.toPlainText())
        #tex path
        self.lineEdit.setText(self.settings["tex_path"])
        #Footer
        g = codecs.open(os.path.join(home_dir, ".partielator", "footer"), 'w', "utf-8")
        g.write(unicode(self.ui_prefs.textEdit1.toPlainText()))
        g.close()
        self.footer = unicode(self.ui_prefs.textEdit1.toPlainText())
        #Tags
        h = codecs.open(os.path.join(home_dir, ".partielator", "tags"), 'w', "utf-8")
        self.tags = [[], []]
        for i in range(self.ui_prefs.listWidget.count()):
            t1 = self.ui_prefs.listWidget.item(i).t1
            t2 = self.ui_prefs.listWidget.item(i).t2
            self.tags[0].append(t1)
            self.tags[1].append(t2)
            h.write(t1 + "!!!" + t2 + "\n")
        h.close()
        #Compile sequence
        self.compile_seq = self.new_compile_seq #save changes
        self.settings["preferred compile sequence"] = unicode(self.ui_prefs.comboBox_compile.currentText())
        self.populate_compile() #update compile submenu
        f = codecs.open(os.path.join(home_dir,".partielator","compile_seq2"),'w','utf-8')
        for key in self.compile_seq.keys():
            f.write("###" + key + "###\n")
            for item in self.compile_seq[key]:
                f.write(item+'\n')
        f.close()
        #Generate
        #Save pending changes
        self.new_generate[self.last_generate][0] = unicode(self.ui_prefs.textEdit_generate.toPlainText())
        self.new_generate[self.last_generate][1] = unicode(self.ui_prefs.textEdit_generate_footer.toPlainText())
        #Keep the new generate dictionnary as user clicked "ok"
        self.generate = self.new_generate
        for key in self.generate.keys():
            if key == "Same header/footer":
                continue
            f = codecs.open(os.path.join(home_dir, ".partielator", "generate", key), 'w', 'utf-8')
            g = codecs.open(os.path.join(home_dir, ".partielator", "generate", key+".end"), 'w', 'utf-8')
            f.write(self.generate[key][0])
            g.write(self.generate[key][1])
            f.close()
            g.close()

def add_compile_config(self):
    """Add a new compile config"""
    Dialog_newconf = QtGui.QDialog()
    self.ui_newconf = guinewconf.Ui_Dialog()
    self.ui_newconf.setupUi(Dialog_newconf)
    res = Dialog_newconf.exec_()
    newkey = str(self.ui_newconf.lineEdit.text())
    if res and newkey and not newkey in self.new_generate.keys():
        self.new_compile_seq[newkey] = []
        length = self.ui_prefs.comboBox_compile.count()
        for k in range(length):#insert alphabetically newkey
            if newkey.lower() < str(self.ui_prefs.comboBox_compile.itemText(k)).lower():
                self.ui_prefs.comboBox_compile.setCurrentIndex(0)#if not present insertItem sends a bad signal
                self.ui_prefs.comboBox_compile.insertItem(k,newkey)
                self.ui_prefs.comboBox_compile.setCurrentIndex(k)
                break
        if k == length-1:
            self.ui_prefs.comboBox_compile.setCurrentIndex(0)#if not present insertItem sends a bad signal
            self.ui_prefs.comboBox_compile.insertItem(k,newkey)
            self.ui_prefs.comboBox_compile.setCurrentIndex(k)
        #Enable buttons
        self.ui_prefs.pushButton_delete_compile_config.setEnabled(True)
        self.ui_prefs.pushButton_addc.setEnabled(True)
        self.ui_prefs.pushButton_removec.setEnabled(True)
        self.ui_prefs.pushButton_up.setEnabled(True)
        self.ui_prefs.pushButton_down.setEnabled(True)
        #Update last compile seq in case it has been modified
        self.new_compile_seq[self.last_compile] = []
        for i in range(self.ui_prefs.listWidget_comp.count()):
            c = self.ui_prefs.listWidget_comp.item(i).text()
            self.new_compile_seq[self.last_compile].append(c)
        #Clear list
        self.ui_prefs.listWidget_comp.clear()        
        self.last_compile = newkey

def comboCompile(self,text):
    """Dealing with compile configs"""
    comp = str(text)
    #Disable buttons if compile sequence is protected
    if comp in ["Default (dvi no okular)","Alternative 1 (dvi + okular)","Alternative 2 (pdf + okular)"]:
        self.ui_prefs.pushButton_delete_compile_config.setEnabled(False)
        self.ui_prefs.pushButton_addc.setEnabled(False)
        self.ui_prefs.pushButton_removec.setEnabled(False)
        self.ui_prefs.pushButton_up.setEnabled(False)
        self.ui_prefs.pushButton_down.setEnabled(False)
    else:
        self.ui_prefs.pushButton_delete_compile_config.setEnabled(True)
        self.ui_prefs.pushButton_addc.setEnabled(True)
        self.ui_prefs.pushButton_removec.setEnabled(True)
        self.ui_prefs.pushButton_up.setEnabled(True)
        self.ui_prefs.pushButton_down.setEnabled(True)
    #Update config displayed before the change of config
    self.new_compile_seq[self.last_compile] = []
    for i in range(self.ui_prefs.listWidget_comp.count()):
        c = self.ui_prefs.listWidget_comp.item(i).text()
        self.new_compile_seq[self.last_compile].append(c)
    #Clear list and write corresponding compile sequence
    self.ui_prefs.listWidget_comp.clear()
    for i in range(len(self.new_compile_seq[comp])):
        item = QtGui.QListWidgetItem(self.ui_prefs.listWidget_comp)
        item.setText(self.new_compile_seq[comp][i].replace("/tmp/partielator/file","!file"))
    self.last_compile = comp

def delete_compile_config(self):
    """Opens a dialog to ensure user wants to delete the selected compile config"""
    Dialog_delete = QtGui.QDialog()
    self.ui_delete = guidelete.Ui_Dialog()
    self.ui_delete.setupUi(Dialog_delete)
    i = self.ui_prefs.comboBox_compile.currentIndex()
    text = str(self.ui_prefs.comboBox_compile.currentText())
    self.ui_delete.label.setText(QtGui.QApplication.translate("Form", "You are about to delete the compile sequence : ",\
                                 None, QtGui.QApplication.UnicodeUTF8) + text)
    res = Dialog_delete.exec_()
    if res:
        self.ui_prefs.comboBox_compile.removeItem(i)
        del self.new_compile_seq[text]

def add_generate_config(self):
    """Add a new generate config"""
    Dialog_newconf = QtGui.QDialog()
    self.ui_newconf = guinewconf.Ui_Dialog()
    self.ui_newconf.setupUi(Dialog_newconf)
    res = Dialog_newconf.exec_()
    newkey = str(self.ui_newconf.lineEdit.text())
    if res and newkey and not newkey in self.new_generate.keys():
        self.new_generate[newkey] = ["",""]
        self.new_generate[newkey][0] = "\\documentclass{article}\n\n\\begin{document}\n\n\n\n\n%Your exercises will be written after these lines"
        self.new_generate[newkey][1] = "\n\n%Your exercises will appear before these lines\n\\end{document}"
        length = self.ui_prefs.comboBox_gen.count()
        for k in range(length):#insert alphabetically newkey
            if newkey.lower() < str(self.ui_prefs.comboBox_gen.itemText(k)).lower():
                self.ui_prefs.comboBox_gen.setCurrentIndex(0)#if not present insertItem sends a bad signal
                self.ui_prefs.comboBox_gen.insertItem(k,newkey)
                self.ui_prefs.comboBox_gen.setCurrentIndex(k)
                break
        if k == length-1:
            self.ui_prefs.comboBox_gen.setCurrentIndex(0)#if not present insertItem sends a bad signal
            self.ui_prefs.comboBox_gen.insertItem(k,newkey)
            self.ui_prefs.comboBox_gen.setCurrentIndex(k)
        self.last_generate = newkey
        self.ui_prefs.pushButton_delete.setEnabled(True)

def combo(self, text):
    """Dealing with generate configs"""
    #Before doing anything, update the config that may (or may not) have changed
    self.new_generate[self.last_generate][0] = unicode(self.ui_prefs.textEdit_generate.toPlainText())
    self.new_generate[self.last_generate][1] = unicode(self.ui_prefs.textEdit_generate_footer.toPlainText())
    a = str(text)
    if text == "Same header/footer":
        self.ui_prefs.textEdit_generate.setReadOnly(True)
        self.ui_prefs.textEdit_generate.setText(self.new_generate[a][0])
        self.ui_prefs.textEdit_generate_footer.setReadOnly(True)
        self.ui_prefs.textEdit_generate_footer.setText(self.new_generate[a][1])
        self.last_generate = a
        self.ui_prefs.pushButton_delete.setEnabled(False)
    else:
        self.ui_prefs.textEdit_generate.setReadOnly(False)
        self.ui_prefs.textEdit_generate.setText(self.new_generate[a][0])
        self.ui_prefs.textEdit_generate_footer.setReadOnly(False)
        self.ui_prefs.textEdit_generate_footer.setText(self.new_generate[a][1])
        self.last_generate = a
        self.ui_prefs.pushButton_delete.setEnabled(True)


def update_generate_header(self):
    self.new_generate["Same header/footer"][0] = unicode(self.ui_prefs.textEdit.toPlainText())
    if self.last_generate == "Same header/footer":
        self.ui_prefs.textEdit_generate.setText(self.new_generate["Same header/footer"][0])

def update_generate_footer(self):
    self.new_generate["Same header/footer"][1] = unicode(self.ui_prefs.textEdit1.toPlainText())
    if self.last_generate == "Same header/footer":
        self.ui_prefs.textEdit_generate_footer.setText(self.new_generate["Same header/footer"][1])


def parcourir_tex_path(self):
    dirName = QtGui.QFileDialog.getExistingDirectory(self.Dialog_prefs,\
                 QtGui.QApplication.translate("Form", "Pick a folder",\
                 None, QtGui.QApplication.UnicodeUTF8),\
                 self.settings["tex_path"])
    if dirName:
        self.ui_prefs.lineEdit_ex_folder.setText(dirName)

def parcourir_sav(self):
    dirName = QtGui.QFileDialog.getExistingDirectory(self.Dialog_prefs,\
                QtGui.QApplication.translate("Form", "Pick a folder",\
                None, QtGui.QApplication.UnicodeUTF8),\
                self.settings["save_location"])
    if dirName:
        self.ui_prefs.lineEdit_save_folder.setText(dirName)

def removetags(self):
    self.ui_prefs.listWidget.takeItem(self.ui_prefs.listWidget.currentRow())

def addtags(self):
    if unicode(self.ui_prefs.lineEdit_tag1.text()) and unicode(self.ui_prefs.lineEdit_tag2.text()):
        item = QtGui.QListWidgetItem(self.ui_prefs.listWidget)
        item.t1 = unicode(self.ui_prefs.lineEdit_tag1.text())
        item.t2 = unicode(self.ui_prefs.lineEdit_tag2.text())
        item.setText(item.t1 + u" ... " + item.t2)

def addtocompileseq(self):
    if unicode(self.ui_prefs.lineEdit_command.text()):
        item = QtGui.QListWidgetItem(self.ui_prefs.listWidget_comp)
        item.setText(unicode(self.ui_prefs.lineEdit_command.text()))

def prefs_delete(self):
    Dialog_delete = QtGui.QDialog()
    self.ui_delete = guidelete.Ui_Dialog()
    self.ui_delete.setupUi(Dialog_delete)
    i = self.ui_prefs.comboBox_gen.currentIndex()
    text = str(self.ui_prefs.comboBox_gen.currentText())
    self.ui_delete.label.setText(QtGui.QApplication.translate("Form", "You are about to delete the config : ",\
                                 None, QtGui.QApplication.UnicodeUTF8) + text)
    res = Dialog_delete.exec_()
    if res:
        self.ui_prefs.comboBox_gen.removeItem(i)
        del self.new_generate[text]
        home_dir = os.path.expanduser("~")
        os.remove(os.path.join(home_dir,".partielator","generate",text))
        os.remove(os.path.join(home_dir,".partielator","generate",text+".end"))
