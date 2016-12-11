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
        self.frame0 = QtGui.QFrame(Dialog)
        self.frame0.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame0.setFrameShadow(QtGui.QFrame.Raised)
        self.frame0.setObjectName(_fromUtf8("frame0"))
        self.gridLayout_2 = QtGui.QGridLayout(self.frame0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_2 = QtGui.QLabel(self.frame0)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(685, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(691, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 1, 1, 2)
        self.comboBox_header = QtGui.QComboBox(self.frame0)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_header.sizePolicy().hasHeightForWidth())
        self.comboBox_header.setSizePolicy(sizePolicy)
        self.comboBox_header.setObjectName(_fromUtf8("comboBox_header"))
        self.gridLayout_2.addWidget(self.comboBox_header, 0, 3, 1, 1)
        self.label_4 = QtGui.QLabel(self.frame0)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 2)
        self.comboBox_compile = QtGui.QComboBox(self.frame0)
        self.comboBox_compile.setObjectName(_fromUtf8("comboBox_compile"))
        self.gridLayout_2.addWidget(self.comboBox_compile, 1, 3, 1, 1)
        self.gridLayout.addWidget(self.frame0, 0, 0, 1, 1)
        self.frame1 = QtGui.QFrame(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame1.sizePolicy().hasHeightForWidth())
        self.frame1.setSizePolicy(sizePolicy)
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
        self.gridLayout.addWidget(self.frame1, 1, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButton_source = QtGui.QPushButton(Dialog)
        self.pushButton_source.setEnabled(True)
        self.pushButton_source.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/all/icones/filesave.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_source.setIcon(icon1)
        self.pushButton_source.setObjectName(_fromUtf8("pushButton_source"))
        self.horizontalLayout.addWidget(self.pushButton_source)
        self.pushButton_compile = QtGui.QPushButton(Dialog)
        self.pushButton_compile.setEnabled(True)
        self.pushButton_compile.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/all/icones/pdf.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_compile.setIcon(icon2)
        self.pushButton_compile.setObjectName(_fromUtf8("pushButton_compile"))
        self.horizontalLayout.addWidget(self.pushButton_compile)
        self.pushButton_close = QtGui.QPushButton(Dialog)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/all/icones/fileclose.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_close.setIcon(icon3)
        self.pushButton_close.setObjectName(_fromUtf8("pushButton_close"))
        self.horizontalLayout.addWidget(self.pushButton_close)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButton_close, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Export", None))
        self.label_2.setText(_translate("Dialog", "Choose a header/footer", None))
        self.label_4.setText(_translate("Dialog", "Choose a compilation sequence", None))
        self.label_3.setText(_translate("Dialog", "Here are the sources that will be used. You can edit them if you want", None))
        self.pushButton_source.setText(_translate("Dialog", "Export source", None))
        self.pushButton_compile.setText(_translate("Dialog", "Compile and export", None))
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

