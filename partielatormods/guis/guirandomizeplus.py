#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from random import shuffle

def close(self, res):
    #If user clicked Ok :
    if res:
        #Depending on what radioButton was selected, set parent.
        if self.ui_random.radioButton_selected_folder.isChecked():
            itemsList = [self.treeWidget.topLevelItem(0)]
            if not itemsList: #If user didn't click on "look for exercises"
                print "Look for exercises before !!!"
                return
            if not self.treeWidget.selectedItems(): #If treeWidget has never been clicked
                print "You did not select a folder : picking exercises in the entire database"
            else:
                itemsList = self.treeWidget.selectedItems()
        else:
            itemsList = [self.treeWidget.topLevelItem(0)]
        #List the exercises under the items
        leaves = []
        for i in itemsList:
            leaves += self.list_children(i, [])
        #Is there enough exercises ?
        n = self.ui_random.spinBox.value()
        if n>len(leaves):
            print "not enough exercises"
            n = len(leaves)
        shuffle(leaves)
        leaves = leaves[:n]
        self.tableWidget.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.tableWidget.selectionModel().clearSelection()
        for exercise in leaves:
            self.add_items(exercise)
        self.tableWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        if leaves:
            self.tableWidget.emit(QtCore.SIGNAL("notempty()"))
