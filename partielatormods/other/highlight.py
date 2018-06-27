#!/usr/bin/python
#-*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui
import re



class MyHighlighter(QtGui.QSyntaxHighlighter):
    def __init__(self, edit):
        QtGui.QSyntaxHighlighter.__init__(self,edit)

    def highlightBlock(self, text):

        normalFormat = QtGui.QTextCharFormat()
        normalFormat.setForeground(QtCore.Qt.black)

        macroFormat = QtGui.QTextCharFormat()
        macroFormat.setFontWeight(QtGui.QFont.Bold)
        macroFormat.setForeground(QtCore.Qt.darkRed)
        macroMathFormat = QtGui.QTextCharFormat()
        macroMathFormat.setForeground(QtGui.QColor(140, 140, 100))
        macroPattern = "\\\\([a-zA-Z][a-zA-Z0-9]*|\W)"

        beginendFormat = QtGui.QTextCharFormat()
        beginendFormat.setFontWeight(QtGui.QFont.Bold)
        beginendFormat.setForeground(QtCore.Qt.red)
        beginendPattern = "(\\\\begin\{|\\\\end\{)"

        beginend2Format = QtGui.QTextCharFormat()
        beginend2Format.setFontWeight(QtGui.QFont.Bold)
        beginend2Format.setForeground(QtCore.Qt.blue)

        commentFormat = QtGui.QTextCharFormat()
        commentFormat.setForeground(QtCore.Qt.darkGray)
        commentFormat.setFontItalic(True)
        commentPattern = "%[^\n]*"

        mathFormat = QtGui.QTextCharFormat()
        mathFormat.setForeground(QtGui.QColor(90, 160, 90))
        mathPattern = "(\${1,2}"
        mathPattern += "|\\\\begin\{align\W*\}|\\\\end\{align\W*\}"
        mathPattern += "|\\\\begin\{equation\W*\}|\\\\end\{equation\W*\}"
        mathPattern += "|\\\\begin\{eqnarray\W*\}|\\\\end\{eqnarray\W*\}"
        mathPattern += "|\\\\\(|\\\\\)"
        mathPattern += "|\\\\\[|\\\\\])"
        #mathPattern = r"\\[|\\]"



        #Comment highlighting
        expression = QtCore.QRegExp(commentPattern)
        index = expression.indexIn(text)
        commentIndex = len(text)+1
        if (index >= 0):
            commentIndex = index
            self.setFormat(index, len(text)-index, commentFormat)

        #Math highlighting
        mathIndex = []
        #self.setCurrentBlockState(0)
        expression = QtCore.QRegExp(mathPattern)

        if (self.previousBlockState() != 1 ):
            startIndex = expression.indexIn(text)
            endIndex = expression.indexIn(text, startIndex+expression.matchedLength())
        else:
            endIndex = expression.indexIn(text, 0)
            startIndex = 0


        while (startIndex >= 0):
            if startIndex > commentIndex:
                break
            if (endIndex == -1):
                self.setCurrentBlockState(1)
                mathLength = len(text) - startIndex
            elif commentIndex < endIndex:
                self.setCurrentBlockState(1)
                mathLength = commentIndex - startIndex
            else:
                self.setCurrentBlockState(0)
                mathLength = endIndex - startIndex + expression.matchedLength()
            self.setFormat(startIndex, mathLength, mathFormat)
            mathIndex += list(range(startIndex,startIndex+mathLength))
            startIndex = expression.indexIn(text, startIndex + mathLength)
            endIndex = expression.indexIn(text, startIndex+1)


        #mathIndex = []
        #Macro highlight
        expression = QtCore.QRegExp(macroPattern)
        index = expression.indexIn(text)
        while (index >= 0):
            length = expression.matchedLength()
            if index > commentIndex:
                break
            if index in mathIndex:
                self.setFormat(index, length, macroMathFormat)
            else:
                self.setFormat(index, length, macroFormat)
            index = expression.indexIn(text, index + length)

        #Begin highlight
        expression = QtCore.QRegExp(beginendPattern)
        e2 = QtCore.QRegExp("\}")
        index = expression.indexIn(text)
        while (index >= 0):
            if index > commentIndex:
                break
            length = expression.matchedLength()
            i2 = e2.indexIn(text, index + length)
            self.setFormat(index, length-1, beginendFormat)
            self.setFormat(index+length-1, 1, normalFormat)
            if i2 > 0 and i2 < commentIndex:
                self.setFormat(index+length, i2-index-length, beginend2Format)
                self.setFormat(i2, 1, normalFormat)
            index = expression.indexIn(text, index + length)
