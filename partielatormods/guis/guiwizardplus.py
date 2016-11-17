#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import os, codecs


def updateUi(self, MyHighlighter, Dialog_wizard):
    #Change font of textEdit
    self.ui_wizard.textEdit.setFont(self.myfont)
    #Set up highlighting
    self.highlighter4 = MyHighlighter(self.ui_wizard.textEdit)
    #Current frame
    self.ui_wizard.frame2.hide()
    self.ui_wizard.frame3.hide()
    self.ui_wizard.whatframe = 1
    #Is it the first time TeXamator is launched ?
    if self.first_time:
        self.ui_wizard.label_warning.setText("It looks like it is the first time you use TeXamator on this computer !")
    #Shape
    Dialog_wizard.resize(500,400)
    #Slots and signals
    QtCore.QObject.connect(self.ui_wizard.pushButton_next,QtCore.SIGNAL("clicked()"),self.wizard_next)
    QtCore.QObject.connect(self.ui_wizard.pushButton_back,QtCore.SIGNAL("clicked()"),self.wizard_back)
    QtCore.QObject.connect(self.ui_wizard.pushButton_browse,QtCore.SIGNAL("clicked()"),self.wizard_browse)
    QtCore.QObject.connect(self.ui_wizard.pushButton_remove,QtCore.SIGNAL("clicked()"),self.wizard_removetags)
    QtCore.QObject.connect(self.ui_wizard.pushButton_add,QtCore.SIGNAL("clicked()"),self.wizard_addtags)
    QtCore.QObject.connect(self.ui_wizard.lineEdit,QtCore.SIGNAL("textChanged(QString)"),self.wizard_allow_next)

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
    dirName = QtGui.QFileDialog.getOpenFileName(Dialog_wizard,"Pick a folder",
                self.settings["tex_path"], "TeX files (*.tex *.TeX *.TEX)")
    if dirName:
        self.ui_wizard.lineEdit.setText(dirName)
        self.ui_wizard.pushButton_next.setEnabled(True)


def wizard_guess(self):
    #Header
    if self.gheader:
        self.ui_wizard.textEdit.setText(self.gheader)
        self.ui_wizard.label_header.setText(QtGui.QApplication.translate( "Dialog",\
            "Here is the header TeXamator is going to use each time it needs to compile a file.",\
            None, QtGui.QApplication.UnicodeUTF8))
    else:
        self.ui_wizard.label_header.setText(QtGui.QApplication.translate( "Dialog",\
            "TeXamator couldn't find a header in the file you gave.\nFeel free to modify the default header : it will be used to compile .tex files.",\
            None, QtGui.QApplication.UnicodeUTF8))
        self.ui_wizard.textEdit.setText("\\documentclass{article}")
    self.ui_wizard.listWidget.clear()
    #Tags
    if self.gtags:
        self.ui_wizard.label_tags.setText(QtGui.QApplication.translate( "Dialog",\
            "Here are the tags TeXamator found. You can add or delete tags from the list.",\
            None, QtGui.QApplication.UnicodeUTF8))
        for i in self.gtags:
            item = QtGui.QListWidgetItem(self.ui_wizard.listWidget)
            item.t1 = "\\begin{" + i + "}"
            item.t2 = "\\end{" + i + "}"
            item.setText(item.t1 + u" ... " + item.t2)
    else:
        self.ui_wizard.label_tags.setText(QtGui.QApplication.translate( "Dialog",\
            "TeXamator couldn't find the tags you use. Please, add them manually.",\
            None, QtGui.QApplication.UnicodeUTF8))


def wizard_removetags(self):
    self.ui_wizard.listWidget.takeItem(self.ui_wizard.listWidget.currentRow())


def wizard_addtags(self):
    if unicode(self.ui_wizard.lineEdit_tag1.text()) and unicode(self.ui_wizard.lineEdit_tag2.text()):
        item = QtGui.QListWidgetItem(self.ui_wizard.listWidget)
        item.t1 = unicode(self.ui_wizard.lineEdit_tag1.text())
        item.t2 = unicode(self.ui_wizard.lineEdit_tag2.text())
        item.setText(item.t1 + u" ... " + item.t2)


def wizard_apply(self, res):
    self.first_time = False
    if res:
        home_dir = os.path.expanduser("~")
        #Header
        self.header = unicode(self.ui_wizard.textEdit.toPlainText())
        g = codecs.open(os.path.join(home_dir, ".partielator", "header"), 'w', "utf-8")
        g.write(self.header)
        g.close()
        #Tags
        h = codecs.open(os.path.join(home_dir, ".partielator", "tags"), 'w', "utf-8")
        self.tags = [[], []]
        for i in range(self.ui_wizard.listWidget.count()):
            t1 = self.ui_wizard.listWidget.item(i).t1
            t2 = self.ui_wizard.listWidget.item(i).t2
            self.tags[0].append(t1)
            self.tags[1].append(t2)
            h.write(t1 + "!!!" + t2 + "\n")
        h.close()
