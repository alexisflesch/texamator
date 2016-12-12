#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from random import shuffle

def close(self, res):
    #If user clicked Ok :
    if res:
        #Depending on what radioButton was selected, create a list with the exercises to be shuffled.
        if self.ui_shuffle.radioButton_selected_elements.isChecked():
            itemsList = self.tableWidget.selectedItems()
            fullList = []
        else:
            itemsList = []
            for i in range(self.tableWidget.rowCount()):
                itemsList.append(self.tableWidget.item(0,i))
            fullList = itemsList
        #Create a list with all the items from the tableWidget
        if not fullList:
            for i in range(self.tableWidget.rowCount()):
                fullList.append(self.tableWidget.item(0,i))
        shuffleTable(itemsList, fullList, self.tableWidget)


def shuffleFromContext(tableWidget):
    """When shuffling from context menu, we want to shuffle the selected
       items without showing the dialog"""
    itemsList = tableWidget.selectedItems()
    fullList = []
    for i in range(tableWidget.rowCount()):
        fullList.append(tableWidget.item(0,i))
    shuffleTable(itemsList, fullList, tableWidget)


def shuffleTable(itemsList, fullList, tableWidget):
    #Find the indexes of the items to be shuffled
    indexes = [tableWidget.row(item) for item in itemsList]
    #Copy the list of indexes and shuffle it
    shuffled_indexes = list(indexes)
    shuffle(shuffled_indexes)
    for i in indexes:
        tableWidget.takeItem(i,0)
    for i in range(len(indexes)):
        tableWidget.setItem(indexes[i],0,fullList[shuffled_indexes[i]])
        