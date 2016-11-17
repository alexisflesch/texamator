# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'export.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1325, 977)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/all/icones/TeXamator.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame1 = QtGui.QFrame(Dialog)
        self.frame1.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame1.setFrameShadow(QtGui.QFrame.Raised)
        self.frame1.setObjectName(_fromUtf8("frame1"))
        self.gridLayout_3 = QtGui.QGridLayout(self.frame1)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_3 = QtGui.QLabel(self.frame1)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_2.addWidget(self.label_3)
        self.textEdit = QtGui.QTextEdit(self.frame1)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout_2.addWidget(self.textEdit)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame1)
        self.frame0 = QtGui.QFrame(Dialog)
        self.frame0.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame0.setFrameShadow(QtGui.QFrame.Raised)
        self.frame0.setObjectName(_fromUtf8("frame0"))
        self.gridLayout_2 = QtGui.QGridLayout(self.frame0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        spacerItem = QtGui.QSpacerItem(691, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 1, 1, 2)
        spacerItem1 = QtGui.QSpacerItem(691, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 1, 1, 2)
        self.label_4 = QtGui.QLabel(self.frame0)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 2)
        self.comboBox_type = QtGui.QComboBox(self.frame0)
        self.comboBox_type.setObjectName(_fromUtf8("comboBox_type"))
        self.comboBox_type.addItem(_fromUtf8(""))
        self.comboBox_type.setItemText(0, _fromUtf8("dvi"))
        self.comboBox_type.addItem(_fromUtf8(""))
        self.comboBox_type.setItemText(1, _fromUtf8("pdf"))
        self.comboBox_type.addItem(_fromUtf8(""))
        self.comboBox_type.setItemText(2, _fromUtf8("ps"))
        self.comboBox_type.addItem(_fromUtf8(""))
        self.comboBox_type.setItemText(3, _fromUtf8("tex"))
        self.gridLayout_2.addWidget(self.comboBox_type, 0, 3, 1, 1)
        self.comboBox_header = QtGui.QComboBox(self.frame0)
        self.comboBox_header.setObjectName(_fromUtf8("comboBox_header"))
        self.gridLayout_2.addWidget(self.comboBox_header, 1, 3, 1, 1)
        self.label_2 = QtGui.QLabel(self.frame0)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtGui.QLabel(self.frame0)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox_compile = QtGui.QComboBox(self.frame0)
        self.comboBox_compile.setObjectName(_fromUtf8("comboBox_compile"))
        self.gridLayout_2.addWidget(self.comboBox_compile, 2, 3, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(685, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 2, 2, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 3, 2, 1, 1)
        self.verticalLayout.addWidget(self.frame0)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.pushButton_back = QtGui.QPushButton(Dialog)
        self.pushButton_back.setEnabled(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/all/icones/left.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_back.setIcon(icon1)
        self.pushButton_back.setObjectName(_fromUtf8("pushButton_back"))
        self.horizontalLayout.addWidget(self.pushButton_back)
        self.pushButton_next = QtGui.QPushButton(Dialog)
        self.pushButton_next.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/all/icones/right.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_next.setIcon(icon2)
        self.pushButton_next.setObjectName(_fromUtf8("pushButton_next"))
        self.horizontalLayout.addWidget(self.pushButton_next)
        self.pushButton_export = QtGui.QPushButton(Dialog)
        self.pushButton_export.setEnabled(False)
        self.pushButton_export.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/all/icones/filesave.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_export.setIcon(icon3)
        self.pushButton_export.setObjectName(_fromUtf8("pushButton_export"))
        self.horizontalLayout.addWidget(self.pushButton_export)
        self.pushButton_close = QtGui.QPushButton(Dialog)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/all/icones/fileclose.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_close.setIcon(icon4)
        self.pushButton_close.setObjectName(_fromUtf8("pushButton_close"))
        self.horizontalLayout.addWidget(self.pushButton_close)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButton_close, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Export", None))
        self.label_3.setText(_translate("Dialog", "Here are the sources that will be used. You can edit them if you want", None))
        self.label_4.setText(_translate("Dialog", "Choose a compilation sequence", None))
        self.label_2.setText(_translate("Dialog", "Choose a header/footer", None))
        self.label.setText(_translate("Dialog", "What type of file do you want to export ?", None))
        self.pushButton_back.setText(_translate("Dialog", "Back", None))
        self.pushButton_next.setText(_translate("Dialog", "Next", None))
        self.pushButton_export.setText(_translate("Dialog", "Export", None))
        self.pushButton_close.setText(_translate("Dialog", "Close", None))

import icones_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

