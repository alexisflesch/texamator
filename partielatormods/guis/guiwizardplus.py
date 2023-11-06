#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import os
import codecs

_translate = QtCore.QCoreApplication.translate


def updateUi(self, MyHighlighter, Dialog_wizard):
    # Change font of textEdit
    self.ui_wizard.textEdit.setFont(self.myfont)
    # Set up highlighting
    self.highlighter4 = MyHighlighter(self.ui_wizard.textEdit)
    # Current frame
    self.ui_wizard.frame2.hide()
    self.ui_wizard.frame3.hide()
    self.ui_wizard.whatframe = 1
    # Is it the first time TeXamator is launched ?
    if self.first_time:
        self.ui_wizard.label_warning.setText(_translate(
            "Wizard", "It looks like it is the first time you use TeXamator on this computer !"))
    # Shape
    Dialog_wizard.resize(800, 600)
    # Slots and signals
    self.ui_wizard.pushButton_next.clicked.connect(self.wizard_next)
    self.ui_wizard.pushButton_back.clicked.connect(self.wizard_back)
    self.ui_wizard.pushButton_browse.clicked.connect(self.wizard_browse)
    self.ui_wizard.pushButton_remove.clicked.connect(self.wizard_removetags)
    self.ui_wizard.pushButton_add.clicked.connect(self.wizard_addtags)
    self.ui_wizard.lineEdit.textChanged[str].connect(self.wizard_allow_next)


def wizard_allow_next(self):
    if self.ui_wizard.lineEdit.text():
        self.ui_wizard.pushButton_next.setEnabled(True)
    else:
        self.ui_wizard.pushButton_next.setEnabled(False)


def wizard_next(self):
    if self.ui_wizard.whatframe == 1:
        self.ui_wizard.frame1.hide()
        self.ui_wizard.frame2.show()
        self.ui_wizard.pushButton_back.setEnabled(True)
        self.ui_wizard.whatframe = 2
        self.wizard_guess()
    elif self.ui_wizard.whatframe == 2:
        self.ui_wizard.frame2.hide()
        self.ui_wizard.frame3.show()
        self.ui_wizard.pushButton_next.setEnabled(False)
        self.ui_wizard.pushButton_apply.setEnabled(True)
        self.ui_wizard.whatframe = 3


def wizard_back(self):
    if self.ui_wizard.whatframe == 2:
        self.ui_wizard.frame2.hide()
        self.ui_wizard.frame1.show()
        self.ui_wizard.pushButton_back.setEnabled(False)
        self.ui_wizard.whatframe = 1
    elif self.ui_wizard.whatframe == 3:
        self.ui_wizard.frame3.hide()
        self.ui_wizard.frame2.show()
        self.ui_wizard.pushButton_next.setEnabled(True)
        self.ui_wizard.pushButton_apply.setEnabled(False)
        self.ui_wizard.whatframe = 2


def wizard_browse(self, Dialog_wizard):
    fileName, _ = QtWidgets.QFileDialog.getOpenFileName(Dialog_wizard, _translate(
        "Wizard", "Pick a file"), os.path.expanduser("~"), "TeX files (*.tex *.TeX *.TEX)")
    if fileName:
        self.ui_wizard.lineEdit.setText(fileName)
        self.ui_wizard.pushButton_next.setEnabled(True)


def wizard_guess(self):
    # Header
    if self.gheader:
        self.ui_wizard.textEdit.setText(self.gheader)
        self.ui_wizard.label_header.setText(_translate(
            "Wizard", "Here is the header TeXamator is going to use each time it needs to compile a file."))
    else:
        self.ui_wizard.label_header.setText(_translate("Wizard",
                                                       "TeXamator couldn't find a header in the file you gave.\nFeel free to modify the default header : it will be used to compile .tex files."))
        self.ui_wizard.textEdit.setText("\\documentclass{article}")
    self.ui_wizard.listWidget.clear()
    # Tags
    if self.gtags:
        self.ui_wizard.label_tags.setText(_translate(
            "Wizard", "Here are the tags TeXamator found. You can add or delete tags from the list."))
        for i in self.gtags:
            item = QtWidgets.QListWidgetItem(self.ui_wizard.listWidget)
            item.t1 = "\\begin{" + i + "}"
            item.t2 = "\\end{" + i + "}"
            item.setText(item.t1 + " ... " + item.t2)
    else:
        self.ui_wizard.label_tags.setText(_translate(
            "Wizard", "TeXamator couldn't find the tags you use. Please, add them manually."))


def wizard_removetags(self):
    self.ui_wizard.listWidget.takeItem(self.ui_wizard.listWidget.currentRow())


def wizard_addtags(self):
    if self.ui_wizard.lineEdit_tag1.text() and self.ui_wizard.lineEdit_tag2.text():
        item = QtWidgets.QListWidgetItem(self.ui_wizard.listWidget)
        item.t1 = self.ui_wizard.lineEdit_tag1.text()
        item.t2 = self.ui_wizard.lineEdit_tag2.text()
        item.setText(item.t1 + " ... " + item.t2)
        print(type(self.ui_wizard.lineEdit_tag1.text()))


def wizard_apply(self, res):
    self.first_time = False
    if res:
        home_dir = os.path.expanduser("~")
        # Header
        self.preamblesPostambles["Default"][0] = self.ui_wizard.textEdit.toPlainText(
        )
        f = codecs.open(os.path.join(home_dir, ".texamator",
                        "preambles.and.postambles", "Default.preamble.tex"), 'w', "utf-8")
        f.write(self.preamblesPostambles["Default"][0])
        f.close()
        g = codecs.open(os.path.join(home_dir, ".texamator",
                        "preambles.and.postambles", "Default.postamble.tex"), 'w', "utf-8")
        g.write("""\\end{document}""")
        g.close()
        # Tags
        h = codecs.open(os.path.join(
            home_dir, ".texamator", "tags.txt"), 'w', "utf-8")
        self.tags = [[], []]
        for i in range(self.ui_wizard.listWidget.count()):
            t1 = self.ui_wizard.listWidget.item(i).t1
            t2 = self.ui_wizard.listWidget.item(i).t2
            self.tags[0].append(t1)
            self.tags[1].append(t2)
            h.write(t1 + "!!!" + t2 + "\n")
        h.close()
