#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from . import guiexportamc


def updateUi(self, ui_AMC, elementsList):
    """add what's missing"""
    horizontalLayouts = []
    self.spinBoxes = []
    elementsList = [i for i in elementsList if i]
    for i in elementsList:
        label = QtWidgets.QLabel()
        label.setText(i)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.spinBoxes.append(QtWidgets.QSpinBox())
        self.spinBoxes[-1].setProperty("value", 1)
        horizontalLayouts.append(QtWidgets.QHBoxLayout())
        horizontalLayouts[-1].addWidget(label)
        horizontalLayouts[-1].addItem(spacerItem)
        horizontalLayouts[-1].addWidget(self.spinBoxes[-1])
        ui_AMC.verticalLayout.addLayout(horizontalLayouts[-1])

def createAMCMacros(self, elementsList, spinBoxes):
    """write AMC Macros"""
    texte = r'\cleargroup{everything}'
    texte += '\n'
    elementsList = [i for i in elementsList if i]
    for i in range(len(elementsList)):
        if spinBoxes[i].value():
            texte += r'\shufflegroup{'
            texte += elementsList[i]
            texte += r'}'
            texte += r'\copygroup['
            texte += str(spinBoxes[i].value())
            texte += r']{'
            texte += elementsList[i]
            texte += r'}{everything}'
            texte += '\n'
    texte += '\n'
    texte += r'\shufflegroup{everything}'
    texte += '\n'
    texte += r'\insertgroup{everything}'
    texte += '\n'
    texte += r'\clearpage'
    texte += '\n'
    self.AMC_texte = texte