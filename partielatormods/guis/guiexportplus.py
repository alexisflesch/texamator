#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import os, codecs
import guidepthwarning


def updateUi(self, MyHighlighter):
    #Geometry
    w = self.settings["export width"]
    h = self.settings["export height"]
    self.Dialog_export.resize(int(w),int(h))
    #Change font of textEdit
    self.ui_export.textEdit.setFont(self.myfont)
    #Set up highlighting
    self.highlighter3 = MyHighlighter(self.ui_export.textEdit)
    #Populate header/footer comboBox and select preferred header/footer
    for key in sorted(self.generate):
        self.ui_export.comboBox_header.addItem(key,key)
    num = self.ui_export.comboBox_header.findText(self.settings["preferred header/footer"])
    self.ui_export.comboBox_header.setCurrentIndex(num)
    self.lastHeaderIndex = num
    #Populate Compilation sequence comboBox and select preferred compilation sequence
    for key in sorted(self.compile_seq):
        self.ui_export.comboBox_compile.addItem(key,key)
    num = self.ui_export.comboBox_compile.findText(self.settings["preferred compile sequence for exportation"])
    self.ui_export.comboBox_compile.setCurrentIndex(num)
    #Copy tex code to the textEdit
    value = self.settings["preferred header/footer"]
    self.sources = create_document(self, value)
    self.ui_export.textEdit.setText(self.sources)
    #Slots and signals
    QtCore.QObject.connect(self.ui_export.comboBox_header,\
                            QtCore.SIGNAL("currentIndexChanged(QString)"),self.update_header)
    QtCore.QObject.connect(self.ui_export.comboBox_compile,\
                            QtCore.SIGNAL("currentIndexChanged(QString)"),self.update_compile)
    QtCore.QObject.connect(self.ui_export.pushButton_source,QtCore.SIGNAL("clicked()"), self.source_export)
    QtCore.QObject.connect(self.ui_export.pushButton_close,QtCore.SIGNAL("clicked()"), self.close_export)
    QtCore.QObject.connect(self.ui_export.pushButton_compile,QtCore.SIGNAL("clicked()"), self.compile_export)


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
    self.settings["preferred header/footer"] = value
    if self.sources != unicode(self.ui_export.textEdit.toPlainText()):
        Dialog_warning = QtGui.QDialog()
        ui_warning = guidepthwarning.Ui_Dialog()
        ui_warning.setupUi(Dialog_warning)
        ui_warning.label_2.setText(QtGui.QApplication.translate("Dialog","All the changes you made to the source code will be lost. Do you want to continue?", None, QtGui.QApplication.UnicodeUTF8))
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
    fileName = QtGui.QFileDialog.getSaveFileName(MainWindow,"Save",
                    os.path.join(self.settings["save_location"],"exam.tex"),
                    "TeX files (*.tex);;All files (*.*)")
    if fileName:
        fichier = codecs.open(fileName,'w',"utf-8")
        fichier.write(tex_code)
        fichier.close()


def create_document(self, key):
    sources = self.generate[key][0] + u"\n"
    if "\\begin{document}" not in sources:
        sources += u"\n\\begin{document}\n"
    sources += unicode(self.whole_thing(), "utf-8")
    sources += self.generate[key][1]
    if "\\end{document}" not in self.generate[key][1]:
        sources += u"\n\\end{document}"
    if self.settings['AMC']=='True' and self.AMC_texte:
        if self.settings['AMC-text'] in sources:
            sources = sources.replace(self.settings['AMC-text'],self.AMC_texte)
        else:
            bla = self.AMC_texte + '\n' + '\\end{document}'
            sources = sources.replace('\\end{document}',bla)
    return sources

def compile_export(self):
    self.show_preview_outside(unicode(self.ui_export.textEdit.toPlainText()))

def source_export(self):
    self.save(unicode(self.ui_export.textEdit.toPlainText()))
