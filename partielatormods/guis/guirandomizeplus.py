#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from random import shuffle

def close(self, res):
    #If user clicked Ok :
    if res:
        #Depending on what radioButton was selected, set parent.
        if self.ui_random.radioButton_selected_folder.isChecked():
            parent = self.treeWidget.topLevelItem(0)
            if not parent: #If user didn't click on "look for exercises"
                print "Look for exercises before !!!"
                return
            if not self.treeWidget.currentItem(): #If treeWidget has never been clicked
                print "You did not select a folder : picking exercises in the entire database"
            else:
                parent = self.treeWidget.currentItem()
            if (parent.childCount() == 0): #If an exercise is selected, use its parent instead
                parent = parent.parent()
        else:
            parent = self.treeWidget.topLevelItem(0)
        #List the exercises under the item        
        l = self.list_child_exercises(parent, [])
        #Is there enough exercises ?
        n = self.ui_random.spinBox.value()
        if n>len(l):
            print "not enough exercises"
            n = len(l)
        shuffle(l)
        l = l[:n]
        for exo in l:
            item = QtGui.QListWidgetItem(self.listWidget)
            nom = exo["titre"]
            item.enonce = exo["enonce"]
            item.setText(QtGui.QApplication.translate("Form", str(nom), None,\
                            QtGui.QApplication.UnicodeUTF8))
        if l:
            self.pushButton_preview.setEnabled(True)
            self.actionEdit_exercise.setEnabled(True)
            self.pushButton_edit.setEnabled(True)
            self.listWidget.setCurrentItem(item)
