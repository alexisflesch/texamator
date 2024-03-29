# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preferences.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(655, 475)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/all/icones/TeXamator.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem = QtWidgets.QSpacerItem(385, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem)
        self.pushButton_cancel = QtWidgets.QPushButton(Dialog)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/all/icones/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_cancel.setIcon(icon1)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout_12.addWidget(self.pushButton_cancel)
        self.pushButton_ok = QtWidgets.QPushButton(Dialog)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/all/icones/apply.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_ok.setIcon(icon2)
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.horizontalLayout_12.addWidget(self.pushButton_ok)
        self.gridLayout_2.addLayout(self.horizontalLayout_12, 1, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_10 = QtWidgets.QLabel(self.tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_8.addWidget(self.label_10)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.lineEdit_dvi_viewer = QtWidgets.QLineEdit(self.tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_dvi_viewer.sizePolicy().hasHeightForWidth())
        self.lineEdit_dvi_viewer.setSizePolicy(sizePolicy)
        self.lineEdit_dvi_viewer.setText("")
        self.lineEdit_dvi_viewer.setObjectName("lineEdit_dvi_viewer")
        self.horizontalLayout_8.addWidget(self.lineEdit_dvi_viewer)
        self.gridLayout_3.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.tab1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_3.addWidget(self.line, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab1)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 2, 0, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.lineEdit_save_folder = QtWidgets.QLineEdit(self.tab1)
        self.lineEdit_save_folder.setObjectName("lineEdit_save_folder")
        self.horizontalLayout_10.addWidget(self.lineEdit_save_folder)
        self.pushButton_parcourir_sav = QtWidgets.QPushButton(self.tab1)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/all/icones/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_parcourir_sav.setIcon(icon3)
        self.pushButton_parcourir_sav.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_parcourir_sav.setObjectName("pushButton_parcourir_sav")
        self.horizontalLayout_10.addWidget(self.pushButton_parcourir_sav)
        self.gridLayout_3.addLayout(self.horizontalLayout_10, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab1)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 4, 0, 1, 1)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.lineEdit_ex_folder = QtWidgets.QLineEdit(self.tab1)
        self.lineEdit_ex_folder.setObjectName("lineEdit_ex_folder")
        self.horizontalLayout_11.addWidget(self.lineEdit_ex_folder)
        self.pushButton_parcourir_tex_path = QtWidgets.QPushButton(self.tab1)
        self.pushButton_parcourir_tex_path.setIcon(icon3)
        self.pushButton_parcourir_tex_path.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_parcourir_tex_path.setObjectName("pushButton_parcourir_tex_path")
        self.horizontalLayout_11.addWidget(self.pushButton_parcourir_tex_path)
        self.gridLayout_3.addLayout(self.horizontalLayout_11, 5, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.tab1)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_3.addWidget(self.line_2, 6, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 439, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 7, 0, 1, 1)
        self.line_2.raise_()
        self.line.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.tabWidget.addTab(self.tab1, "")
        self.tab3 = QtWidgets.QWidget()
        self.tab3.setObjectName("tab3")
        self.gridlayout = QtWidgets.QGridLayout(self.tab3)
        self.gridlayout.setObjectName("gridlayout")
        self.label_3 = QtWidgets.QLabel(self.tab3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridlayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.gridlayout1 = QtWidgets.QGridLayout()
        self.gridlayout1.setObjectName("gridlayout1")
        self.label_5 = QtWidgets.QLabel(self.tab3)
        self.label_5.setObjectName("label_5")
        self.gridlayout1.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab3)
        self.label_6.setObjectName("label_6")
        self.gridlayout1.addWidget(self.label_6, 0, 1, 1, 1)
        self.lineEdit_tag1 = QtWidgets.QLineEdit(self.tab3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_tag1.sizePolicy().hasHeightForWidth())
        self.lineEdit_tag1.setSizePolicy(sizePolicy)
        self.lineEdit_tag1.setObjectName("lineEdit_tag1")
        self.gridlayout1.addWidget(self.lineEdit_tag1, 1, 0, 1, 1)
        self.lineEdit_tag2 = QtWidgets.QLineEdit(self.tab3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_tag2.sizePolicy().hasHeightForWidth())
        self.lineEdit_tag2.setSizePolicy(sizePolicy)
        self.lineEdit_tag2.setObjectName("lineEdit_tag2")
        self.gridlayout1.addWidget(self.lineEdit_tag2, 1, 1, 1, 1)
        self.gridlayout.addLayout(self.gridlayout1, 2, 0, 1, 1)
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.listWidget = QtWidgets.QListWidget(self.tab3)
        self.listWidget.setObjectName("listWidget")
        self.hboxlayout.addWidget(self.listWidget)
        self.vboxlayout = QtWidgets.QVBoxLayout()
        self.vboxlayout.setObjectName("vboxlayout")
        self.pushButton_add = QtWidgets.QPushButton(self.tab3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_add.sizePolicy().hasHeightForWidth())
        self.pushButton_add.setSizePolicy(sizePolicy)
        self.pushButton_add.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/all/icones/edit_add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_add.setIcon(icon4)
        self.pushButton_add.setObjectName("pushButton_add")
        self.vboxlayout.addWidget(self.pushButton_add)
        self.pushButton_remove = QtWidgets.QPushButton(self.tab3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_remove.sizePolicy().hasHeightForWidth())
        self.pushButton_remove.setSizePolicy(sizePolicy)
        self.pushButton_remove.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/all/icones/edit_remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_remove.setIcon(icon5)
        self.pushButton_remove.setObjectName("pushButton_remove")
        self.vboxlayout.addWidget(self.pushButton_remove)
        spacerItem3 = QtWidgets.QSpacerItem(20, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem3)
        self.hboxlayout.addLayout(self.vboxlayout)
        self.gridlayout.addLayout(self.hboxlayout, 3, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.tab3)
        self.label_17.setWordWrap(True)
        self.label_17.setObjectName("label_17")
        self.gridlayout.addWidget(self.label_17, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab3, "")
        self.tabcomp = QtWidgets.QWidget()
        self.tabcomp.setObjectName("tabcomp")
        self.gridLayout = QtWidgets.QGridLayout(self.tabcomp)
        self.gridLayout.setObjectName("gridLayout")
        self.label_7 = QtWidgets.QLabel(self.tabcomp)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setTextFormat(QtCore.Qt.AutoText)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 2)
        self.label_siteweb = QtWidgets.QLabel(self.tabcomp)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_siteweb.sizePolicy().hasHeightForWidth())
        self.label_siteweb.setSizePolicy(sizePolicy)
        self.label_siteweb.setObjectName("label_siteweb")
        self.gridLayout.addWidget(self.label_siteweb, 1, 0, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.tabcomp)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 2, 0, 1, 2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_16 = QtWidgets.QLabel(self.tabcomp)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_4.addWidget(self.label_16)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.comboBox_compile = QtWidgets.QComboBox(self.tabcomp)
        self.comboBox_compile.setObjectName("comboBox_compile")
        self.horizontalLayout_4.addWidget(self.comboBox_compile)
        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_19 = QtWidgets.QLabel(self.tabcomp)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        self.label_19.setWordWrap(True)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_5.addWidget(self.label_19)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.pushButton_new_compile_config = QtWidgets.QPushButton(self.tabcomp)
        self.pushButton_new_compile_config.setIcon(icon4)
        self.pushButton_new_compile_config.setObjectName("pushButton_new_compile_config")
        self.horizontalLayout_5.addWidget(self.pushButton_new_compile_config)
        self.pushButton_delete_compile_config = QtWidgets.QPushButton(self.tabcomp)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/all/icones/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_delete_compile_config.setIcon(icon6)
        self.pushButton_delete_compile_config.setObjectName("pushButton_delete_compile_config")
        self.horizontalLayout_5.addWidget(self.pushButton_delete_compile_config)
        self.gridLayout.addLayout(self.horizontalLayout_5, 4, 0, 1, 2)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_8 = QtWidgets.QLabel(self.tabcomp)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_13.addWidget(self.label_8)
        self.gridLayout.addLayout(self.horizontalLayout_13, 5, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_command = QtWidgets.QLineEdit(self.tabcomp)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_command.sizePolicy().hasHeightForWidth())
        self.lineEdit_command.setSizePolicy(sizePolicy)
        self.lineEdit_command.setObjectName("lineEdit_command")
        self.verticalLayout.addWidget(self.lineEdit_command)
        self.listWidget_comp = QtWidgets.QListWidget(self.tabcomp)
        self.listWidget_comp.setObjectName("listWidget_comp")
        self.verticalLayout.addWidget(self.listWidget_comp)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_addc = QtWidgets.QPushButton(self.tabcomp)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_addc.sizePolicy().hasHeightForWidth())
        self.pushButton_addc.setSizePolicy(sizePolicy)
        self.pushButton_addc.setText("")
        self.pushButton_addc.setIcon(icon4)
        self.pushButton_addc.setObjectName("pushButton_addc")
        self.verticalLayout_3.addWidget(self.pushButton_addc)
        self.pushButton_removec = QtWidgets.QPushButton(self.tabcomp)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_removec.sizePolicy().hasHeightForWidth())
        self.pushButton_removec.setSizePolicy(sizePolicy)
        self.pushButton_removec.setText("")
        self.pushButton_removec.setIcon(icon5)
        self.pushButton_removec.setObjectName("pushButton_removec")
        self.verticalLayout_3.addWidget(self.pushButton_removec)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem6)
        self.pushButton_up = QtWidgets.QPushButton(self.tabcomp)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_up.sizePolicy().hasHeightForWidth())
        self.pushButton_up.setSizePolicy(sizePolicy)
        self.pushButton_up.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/all/icones/up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_up.setIcon(icon7)
        self.pushButton_up.setObjectName("pushButton_up")
        self.verticalLayout_3.addWidget(self.pushButton_up)
        self.pushButton_down = QtWidgets.QPushButton(self.tabcomp)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_down.sizePolicy().hasHeightForWidth())
        self.pushButton_down.setSizePolicy(sizePolicy)
        self.pushButton_down.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/all/icones/down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_down.setIcon(icon8)
        self.pushButton_down.setObjectName("pushButton_down")
        self.verticalLayout_3.addWidget(self.pushButton_down)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.gridLayout.addLayout(self.horizontalLayout, 6, 0, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.tabcomp)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout.addWidget(self.line_5, 7, 1, 1, 1)
        self.tabWidget.addTab(self.tabcomp, "")
        self.tabGenerate = QtWidgets.QWidget()
        self.tabGenerate.setObjectName("tabGenerate")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tabGenerate)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_12 = QtWidgets.QLabel(self.tabGenerate)
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_6.addWidget(self.label_12)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_13 = QtWidgets.QLabel(self.tabGenerate)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_2.addWidget(self.label_13)
        self.comboBox_gen = QtWidgets.QComboBox(self.tabGenerate)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_gen.sizePolicy().hasHeightForWidth())
        self.comboBox_gen.setSizePolicy(sizePolicy)
        self.comboBox_gen.setObjectName("comboBox_gen")
        self.horizontalLayout_2.addWidget(self.comboBox_gen)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_15 = QtWidgets.QLabel(self.tabGenerate)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setWordWrap(True)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_3.addWidget(self.label_15)
        self.pushButton_newconfig = QtWidgets.QPushButton(self.tabGenerate)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_newconfig.sizePolicy().hasHeightForWidth())
        self.pushButton_newconfig.setSizePolicy(sizePolicy)
        self.pushButton_newconfig.setIcon(icon4)
        self.pushButton_newconfig.setObjectName("pushButton_newconfig")
        self.horizontalLayout_3.addWidget(self.pushButton_newconfig)
        self.pushButton_delete = QtWidgets.QPushButton(self.tabGenerate)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_delete.sizePolicy().hasHeightForWidth())
        self.pushButton_delete.setSizePolicy(sizePolicy)
        self.pushButton_delete.setIcon(icon6)
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.horizontalLayout_3.addWidget(self.pushButton_delete)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.line_3 = QtWidgets.QFrame(self.tabGenerate)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_6.addWidget(self.line_3)
        self.splitter = QtWidgets.QSplitter(self.tabGenerate)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setHandleWidth(6)
        self.splitter.setObjectName("splitter")
        self.textEdit_generate = QtWidgets.QTextEdit(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_generate.sizePolicy().hasHeightForWidth())
        self.textEdit_generate.setSizePolicy(sizePolicy)
        self.textEdit_generate.setMinimumSize(QtCore.QSize(0, 120))
        self.textEdit_generate.setObjectName("textEdit_generate")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_20 = QtWidgets.QLabel(self.layoutWidget)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_5.addWidget(self.label_20)
        self.textEdit_generate_footer = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit_generate_footer.setMinimumSize(QtCore.QSize(0, 120))
        self.textEdit_generate_footer.setObjectName("textEdit_generate_footer")
        self.verticalLayout_5.addWidget(self.textEdit_generate_footer)
        self.verticalLayout_6.addWidget(self.splitter)
        self.tabWidget.addTab(self.tabGenerate, "")
        self.tabAMC = QtWidgets.QWidget()
        self.tabAMC.setObjectName("tabAMC")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tabAMC)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.tabAMC)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_siteweb_3 = QtWidgets.QLabel(self.tabAMC)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_siteweb_3.sizePolicy().hasHeightForWidth())
        self.label_siteweb_3.setSizePolicy(sizePolicy)
        self.label_siteweb_3.setObjectName("label_siteweb_3")
        self.verticalLayout_2.addWidget(self.label_siteweb_3)
        self.label_23 = QtWidgets.QLabel(self.tabAMC)
        self.label_23.setWordWrap(True)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_2.addWidget(self.label_23)
        self.label_siteweb_2 = QtWidgets.QLabel(self.tabAMC)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_siteweb_2.sizePolicy().hasHeightForWidth())
        self.label_siteweb_2.setSizePolicy(sizePolicy)
        self.label_siteweb_2.setObjectName("label_siteweb_2")
        self.verticalLayout_2.addWidget(self.label_siteweb_2)
        self.line_6 = QtWidgets.QFrame(self.tabAMC)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout_2.addWidget(self.line_6)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_9 = QtWidgets.QLabel(self.tabAMC)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_6.addWidget(self.label_9)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        self.radioButtonAMCYes = QtWidgets.QRadioButton(self.tabAMC)
        self.radioButtonAMCYes.setChecked(False)
        self.radioButtonAMCYes.setObjectName("radioButtonAMCYes")
        self.horizontalLayout_6.addWidget(self.radioButtonAMCYes)
        self.radioButtonAMCNo = QtWidgets.QRadioButton(self.tabAMC)
        self.radioButtonAMCNo.setChecked(True)
        self.radioButtonAMCNo.setObjectName("radioButtonAMCNo")
        self.horizontalLayout_6.addWidget(self.radioButtonAMCNo)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_21 = QtWidgets.QLabel(self.tabAMC)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_7.addWidget(self.label_21)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem8)
        self.lineEditAMCEnv = QtWidgets.QLineEdit(self.tabAMC)
        self.lineEditAMCEnv.setObjectName("lineEditAMCEnv")
        self.horizontalLayout_7.addWidget(self.lineEditAMCEnv)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.line_7 = QtWidgets.QFrame(self.tabAMC)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.verticalLayout_2.addWidget(self.line_7)
        self.label_24 = QtWidgets.QLabel(self.tabAMC)
        self.label_24.setWordWrap(True)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_2.addWidget(self.label_24)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_25 = QtWidgets.QLabel(self.tabAMC)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_9.addWidget(self.label_25)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem9)
        self.lineEditAMCText = QtWidgets.QLineEdit(self.tabAMC)
        self.lineEditAMCText.setObjectName("lineEditAMCText")
        self.horizontalLayout_9.addWidget(self.lineEditAMCText)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        spacerItem10 = QtWidgets.QSpacerItem(20, 429, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem10)
        self.tabWidget.addTab(self.tabAMC, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.pushButton_ok.clicked.connect(Dialog.accept) # type: ignore
        self.pushButton_cancel.clicked.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Preferences"))
        self.pushButton_cancel.setText(_translate("Dialog", "Cancel"))
        self.pushButton_ok.setText(_translate("Dialog", "Ok"))
        self.label_10.setText(_translate("Dialog", "Which viewer do you want to use when you export a project ?"))
        self.label_2.setText(_translate("Dialog", "Default folder in which you wish to save your projects ?"))
        self.pushButton_parcourir_sav.setText(_translate("Dialog", "Browse"))
        self.label_4.setText(_translate("Dialog", "Which folder contains your tex files ?"))
        self.pushButton_parcourir_tex_path.setText(_translate("Dialog", "Browse"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("Dialog", "Basics"))
        self.label_3.setText(_translate("Dialog", "Set up the tags you use for your exercises"))
        self.label_5.setText(_translate("Dialog", "What comes before an exercise ?"))
        self.label_6.setText(_translate("Dialog", "What comes after ?"))
        self.label_17.setText(_translate("Dialog", "TeXamator needs to know how to extract exercises from your .tex files."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), _translate("Dialog", "Tags"))
        self.label_7.setText(_translate("Dialog", "Here you can set up the way LaTeX is called to preview exercises. TeXamator will try to show \"file.pdf\" after running the following commands. Help is available online here :"))
        self.label_siteweb.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Noto Sans\'; font-size:9pt;\">https://github.com/alexisflesch/texamator</span></p></body></html>"))
        self.label_16.setText(_translate("Dialog", "Select the config to use (and edit it if you want to)"))
        self.label_19.setText(_translate("Dialog", "If you want, you can create your own compile sequence"))
        self.pushButton_new_compile_config.setText(_translate("Dialog", "New Config"))
        self.pushButton_delete_compile_config.setText(_translate("Dialog", "Delete"))
        self.label_8.setText(_translate("Dialog", "Write a command and click the + button to add it."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabcomp), _translate("Dialog", "Compilation"))
        self.label_12.setText(_translate("Dialog", "Here, you can set up preambles and postambles used to preview exercises as well as when you click the \"export\" button."))
        self.label_13.setText(_translate("Dialog", "Select a config name"))
        self.label_15.setText(_translate("Dialog", "Set here what you want to appear before your exercises"))
        self.pushButton_newconfig.setText(_translate("Dialog", "New Config"))
        self.pushButton_delete.setText(_translate("Dialog", "Delete"))
        self.label_20.setText(_translate("Dialog", "Set here what you want to appear after your exercises"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGenerate), _translate("Dialog", "Preamble-postamble"))
        self.label.setText(_translate("Dialog", "TeXamator can help you build multiple choices tests with AMC :"))
        self.label_siteweb_3.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"http://home.gna.org/auto-qcm/\"><span style=\" text-decoration: underline; color:#0000ff;\">http://home.gna.org/auto-qcm/</span></a></p></body></html>"))
        self.label_23.setText(_translate("Dialog", "For more information, especially on how to configure this tab and make AMC compatible with TeXamator, please visit :"))
        self.label_siteweb_2.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Noto Sans\'; font-size:9pt;\">https://github.com/alexisflesch/texamator</span></p></body></html>"))
        self.label_9.setText(_translate("Dialog", "Do you want to enable this feature ?"))
        self.radioButtonAMCYes.setText(_translate("Dialog", "Yes"))
        self.radioButtonAMCNo.setText(_translate("Dialog", "No"))
        self.label_21.setText(_translate("Dialog", "What is the name of the corresponding environment?"))
        self.lineEditAMCEnv.setText(_translate("Dialog", "qcm"))
        self.label_24.setText(_translate("Dialog", "When you will export your project, TeXamator will write the \\copygroup and \\shufflegroup stuff for you. TeXamator will replace a text of your choice with these LaTeX macros. This text should appear in at least one of your configs in the \"Preamble-postamble\" tab."))
        self.label_25.setText(_translate("Dialog", "What text do you want to use ? "))
        self.lineEditAMCText.setText(_translate("Dialog", "%AMC-stuff"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabAMC), _translate("Dialog", "AMC"))
from . import icones_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
