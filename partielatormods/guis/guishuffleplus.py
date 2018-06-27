#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui
from random import shuffle

def close(self, res):
    #If user clicked Ok :
    if res:
        #Depending on what radioButton was selected, create a list with the exercises to be shuffled.
        if self.ui_shuffle.radioButton_selected_elements.isChecked():
            itemsList = [item for item in self.tableWidget.selectedItems() \
                           if not self.tableWidget.column(item)]
            fullList = []
        else:
            itemsList = []
            for i in range(self.tableWidget.rowCount()):
                itemsList.append(self.tableWidget.item(i,0))
            fullList = itemsList
        #Create a list with all the items from the tableWidget
        if not fullList:
            for i in range(self.tableWidget.rowCount()):
                fullList.append(self.tableWidget.item(i,0))
        self.shuffleTable(itemsList, fullList)


def shuffleFromContext(self):
    """When shuffling from context menu, we want to shuffle the selected
       items without showing the dialog"""
    itemsList = [item for item in self.tableWidget.selectedItems() \
                           if not self.tableWidget.column(item)]
    fullList = []
    for i in range(self.tableWidget.rowCount()):
        fullList.append(self.tableWidget.item(i,0))
    self.shuffleTable(itemsList, fullList)


def shuffleTable(self, itemsList, fullList):
    #Find the indexes of the items to be shuffled
    indexes = [self.tableWidget.row(item) for item in itemsList]
    #Copy the list of indexes and shuffle it
    shuffled_indexes = list(indexes)
    shuffle(shuffled_indexes)
    if self.settings['AMC']=='True':
        fullElementsList = []
        for i in range(self.tableWidget.rowCount()):
            fullElementsList.append(self.tableWidget.item(i,1))
        ElementsList = []
        for i in indexes:
            self.tableWidget.takeItem(i,0)
            ElementsList.append(self.tableWidget.takeItem(i,1))
        for i in range(len(indexes)):
            self.tableWidget.setItem(indexes[i],0,fullList[shuffled_indexes[i]])
            self.tableWidget.setItem(indexes[i],1,fullElementsList[shuffled_indexes[i]])
    else:
        for i in indexes:
            self.tableWidget.takeItem(i,0)
        for i in range(len(indexes)):
            self.tableWidget.setItem(indexes[i],0,fullList[shuffled_indexes[i]])