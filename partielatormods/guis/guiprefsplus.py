#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import os
import codecs
from . import guinewconf, guidelete, guiwarning

_translate = QtCore.QCoreApplication.translate


def updateUi(self, MyHighlighter):
    """Updates self.ui_prefs"""
    # Set geometry
    self.ui_prefs.splitter.setSizes([int(self.settings["prefs splitter one"]), int(
        self.settings["prefs splitter two"])])
    w = self.settings["prefs width"]
    h = self.settings["prefs height"]
    self.Dialog_prefs.resize(int(w), int(h))
    for child in range(self.ui_prefs.splitter.count()):
        self.ui_prefs.splitter.setCollapsible(child, False)
    # Change font of textEdits
    self.ui_prefs.textEdit_generate.setFont(self.myfont)
    self.ui_prefs.textEdit_generate_footer.setFont(self.myfont)
    # Set up highlighting
    self.highlighter2 = MyHighlighter(self.ui_prefs.textEdit_generate)
    self.highlighter3 = MyHighlighter(self.ui_prefs.textEdit_generate_footer)
    # Fill everything
    self.ui_prefs.lineEdit_ex_folder.setText(self.settings["tex_path"])
    self.ui_prefs.lineEdit_save_folder.setText(self.settings["save_location"])
    self.ui_prefs.lineEdit_dvi_viewer.setText(self.settings["file_viewer"])
    # Add tags to the listWidget :
    for i in range(len(self.tags[0])):
        t1 = self.tags[0][i]
        t2 = self.tags[1][i]
        item = QtWidgets.QListWidgetItem(self.ui_prefs.listWidget)
        item.setText(t1+" ... "+t2)
        item.t1 = t1
        item.t2 = t2
    # Make a copy of the settings
    self.new_preamblesPostambles = self.preamblesPostambles.copy()
    self.new_compile_seq = self.compile_seq.copy()
    # Select current compile sequence and update compile tab
    # config being displayed
    self.last_compile = self.settings["preferred compile sequence"]
    updateCompileTab(self, self.compile_seq[self.last_compile])
    # Populate comboBox_compile
    for key in sorted(self.compile_seq):
        self.ui_prefs.comboBox_compile.addItem(key, key)
    # Set focus on preferred compile sequence
    num = self.ui_prefs.comboBox_compile.findText(
        self.settings["preferred compile sequence"])
    self.ui_prefs.comboBox_compile.setCurrentIndex(num)
    # Disable buttons if compile sequence is protected
    if self.settings["preferred compile sequence"] in ["Alternative (latex/dvips/ps2pdf)", "Default (pdflatex)"]:
        enableCompileEdition(self, enable=False)
    # Add elements to the generate comboBox and fills the textEdit_generate header and footer
    #keys = self.new_preamblesPostambles.keys()
    # keys.sort(key=str.lower)
    keys = []
    for key in sorted(self.new_preamblesPostambles):
        keys.append(key)
        self.ui_prefs.comboBox_gen.addItem(key)  # add key to the combobox
    self.last_generate = keys[0]  # config being displayed
    text = self.new_preamblesPostambles[self.last_generate][0]
    text1 = self.new_preamblesPostambles[self.last_generate][1]
    self.ui_prefs.textEdit_generate.setText(text)
    self.ui_prefs.textEdit_generate_footer.setText(text1)
    self.combo(self.last_generate)
    # AMC
    if self.settings['AMC'] == 'True':
        self.ui_prefs.radioButtonAMCYes.setChecked(True)
        self.ui_prefs.radioButtonAMCNo.setChecked(False)
    else:
        self.ui_prefs.radioButtonAMCYes.setChecked(False)
        self.ui_prefs.radioButtonAMCNo.setChecked(True)
    self.ui_prefs.lineEditAMCEnv.setText(self.settings['AMC-env'])
    self.ui_prefs.lineEditAMCText.setText(self.settings['AMC-text'])
    #Signals and slots
    self.ui_prefs.pushButton_parcourir_tex_path.clicked.connect(
        self.parcourir_tex_path)
    self.ui_prefs.pushButton_parcourir_sav.clicked.connect(self.parcourir_sav)
    self.ui_prefs.pushButton_remove.clicked.connect(self.removetags)
    self.ui_prefs.pushButton_add.clicked.connect(self.addtags)
    self.ui_prefs.pushButton_addc.clicked.connect(self.addtocompileseq)
    self.ui_prefs.pushButton_removec.clicked.connect(self.removefromcompileseq)
    self.ui_prefs.pushButton_up.clicked.connect(self.goup2)
    self.ui_prefs.pushButton_down.clicked.connect(self.godown2)
    self.ui_prefs.comboBox_compile.currentIndexChanged[str].connect(
        self.comboCompile)
    self.ui_prefs.comboBox_gen.currentIndexChanged[str].connect(self.combo)
    self.ui_prefs.pushButton_delete.clicked.connect(self.prefs_delete)
    self.ui_prefs.pushButton_delete_compile_config.clicked.connect(
        self.delete_compile_config)
    self.ui_prefs.pushButton_newconfig.clicked.connect(
        self.add_generate_config)
    self.ui_prefs.pushButton_new_compile_config.clicked.connect(
        self.add_compile_config)


def enableCompileEdition(self, enable=True):
    """to enable (or disable) buttons corresponding to the compile tab
       (to protect default configs)
    """
    self.ui_prefs.pushButton_delete_compile_config.setEnabled(enable)
    self.ui_prefs.pushButton_addc.setEnabled(enable)
    self.ui_prefs.pushButton_removec.setEnabled(enable)
    self.ui_prefs.pushButton_up.setEnabled(enable)
    self.ui_prefs.pushButton_down.setEnabled(enable)


def updateCompileTab(self, compile_seq):
    # Clear list
    self.ui_prefs.listWidget_comp.clear()
    # Add compile commands to the listWidget_comp
    for i in range(len(compile_seq)):
        item = QtWidgets.QListWidgetItem(self.ui_prefs.listWidget_comp)
        item.setText(compile_seq[i])


def close_prefs(self, res):
    """When the prefs window is closed"""
    if res:
        # If user cliked ok, change settings and write it in the config file
        # Basic settings
        self.settings["prefs width"] = str(self.Dialog_prefs.width())
        self.settings["prefs height"] = str(self.Dialog_prefs.height())
        self.settings["prefs splitter one"], self.settings["prefs splitter two"] = self.ui_prefs.splitter.sizes()
        self.settings["tex_path"] = str(
            self.ui_prefs.lineEdit_ex_folder.text())
        self.settings["save_location"] = str(
            self.ui_prefs.lineEdit_save_folder.text())
        self.settings["file_viewer"] = str(
            self.ui_prefs.lineEdit_dvi_viewer.text())
        l1 = self.little_splitter.sizes()[1]
        if self.ui_prefs.radioButtonAMCYes.isChecked():
            self.settings['AMC'] = 'True'
            self.tableWidget.setColumnCount(2)
            self.tableWidget.setHorizontalHeaderLabels(
                ['Exercise', 'Element (AMC)'])
            self.tableWidget.setColumnWidth(0, int(.6*l1))
            self.tableWidget.horizontalHeader().setStretchLastSection(True)
        else:
            self.settings['AMC'] = 'False'
            self.tableWidget.setColumnCount(1)
            self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.settings['AMC-env'] = self.ui_prefs.lineEditAMCEnv.text()
        self.settings['AMC-text'] = self.ui_prefs.lineEditAMCText.text()
        home_dir = os.path.expanduser("~")
        f = codecs.open(os.path.join(home_dir, ".texamator",
                                     "preferences.txt"), 'w', "utf-8")
        for key, value in self.settings.items():
            f.write(key + "=" + str(value) + "\n")
        f.close()
        # tex path
        self.lineEdit.setText(self.settings["tex_path"])
        # Tags
        h = codecs.open(os.path.join(
            home_dir, ".texamator", "tags.txt"), 'w', "utf-8")
        self.tags = [[], []]
        for i in range(self.ui_prefs.listWidget.count()):
            t1 = self.ui_prefs.listWidget.item(i).t1
            t2 = self.ui_prefs.listWidget.item(i).t2
            self.tags[0].append(t1)
            self.tags[1].append(t2)
            h.write(t1 + "!!!" + t2 + "\n")
        h.close()
        # Compile sequence
        # Update config displayed before the change of config
        self.new_compile_seq[self.last_compile] = []
        for i in range(self.ui_prefs.listWidget_comp.count()):
            c = self.ui_prefs.listWidget_comp.item(i).text()
            self.new_compile_seq[self.last_compile].append(c)
        # Save compile sequences
        self.compile_seq = self.new_compile_seq  # save changes
        self.settings["preferred compile sequence"] = self.ui_prefs.comboBox_compile.currentText()
        self.populate_compile()  # update compile submenu
        for key in list(self.compile_seq.keys()):
            if key in ["Alternative (latex/dvips/ps2pdf)", "Default (pdflatex)"]:
                continue
            foo = os.path.join(home_dir, ".texamator",
                               "compile.sequences", key)
            f = codecs.open(foo, 'w', 'utf-8')
            for item in self.compile_seq[key]:
                f.write(item+'\n')
        f.close()
        # Generate
        # Save pending changes
        self.new_preamblesPostambles[self.last_generate][0] = self.ui_prefs.textEdit_generate.toPlainText(
        )
        self.new_preamblesPostambles[self.last_generate][1] = self.ui_prefs.textEdit_generate_footer.toPlainText(
        )
        # Keep the new generate dictionnary as user clicked "ok"
        self.preamblesPostambles = self.new_preamblesPostambles
        for key in list(self.preamblesPostambles.keys()):
            f = codecs.open(os.path.join(
                home_dir, ".texamator", "preambles.and.postambles", key+".preamble.tex"), 'w', 'utf-8')
            g = codecs.open(os.path.join(
                home_dir, ".texamator", "preambles.and.postambles", key+".postamble.tex"), 'w', 'utf-8')
            f.write(self.preamblesPostambles[key][0])
            g.write(self.preamblesPostambles[key][1])
            f.close()
            g.close()


def add_compile_config(self):
    """Add a new compile config"""
    Dialog_newconf = QtWidgets.QDialog()
    self.ui_newconf = guinewconf.Ui_Dialog()
    self.ui_newconf.setupUi(Dialog_newconf)
    res = Dialog_newconf.exec_()
    newkey = str(self.ui_newconf.lineEdit.text())
    if res and newkey and not newkey in list(self.new_preamblesPostambles.keys()):
        self.new_compile_seq[newkey] = []
        length = self.ui_prefs.comboBox_compile.count()
        for k in range(length):  # insert alphabetically newkey
            if newkey.lower() < str(self.ui_prefs.comboBox_compile.itemText(k)).lower():
                # if not present insertItem sends a bad signal
                self.ui_prefs.comboBox_compile.setCurrentIndex(0)
                self.ui_prefs.comboBox_compile.insertItem(k, newkey)
                self.ui_prefs.comboBox_compile.setCurrentIndex(k)
                break
        if k == length-1:
            # if not present insertItem sends a bad signal
            self.ui_prefs.comboBox_compile.setCurrentIndex(0)
            self.ui_prefs.comboBox_compile.insertItem(k, newkey)
            self.ui_prefs.comboBox_compile.setCurrentIndex(k)
        # Enable buttons
        enableCompileEdition(self)
        # Update last compile seq in case it has been modified
        self.new_compile_seq[self.last_compile] = []
        for i in range(self.ui_prefs.listWidget_comp.count()):
            c = self.ui_prefs.listWidget_comp.item(i).text()
            self.new_compile_seq[self.last_compile].append(c)
        # Clear list
        self.ui_prefs.listWidget_comp.clear()
        self.last_compile = newkey


def comboCompile(self, comp):
    """Function called when the compilation config has been changed
       from the comboBox
    """
    # Disable buttons if compile sequence is protected
    if comp in ["Alternative (latex/dvips/ps2pdf)", "Default (pdflatex)"]:
        enableCompileEdition(self, enable=False)
    else:
        enableCompileEdition(self)
    # Update config displayed before the change of config
    self.new_compile_seq[self.last_compile] = []
    for i in range(self.ui_prefs.listWidget_comp.count()):
        c = self.ui_prefs.listWidget_comp.item(i).text()
        self.new_compile_seq[self.last_compile].append(c)
    # update the tab
    updateCompileTab(self, self.new_compile_seq[comp])
    self.last_compile = comp


def delete_compile_config(self):
    """Opens a dialog to ensure user wants to delete the selected compile config"""
    Dialog_delete = QtWidgets.QDialog()
    self.ui_delete = guidelete.Ui_Dialog()
    self.ui_delete.setupUi(Dialog_delete)
    i = self.ui_prefs.comboBox_compile.currentIndex()
    text = str(self.ui_prefs.comboBox_compile.currentText())
    self.ui_delete.label.setText(_translate(
        "Form", "You are about to delete the compile sequence : ") + text)
    res = Dialog_delete.exec_()
    if res:
        self.ui_prefs.comboBox_compile.removeItem(i)
        del self.new_compile_seq[text]


def add_generate_config(self):
    """Add a new generate config"""
    Dialog_newconf = QtWidgets.QDialog()
    self.ui_newconf = guinewconf.Ui_Dialog()
    self.ui_newconf.setupUi(Dialog_newconf)
    res = Dialog_newconf.exec_()
    newkey = str(self.ui_newconf.lineEdit.text())
    if res and newkey and not newkey in list(self.new_preamblesPostambles.keys()):
        self.new_preamblesPostambles[newkey] = ["", ""]
        self.new_preamblesPostambles[newkey][
            0] = "\\documentclass{article}\n\n\\begin{document}\n\n\n\n\n%Your exercises will be written after these lines"
        self.new_preamblesPostambles[newkey][
            1] = "\n\n%Your exercises will appear before these lines\n\\end{document}"
        length = self.ui_prefs.comboBox_gen.count()
        for k in range(length):  # insert alphabetically newkey
            if newkey.lower() < str(self.ui_prefs.comboBox_gen.itemText(k)).lower():
                # if not present insertItem sends a bad signal
                self.ui_prefs.comboBox_gen.setCurrentIndex(0)
                self.ui_prefs.comboBox_gen.insertItem(k, newkey)
                self.ui_prefs.comboBox_gen.setCurrentIndex(k)
                break
        if k == length-1:
            # if not present insertItem sends a bad signal
            self.ui_prefs.comboBox_gen.setCurrentIndex(0)
            self.ui_prefs.comboBox_gen.insertItem(k, newkey)
            self.ui_prefs.comboBox_gen.setCurrentIndex(k)
        self.last_generate = newkey
        self.ui_prefs.pushButton_delete.setEnabled(True)


def combo(self, text):
    """Dealing with generate configs"""
    # Before doing anything, update the config that may (or may not) have changed
    self.new_preamblesPostambles[self.last_generate][0] = str(
        self.ui_prefs.textEdit_generate.toPlainText())
    self.new_preamblesPostambles[self.last_generate][1] = str(
        self.ui_prefs.textEdit_generate_footer.toPlainText())
    a = str(text)
    self.ui_prefs.textEdit_generate.setText(self.new_preamblesPostambles[a][0])
    self.ui_prefs.textEdit_generate_footer.setText(
        self.new_preamblesPostambles[a][1])
    self.last_generate = a
    self.ui_prefs.pushButton_delete.setEnabled(True)


def parcourir_tex_path(self):
    dirName = QtWidgets.QFileDialog.getExistingDirectory(
        self.Dialog_prefs, _translate("Form", "Pick a folder"), self.settings["tex_path"])
    if dirName:
        self.ui_prefs.lineEdit_ex_folder.setText(dirName)


def parcourir_sav(self):
    dirName = QtWidgets.QFileDialog.getExistingDirectory(self.Dialog_prefs, _translate(
        "Form", "Pick a folder"), self.settings["save_location"])
    if dirName:
        self.ui_prefs.lineEdit_save_folder.setText(dirName)


def removetags(self):
    self.ui_prefs.listWidget.takeItem(self.ui_prefs.listWidget.currentRow())


def addtags(self):
    if str(self.ui_prefs.lineEdit_tag1.text()) and str(self.ui_prefs.lineEdit_tag2.text()):
        item = QtWidgets.QListWidgetItem(self.ui_prefs.listWidget)
        item.t1 = str(self.ui_prefs.lineEdit_tag1.text())
        item.t2 = str(self.ui_prefs.lineEdit_tag2.text())
        item.setText(item.t1 + " ... " + item.t2)


def addtocompileseq(self):
    if str(self.ui_prefs.lineEdit_command.text()):
        item = QtWidgets.QListWidgetItem(self.ui_prefs.listWidget_comp)
        item.setText(str(self.ui_prefs.lineEdit_command.text()))


def prefs_delete(self):
    Dialog_delete = QtWidgets.QDialog()
    self.ui_delete = guidelete.Ui_Dialog()
    self.ui_delete.setupUi(Dialog_delete)
    i = self.ui_prefs.comboBox_gen.currentIndex()
    text = str(self.ui_prefs.comboBox_gen.currentText())
    self.ui_delete.label.setText(_translate(
        "Form", "You are about to delete the config : ") + text)
    res = Dialog_delete.exec_()
    if res:
        self.ui_prefs.comboBox_gen.removeItem(i)
        del self.new_preamblesPostambles[text]
        home_dir = os.path.expanduser("~")
        os.remove(os.path.join(home_dir, ".texamator",
                               "preambles.and.postambles", text+".preamble.tex"))
        os.remove(os.path.join(home_dir, ".texamator",
                               "preambles.and.postambles", text+".postamble.tex"))
