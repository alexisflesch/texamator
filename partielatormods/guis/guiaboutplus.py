#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui


def updateUi(ui):
    ui.label.setText(QtGui.QApplication.translate("Dialog", "TeXamator v2.4", None, QtGui.QApplication.UnicodeUTF8))
