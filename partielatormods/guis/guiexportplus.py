#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import os, codecs


def updateUi(self, MyHighlighter):
    #Geometry
    w = self.settings["export width"]
    h = self.settings["export height"]
    self.Dialog_export.resize(int(w),int(h))
    #Change font of textEdit
    self.ui_export.textEdit.setFont(self.myfont)
    #Set up highlighting
    self.highlighter3 = MyHighlighter(self.ui_export.textEdit)
    #Select preferred type of export on the comboBox_type
    num = self.ui_export.comboBox_type.findText(self.settings["preferred type of export"])
    self.ui_export.comboBox_type.setCurrentIndex(num)
    #Populate header/footer comboBox and select preferred header/footer
    for key in sorted(self.generate):
        self.ui_export.comboBox_header.addItem(key,key)
    num = self.ui_export.comboBox_header.findText(self.settings["preferred header/footer"])
    self.ui_export.comboBox_header.setCurrentIndex(num)
    #Populate Compilation sequence comboBox and select preferred compilation sequence
    for key in sorted(self.compile_seq):
        self.ui_export.comboBox_compile.addItem(key,key)
    num = self.ui_export.comboBox_compile.findText(self.settings["preferred compile sequence for exportation"])
    self.ui_export.comboBox_compile.setCurrentIndex(num)
    #Copy tex code to the textEdit
    value = self.settings["preferred header/footer"]
    sources = self.export_sources(value)
    self.ui_export.textEdit.setText(sources)
    #Slots and signals
    QtCore.QObject.connect(self.ui_export.pushButton_next,QtCore.SIGNAL("clicked()"),self.gen_next)
    QtCore.QObject.connect(self.ui_export.pushButton_back,QtCore.SIGNAL("clicked()"),self.gen_back)
    QtCore.QObject.connect(self.ui_export.comboBox_header,\
                            QtCore.SIGNAL("currentIndexChanged(QString)"),self.update_header)
    QtCore.QObject.connect(self.ui_export.comboBox_compile,\
                            QtCore.SIGNAL("currentIndexChanged(QString)"),self.update_compile)
    QtCore.QObject.connect(self.ui_export.comboBox_type,\
                            QtCore.SIGNAL("currentIndexChanged(QString)"),self.update_type)
    QtCore.QObject.connect(self.ui_export.pushButton_export,QtCore.SIGNAL("clicked()"), self.fin_export)
    QtCore.QObject.connect(self.ui_export.pushButton_close,QtCore.SIGNAL("clicked()"), self.close_export)


def close_export(self):
    """Save geometry"""
    self.settings["export width"] = str(self.Dialog_export.width())
    self.settings["export height"] = str(self.Dialog_export.height())

def gen_next(self):
    """Hide frame0, show frame1"""
    self.ui_export.frame0.hide()
    self.ui_export.frame1.show()
    self.ui_export.pushButton_next.setEnabled(False)
    self.ui_export.pushButton_back.setEnabled(True)
    self.ui_export.pushButton_export.setEnabled(True)
    

def gen_back(self):
    self.ui_export.frame1.hide()
    self.ui_export.frame0.show()
    self.ui_export.pushButton_next.setEnabled(True)
    self.ui_export.pushButton_back.setEnabled(False)
    self.ui_export.pushButton_export.setEnabled(False)

def update_type(self, text):
    """Update settings according to comboBox_type"""
    value = str(text)
    self.settings["preferred type of export"] = value
    
def update_compile(self, text):
    """Update settings according to comboBox_compile"""
    value = str(text)
    self.settings["preferred compile sequence for exportation"] = value

def update_header(self, text):
    """Update settings and change textEdit according to comboBox_header"""
    value = str(text)
    self.settings["preferred header/footer"] = value
    sources = self.export_sources(value)
    self.ui_export.textEdit.setText(sources)


def save(self, tex_code, MainWindow):
    fileName = QtGui.QFileDialog.getSaveFileName(MainWindow,"Save",
                    os.path.join(self.settings["save_location"],"exam.tex"),
                    "TeX files (*.tex);;All files (*.*)")
    if fileName:
        fichier = codecs.open(fileName,'w',"utf-8")
        fichier.write(tex_code)
        fichier.close()


def export_sources(self, key):
    sources = self.generate[key][0] + u"\n"
    if "\\begin{document}" not in sources:
        sources += u"\\begin{document}\n"
    sources += unicode(self.whole_thing(), "utf-8")
    sources += self.generate[key][1]
    if "\\end{document}" not in self.generate[key][1]:
        sources += u"\n\\end{document}"
    return sources


def fin_export(self):
    if self.ui_export.comboBox_type.currentText() == "tex":
        self.save(unicode(self.ui_export.textEdit.toPlainText()))
    else:
        self.show_preview_outside(unicode(self.ui_export.textEdit.toPlainText()))
