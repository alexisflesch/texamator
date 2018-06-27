#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import os, codecs
from . import guidepthwarning

_translate = QtCore.QCoreApplication.translate

def updateUi(self, MyHighlighter):
    #Geometry
    w = self.settings["export width"]
    h = self.settings["export height"]
    self.Dialog_export.resize(int(w),int(h))
    #Change font of textEdit
    self.ui_export.textEdit.setFont(self.myfont)
    #Set up highlighting
    self.highlighter3 = MyHighlighter(self.ui_export.textEdit)
    #Populate preamble comboBox and select preferred preamble for export
    for key in sorted(self.preamblesPostambles):
        self.ui_export.comboBox_header.addItem(key,key)
    num = self.ui_export.comboBox_header.findText(self.settings["preferred preamble for export"])
    self.ui_export.comboBox_header.setCurrentIndex(num)
    self.lastHeaderIndex = num
    #Populate Compilation sequence comboBox and select preferred compilation sequence
    for key in sorted(self.compile_seq):
        self.ui_export.comboBox_compile.addItem(key,key)
    num = self.ui_export.comboBox_compile.findText(self.settings["preferred compile sequence for exportation"])
    self.ui_export.comboBox_compile.setCurrentIndex(num)
    #Copy tex code to the textEdit
    value = self.settings["preferred preamble for export"]
    self.sources = create_document(self, value)
    self.ui_export.textEdit.setText(self.sources)
    #Slots and signals
    self.ui_export.comboBox_header.currentIndexChanged[str].connect(self.update_header)
    self.ui_export.comboBox_compile.currentIndexChanged[str].connect(self.update_compile)
    self.ui_export.pushButton_source.clicked.connect(self.source_export)
    self.ui_export.pushButton_close.clicked.connect(self.close_export)
    self.ui_export.pushButton_compile.clicked.connect(self.compile_export)


def close_export(self):
    """Save geometry"""
    self.settings["export width"] = str(self.Dialog_export.width())
    self.settings["export height"] = str(self.Dialog_export.height())


def update_compile(self, text):
    """Update settings according to comboBox_compile"""
    value = str(text)
    self.settings["preferred compile sequence for exportation"] = value


def update_header(self, text):
    """Update settings and change textEdit according to comboBox_header"""
    value = str(text)
    self.settings["preferred preamble for export"] = value
    if self.sources != self.ui_export.textEdit.toPlainText():
        Dialog_warning = QtWidgets.QDialog()
        ui_warning = guidepthwarning.Ui_Dialog()
        ui_warning.setupUi(Dialog_warning)
        ui_warning.label_2.setText(_translate("Dialog","All the changes you made to the source code will be lost. Do you want to continue?"))
        res = Dialog_warning.exec_()
        if not res:
            self.ui_export.comboBox_header.blockSignals(True)
            self.ui_export.comboBox_header.setCurrentIndex(self.lastHeaderIndex)
            self.ui_export.comboBox_header.blockSignals(False)
            return
    self.sources = create_document(self, value)
    self.ui_export.textEdit.setText(self.sources)
    self.lastHeaderIndex = self.ui_export.comboBox_header.findText(text)


def save(self, tex_code, MainWindow):
    fileName = QtWidgets.QFileDialog.getSaveFileName(MainWindow,"Save",
                    os.path.join(self.settings["save_location"],"exam.tex"),
                    "TeX files (*.tex);;All files (*.*)")
    if fileName:
        fichier = codecs.open(fileName,'w',"utf-8")
        fichier.write(tex_code)
        fichier.close()


def create_document(self, key):
    sources = self.preamblesPostambles[key][0] + "\n"
    if "\\begin{document}" not in sources:
        sources += "\n\\begin{document}\n"
    sources += self.whole_thing()
    sources += self.preamblesPostambles[key][1]
    if "\\end{document}" not in self.preamblesPostambles[key][1]:
        sources += "\n\\end{document}"
    if self.settings['AMC']=='True' and self.AMC_texte:
        if self.settings['AMC-text'] in sources:
            sources = sources.replace(self.settings['AMC-text'],self.AMC_texte)
        else:
            bla = self.AMC_texte + '\n' + '\\end{document}'
            sources = sources.replace('\\end{document}',bla)
    return sources

def compile_export(self):
    self.show_preview_outside(self.ui_export.textEdit.toPlainText())

def source_export(self):
    self.save(self.ui_export.textEdit.toPlainText())
