# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preferences.ui'
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
        Dialog.resize(1443, 997)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/all/icones/TeXamator.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout_2 = QtGui.QGridLayout(Dialog)
        self.gridLayout_2.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.tabWidget = QtGui.QTabWidget(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab1 = QtGui.QWidget()
        self.tab1.setObjectName(_fromUtf8("tab1"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab1)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_9 = QtGui.QLabel(self.tab1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_6.addWidget(self.label_9)
        self.radioButton_yes = QtGui.QRadioButton(self.tab1)
        self.radioButton_yes.setChecked(True)
        self.radioButton_yes.setObjectName(_fromUtf8("radioButton_yes"))
        self.horizontalLayout_6.addWidget(self.radioButton_yes)
        self.radioButton_no = QtGui.QRadioButton(self.tab1)
        self.radioButton_no.setObjectName(_fromUtf8("radioButton_no"))
        self.horizontalLayout_6.addWidget(self.radioButton_no)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label = QtGui.QLabel(self.tab1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_9.addWidget(self.label)
        self.comboBox = QtGui.QComboBox(self.tab1)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.setItemText(0, _fromUtf8("dvi"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.setItemText(1, _fromUtf8("pdf"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.setItemText(2, _fromUtf8("ps"))
        self.horizontalLayout_9.addWidget(self.comboBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_21 = QtGui.QLabel(self.tab1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.horizontalLayout_7.addWidget(self.label_21)
        self.comboBox_viewer = QtGui.QComboBox(self.tab1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_viewer.sizePolicy().hasHeightForWidth())
        self.comboBox_viewer.setSizePolicy(sizePolicy)
        self.comboBox_viewer.setObjectName(_fromUtf8("comboBox_viewer"))
        self.comboBox_viewer.addItem(_fromUtf8(""))
        self.comboBox_viewer.setItemText(0, _fromUtf8("embedded (with dvipng)"))
        self.comboBox_viewer.addItem(_fromUtf8(""))
        self.comboBox_viewer.setItemText(1, _fromUtf8("okular"))
        self.horizontalLayout_7.addWidget(self.comboBox_viewer)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_10 = QtGui.QLabel(self.tab1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_8.addWidget(self.label_10)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.lineEdit_dvi_viewer = QtGui.QLineEdit(self.tab1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_dvi_viewer.sizePolicy().hasHeightForWidth())
        self.lineEdit_dvi_viewer.setSizePolicy(sizePolicy)
        self.lineEdit_dvi_viewer.setText(_fromUtf8(""))
        self.lineEdit_dvi_viewer.setObjectName(_fromUtf8("lineEdit_dvi_viewer"))
        self.horizontalLayout_8.addWidget(self.lineEdit_dvi_viewer)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.line = QtGui.QFrame(self.tab1)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_4.addWidget(self.line)
        self.label_2 = QtGui.QLabel(self.tab1)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_4.addWidget(self.label_2)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.lineEdit_save_folder = QtGui.QLineEdit(self.tab1)
        self.lineEdit_save_folder.setObjectName(_fromUtf8("lineEdit_save_folder"))
        self.horizontalLayout_10.addWidget(self.lineEdit_save_folder)
        self.pushButton_parcourir_sav = QtGui.QPushButton(self.tab1)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/all/icones/folder.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_parcourir_sav.setIcon(icon1)
        self.pushButton_parcourir_sav.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_parcourir_sav.setObjectName(_fromUtf8("pushButton_parcourir_sav"))
        self.horizontalLayout_10.addWidget(self.pushButton_parcourir_sav)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.label_4 = QtGui.QLabel(self.tab1)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_4.addWidget(self.label_4)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.lineEdit_ex_folder = QtGui.QLineEdit(self.tab1)
        self.lineEdit_ex_folder.setObjectName(_fromUtf8("lineEdit_ex_folder"))
        self.horizontalLayout_11.addWidget(self.lineEdit_ex_folder)
        self.pushButton_parcourir_tex_path = QtGui.QPushButton(self.tab1)
        self.pushButton_parcourir_tex_path.setIcon(icon1)
        self.pushButton_parcourir_tex_path.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_parcourir_tex_path.setObjectName(_fromUtf8("pushButton_parcourir_tex_path"))
        self.horizontalLayout_11.addWidget(self.pushButton_parcourir_tex_path)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.line_2 = QtGui.QFrame(self.tab1)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout_4.addWidget(self.line_2)
        spacerItem1 = QtGui.QSpacerItem(20, 439, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.line_2.raise_()
        self.line.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.tabWidget.addTab(self.tab1, _fromUtf8(""))
        self.tabcomp = QtGui.QWidget()
        self.tabcomp.setObjectName(_fromUtf8("tabcomp"))
        self.gridLayout = QtGui.QGridLayout(self.tabcomp)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_7 = QtGui.QLabel(self.tabcomp)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setTextFormat(QtCore.Qt.RichText)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_2.addWidget(self.label_7)
        self.label_siteweb = QtGui.QLabel(self.tabcomp)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_siteweb.sizePolicy().hasHeightForWidth())
        self.label_siteweb.setSizePolicy(sizePolicy)
        self.label_siteweb.setObjectName(_fromUtf8("label_siteweb"))
        self.verticalLayout_2.addWidget(self.label_siteweb)
        self.line_4 = QtGui.QFrame(self.tabcomp)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.verticalLayout_2.addWidget(self.line_4)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_16 = QtGui.QLabel(self.tabcomp)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_4.addWidget(self.label_16)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.comboBox_compile = QtGui.QComboBox(self.tabcomp)
        self.comboBox_compile.setObjectName(_fromUtf8("comboBox_compile"))
        self.horizontalLayout_4.addWidget(self.comboBox_compile)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_19 = QtGui.QLabel(self.tabcomp)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        self.label_19.setWordWrap(True)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.horizontalLayout_5.addWidget(self.label_19)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.pushButton_new_compile_config = QtGui.QPushButton(self.tabcomp)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/all/icones/edit_add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_new_compile_config.setIcon(icon2)
        self.pushButton_new_compile_config.setObjectName(_fromUtf8("pushButton_new_compile_config"))
        self.horizontalLayout_5.addWidget(self.pushButton_new_compile_config)
        self.pushButton_delete_compile_config = QtGui.QPushButton(self.tabcomp)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/all/icones/delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_delete_compile_config.setIcon(icon3)
        self.pushButton_delete_compile_config.setObjectName(_fromUtf8("pushButton_delete_compile_config"))
        self.horizontalLayout_5.addWidget(self.pushButton_delete_compile_config)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.label_8 = QtGui.QLabel(self.tabcomp)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_2.addWidget(self.label_8)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lineEdit_command = QtGui.QLineEdit(self.tabcomp)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_command.sizePolicy().hasHeightForWidth())
        self.lineEdit_command.setSizePolicy(sizePolicy)
        self.lineEdit_command.setObjectName(_fromUtf8("lineEdit_command"))
        self.verticalLayout.addWidget(self.lineEdit_command)
        self.listWidget_comp = QtGui.QListWidget(self.tabcomp)
        self.listWidget_comp.setObjectName(_fromUtf8("listWidget_comp"))
        self.verticalLayout.addWidget(self.listWidget_comp)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.pushButton_addc = QtGui.QPushButton(self.tabcomp)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_addc.sizePolicy().hasHeightForWidth())
        self.pushButton_addc.setSizePolicy(sizePolicy)
        self.pushButton_addc.setText(_fromUtf8(""))
        self.pushButton_addc.setIcon(icon2)
        self.pushButton_addc.setObjectName(_fromUtf8("pushButton_addc"))
        self.verticalLayout_3.addWidget(self.pushButton_addc)
        self.pushButton_removec = QtGui.QPushButton(self.tabcomp)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_removec.sizePolicy().hasHeightForWidth())
        self.pushButton_removec.setSizePolicy(sizePolicy)
        self.pushButton_removec.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/all/icones/edit_remove.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_removec.setIcon(icon4)
        self.pushButton_removec.setObjectName(_fromUtf8("pushButton_removec"))
        self.verticalLayout_3.addWidget(self.pushButton_removec)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.pushButton_up = QtGui.QPushButton(self.tabcomp)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_up.sizePolicy().hasHeightForWidth())
        self.pushButton_up.setSizePolicy(sizePolicy)
        self.pushButton_up.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/all/icones/up.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_up.setIcon(icon5)
        self.pushButton_up.setObjectName(_fromUtf8("pushButton_up"))
        self.verticalLayout_3.addWidget(self.pushButton_up)
        self.pushButton_down = QtGui.QPushButton(self.tabcomp)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_down.sizePolicy().hasHeightForWidth())
        self.pushButton_down.setSizePolicy(sizePolicy)
        self.pushButton_down.setText(_fromUtf8(""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/all/icones/down.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_down.setIcon(icon6)
        self.pushButton_down.setObjectName(_fromUtf8("pushButton_down"))
        self.verticalLayout_3.addWidget(self.pushButton_down)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 2, 2)
        self.line_5 = QtGui.QFrame(self.tabcomp)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.gridLayout.addWidget(self.line_5, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tabcomp, _fromUtf8(""))
        self.tab2 = QtGui.QWidget()
        self.tab2.setObjectName(_fromUtf8("tab2"))
        self.gridlayout = QtGui.QGridLayout(self.tab2)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.label_14 = QtGui.QLabel(self.tab2)
        self.label_14.setWordWrap(True)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridlayout.addWidget(self.label_14, 0, 0, 1, 1)
        self.textEdit = QtGui.QTextEdit(self.tab2)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridlayout.addWidget(self.textEdit, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab2, _fromUtf8(""))
        self.tab21 = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab21.sizePolicy().hasHeightForWidth())
        self.tab21.setSizePolicy(sizePolicy)
        self.tab21.setMinimumSize(QtCore.QSize(1421, 876))
        self.tab21.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tab21.setObjectName(_fromUtf8("tab21"))
        self.gridLayout_6 = QtGui.QGridLayout(self.tab21)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.label_18 = QtGui.QLabel(self.tab21)
        self.label_18.setEnabled(True)
        self.label_18.setWordWrap(True)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout_6.addWidget(self.label_18, 0, 0, 1, 1)
        self.textEdit1 = QtGui.QTextEdit(self.tab21)
        self.textEdit1.setEnabled(True)
        self.textEdit1.setObjectName(_fromUtf8("textEdit1"))
        self.gridLayout_6.addWidget(self.textEdit1, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab21, _fromUtf8(""))
        self.tab3 = QtGui.QWidget()
        self.tab3.setObjectName(_fromUtf8("tab3"))
        self.gridlayout1 = QtGui.QGridLayout(self.tab3)
        self.gridlayout1.setObjectName(_fromUtf8("gridlayout1"))
        self.label_3 = QtGui.QLabel(self.tab3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridlayout1.addWidget(self.label_3, 0, 0, 1, 1)
        self.gridlayout2 = QtGui.QGridLayout()
        self.gridlayout2.setObjectName(_fromUtf8("gridlayout2"))
        self.label_5 = QtGui.QLabel(self.tab3)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridlayout2.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.tab3)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridlayout2.addWidget(self.label_6, 0, 1, 1, 1)
        self.lineEdit_tag1 = QtGui.QLineEdit(self.tab3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_tag1.sizePolicy().hasHeightForWidth())
        self.lineEdit_tag1.setSizePolicy(sizePolicy)
        self.lineEdit_tag1.setObjectName(_fromUtf8("lineEdit_tag1"))
        self.gridlayout2.addWidget(self.lineEdit_tag1, 1, 0, 1, 1)
        self.lineEdit_tag2 = QtGui.QLineEdit(self.tab3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_tag2.sizePolicy().hasHeightForWidth())
        self.lineEdit_tag2.setSizePolicy(sizePolicy)
        self.lineEdit_tag2.setObjectName(_fromUtf8("lineEdit_tag2"))
        self.gridlayout2.addWidget(self.lineEdit_tag2, 1, 1, 1, 1)
        self.gridlayout1.addLayout(self.gridlayout2, 2, 0, 1, 1)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.listWidget = QtGui.QListWidget(self.tab3)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.hboxlayout.addWidget(self.listWidget)
        self.vboxlayout = QtGui.QVBoxLayout()
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.pushButton_add = QtGui.QPushButton(self.tab3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_add.sizePolicy().hasHeightForWidth())
        self.pushButton_add.setSizePolicy(sizePolicy)
        self.pushButton_add.setText(_fromUtf8(""))
        self.pushButton_add.setIcon(icon2)
        self.pushButton_add.setObjectName(_fromUtf8("pushButton_add"))
        self.vboxlayout.addWidget(self.pushButton_add)
        self.pushButton_remove = QtGui.QPushButton(self.tab3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_remove.sizePolicy().hasHeightForWidth())
        self.pushButton_remove.setSizePolicy(sizePolicy)
        self.pushButton_remove.setText(_fromUtf8(""))
        self.pushButton_remove.setIcon(icon4)
        self.pushButton_remove.setObjectName(_fromUtf8("pushButton_remove"))
        self.vboxlayout.addWidget(self.pushButton_remove)
        spacerItem5 = QtGui.QSpacerItem(20, 16, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem5)
        self.hboxlayout.addLayout(self.vboxlayout)
        self.gridlayout1.addLayout(self.hboxlayout, 3, 0, 1, 1)
        self.label_17 = QtGui.QLabel(self.tab3)
        self.label_17.setWordWrap(True)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridlayout1.addWidget(self.label_17, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab3, _fromUtf8(""))
        self.tabGenerate = QtGui.QWidget()
        self.tabGenerate.setObjectName(_fromUtf8("tabGenerate"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.tabGenerate)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.label_12 = QtGui.QLabel(self.tabGenerate)
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.verticalLayout_6.addWidget(self.label_12)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_13 = QtGui.QLabel(self.tabGenerate)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_2.addWidget(self.label_13)
        self.comboBox_gen = QtGui.QComboBox(self.tabGenerate)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_gen.sizePolicy().hasHeightForWidth())
        self.comboBox_gen.setSizePolicy(sizePolicy)
        self.comboBox_gen.setObjectName(_fromUtf8("comboBox_gen"))
        self.horizontalLayout_2.addWidget(self.comboBox_gen)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_15 = QtGui.QLabel(self.tabGenerate)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setWordWrap(True)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout_3.addWidget(self.label_15)
        self.pushButton_newconfig = QtGui.QPushButton(self.tabGenerate)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_newconfig.sizePolicy().hasHeightForWidth())
        self.pushButton_newconfig.setSizePolicy(sizePolicy)
        self.pushButton_newconfig.setIcon(icon2)
        self.pushButton_newconfig.setObjectName(_fromUtf8("pushButton_newconfig"))
        self.horizontalLayout_3.addWidget(self.pushButton_newconfig)
        self.pushButton_delete = QtGui.QPushButton(self.tabGenerate)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_delete.sizePolicy().hasHeightForWidth())
        self.pushButton_delete.setSizePolicy(sizePolicy)
        self.pushButton_delete.setIcon(icon3)
        self.pushButton_delete.setObjectName(_fromUtf8("pushButton_delete"))
        self.horizontalLayout_3.addWidget(self.pushButton_delete)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.line_3 = QtGui.QFrame(self.tabGenerate)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout_6.addWidget(self.line_3)
        self.splitter = QtGui.QSplitter(self.tabGenerate)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.textEdit_generate = QtGui.QTextEdit(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_generate.sizePolicy().hasHeightForWidth())
        self.textEdit_generate.setSizePolicy(sizePolicy)
        self.textEdit_generate.setMinimumSize(QtCore.QSize(0, 120))
        self.textEdit_generate.setObjectName(_fromUtf8("textEdit_generate"))
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_20 = QtGui.QLabel(self.layoutWidget)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.verticalLayout_5.addWidget(self.label_20)
        self.textEdit_generate_footer = QtGui.QTextEdit(self.layoutWidget)
        self.textEdit_generate_footer.setMinimumSize(QtCore.QSize(0, 120))
        self.textEdit_generate_footer.setObjectName(_fromUtf8("textEdit_generate_footer"))
        self.verticalLayout_5.addWidget(self.textEdit_generate_footer)
        self.verticalLayout_6.addWidget(self.splitter)
        self.tabWidget.addTab(self.tabGenerate, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        spacerItem6 = QtGui.QSpacerItem(385, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem6)
        self.pushButton_cancel = QtGui.QPushButton(Dialog)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/all/icones/cancel.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_cancel.setIcon(icon7)
        self.pushButton_cancel.setObjectName(_fromUtf8("pushButton_cancel"))
        self.horizontalLayout_12.addWidget(self.pushButton_cancel)
        self.pushButton_ok = QtGui.QPushButton(Dialog)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/all/icones/apply.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_ok.setIcon(icon8)
        self.pushButton_ok.setObjectName(_fromUtf8("pushButton_ok"))
        self.horizontalLayout_12.addWidget(self.pushButton_ok)
        self.gridLayout_2.addLayout(self.horizontalLayout_12, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.pushButton_ok, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.accept)
        QtCore.QObject.connect(self.pushButton_cancel, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Preferences", None))
        self.label_9.setText(_translate("Dialog", "Do you want to use the preview package (default : yes) ?", None))
        self.radioButton_yes.setText(_translate("Dialog", "&Yes", None))
        self.radioButton_no.setText(_translate("Dialog", "&No", None))
        self.label.setText(_translate("Dialog", "What type of file will you generate ? (default : pdf)", None))
        self.label_21.setText(_translate("Dialog", "Which viewer do you want TeXamator to use inside the application ? (default : okular)", None))
        self.label_10.setText(_translate("Dialog", "Which viewer do you want to use when you export a project ?", None))
        self.label_2.setText(_translate("Dialog", "Default folder in which you wish to save your projects ?", None))
        self.pushButton_parcourir_sav.setText(_translate("Dialog", "Browse", None))
        self.label_4.setText(_translate("Dialog", "Which folder contains your tex files ?", None))
        self.pushButton_parcourir_tex_path.setText(_translate("Dialog", "Browse", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("Dialog", "Basics", None))
        self.label_7.setText(_translate("Dialog", "Here you can set up the way LaTeX is called in the background. Leave default settings if unsure. Help is available online here :\n"
"", None))
        self.label_siteweb.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"http://alexisfles.ch/en\"><span style=\" text-decoration: underline; color:#0000ff;\">http://alexisfles.ch/en</span></a></p></body></html>", None))
        self.label_16.setText(_translate("Dialog", "Select the config to use (and edit it if you want to)", None))
        self.label_19.setText(_translate("Dialog", "If you want, you can create your own compile sequence", None))
        self.pushButton_new_compile_config.setText(_translate("Dialog", "New Config", None))
        self.pushButton_delete_compile_config.setText(_translate("Dialog", "Delete", None))
        self.label_8.setText(_translate("Dialog", "Write a command and click the + button to add it", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabcomp), _translate("Dialog", "Compilation", None))
        self.label_14.setText(_translate("Dialog", "This is the header used by TeXamator to compile your .tex files. You can include \\begin{document} if you want.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("Dialog", "Header", None))
        self.label_18.setText(_translate("Dialog", "This is the footer used by TeXamator to compile your .tex files.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab21), _translate("Dialog", "Footer", None))
        self.label_3.setText(_translate("Dialog", "Set up the tags you use for your exercises", None))
        self.label_5.setText(_translate("Dialog", "What comes before an exercise ?", None))
        self.label_6.setText(_translate("Dialog", "What comes after ?", None))
        self.label_17.setText(_translate("Dialog", "TeXamator needs to know how to extract exercises from your .tex files.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), _translate("Dialog", "Tags", None))
        self.label_12.setText(_translate("Dialog", "Here, you can set up the way files are generated when you click the \"export\" button. For example, you could add an \"Exercise sheet\" config and another one, say \"Exam\". Add as many configs as you want.", None))
        self.label_13.setText(_translate("Dialog", "Select a config name", None))
        self.label_15.setText(_translate("Dialog", "Set here what you want to appear before your exercises", None))
        self.pushButton_newconfig.setText(_translate("Dialog", "New Config", None))
        self.pushButton_delete.setText(_translate("Dialog", "Delete", None))
        self.label_20.setText(_translate("Dialog", "Set here what you want to appear after your exercises", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGenerate), _translate("Dialog", "Generating files", None))
        self.pushButton_cancel.setText(_translate("Dialog", "Cancel", None))
        self.pushButton_ok.setText(_translate("Dialog", "Ok", None))

import icones_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

