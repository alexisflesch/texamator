# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'export.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1325, 977)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/all/icones/TeXamator.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.frame0 = QtWidgets.QFrame(Dialog)
        self.frame0.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame0.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame0.setObjectName("frame0")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame0)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(685, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(691, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 1, 1, 2)
        self.comboBox_header = QtWidgets.QComboBox(self.frame0)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_header.sizePolicy().hasHeightForWidth())
        self.comboBox_header.setSizePolicy(sizePolicy)
        self.comboBox_header.setObjectName("comboBox_header")
        self.gridLayout_2.addWidget(self.comboBox_header, 0, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame0)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 2)
        self.comboBox_compile = QtWidgets.QComboBox(self.frame0)
        self.comboBox_compile.setObjectName("comboBox_compile")
        self.gridLayout_2.addWidget(self.comboBox_compile, 1, 3, 1, 1)
        self.gridLayout.addWidget(self.frame0, 0, 0, 1, 1)
        self.frame1 = QtWidgets.QFrame(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame1.sizePolicy().hasHeightForWidth())
        self.frame1.setSizePolicy(sizePolicy)
        self.frame1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame1.setObjectName("frame1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.frame1)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.textEdit = QtWidgets.QTextEdit(self.frame1)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_2.addWidget(self.textEdit)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame1, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButton_source = QtWidgets.QPushButton(Dialog)
        self.pushButton_source.setEnabled(True)
        self.pushButton_source.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/all/icones/filesave.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_source.setIcon(icon1)
        self.pushButton_source.setObjectName("pushButton_source")
        self.horizontalLayout.addWidget(self.pushButton_source)
        self.pushButton_compile = QtWidgets.QPushButton(Dialog)
        self.pushButton_compile.setEnabled(True)
        self.pushButton_compile.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/all/icones/pdf.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_compile.setIcon(icon2)
        self.pushButton_compile.setObjectName("pushButton_compile")
        self.horizontalLayout.addWidget(self.pushButton_compile)
        self.pushButton_close = QtWidgets.QPushButton(Dialog)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/all/icones/fileclose.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_close.setIcon(icon3)
        self.pushButton_close.setObjectName("pushButton_close")
        self.horizontalLayout.addWidget(self.pushButton_close)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.pushButton_close.clicked.connect(Dialog.accept) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Export"))
        self.label_2.setText(_translate("Dialog", "Choose a header/footer"))
        self.label_4.setText(_translate("Dialog", "Choose a compilation sequence"))
        self.label_3.setText(_translate("Dialog", "Here are the sources that will be used. You can edit them if you want"))
        self.pushButton_source.setText(_translate("Dialog", "Export source"))
        self.pushButton_compile.setText(_translate("Dialog", "Compile and export"))
        self.pushButton_close.setText(_translate("Dialog", "Close"))
from . import icones_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
