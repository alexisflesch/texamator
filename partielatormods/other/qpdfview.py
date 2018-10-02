#!/usr/bin/env python3

"""Inspired from :
https://github.com/akkana/scripts/blob/master/qpdfview.py
"""

from PyQt5.QtWidgets import QWidget, QApplication, QShortcut, \
     QLabel, QScrollArea, QSizePolicy, QVBoxLayout
from PyQt5.QtGui import QPainter, QColor, QFont, QPixmap
from PyQt5.QtCore import Qt, QPoint, QSize, QUrl, QByteArray
from PyQt5.QtNetwork import QNetworkAccessManager, \
     QNetworkReply, QNetworkRequest
from PyQt5 import QtCore, QtGui, QtWidgets

from popplerqt5 import Poppler



class DelayedUpdater(QtWidgets.QWidget):
    #https://stackoverflow.com/questions/13552345/how-to-disable-multiple-auto-redrawing-at-resizing-widgets-in-pyqt
    def __init__(self, fun=None):
        super(DelayedUpdater, self).__init__()
        self.fun = fun
        self.delayTimeout = 100
        self._resizeTimer = QtCore.QTimer(self)
        self._resizeTimer.timeout.connect(self._delayedUpdate)

    def resizeEvent(self, event):
        self._resizeTimer.start(self.delayTimeout)
        return super(DelayedUpdater, self).resizeEvent(event)

    def _delayedUpdate(self):
        self._resizeTimer.stop()
        self.fun()


class myQWidget(QtWidgets.QWidget):
    """Sub-class of QWidget that emits a signal when resized"""
    resized = QtCore.pyqtSignal()
    def  __init__(self, parent=None):
        super(myQWidget, self).__init__(parent=parent)

    def resizeEvent(self, event):
        self.resized.emit()
        return super(myQWidget, self).resizeEvent(event)



class PDFWidget(QVBoxLayout):
    """QVBoxLayout subclass to show the pages of a pdf"""
    def __init__(self, filename, dpi=72, parent=None, width=300):
        super(PDFWidget, self).__init__(parent)
        #Getting rid of margins
        self.setContentsMargins(0, 0, 0, 0)
        self.setSpacing(0)
        #Keeping widths somewhere
        self.parentWidth = width
        self.dpi = dpi
        
        #Rendering
        if filename is not None:
            self.document = Poppler.Document.load(filename)
            if self.document is not None:
                self.document.setRenderHint(Poppler.Document.TextAntialiasing)
        else:
            self.document = None
        self.render()

    def render(self):
        if not self.document:
            return

        self.pages = [self.document.page(i) for i in range(self.document.numPages())]
        self.pagesize = self.pages[0].pageSize()
        self.pagewidth = self.pagesize.width()
        frac = self.parentWidth/self.pagewidth
        dpi = self.dpi*frac
            
        for page in self.pages:
            img = page.renderToImage(dpi, dpi)
            pixmap = QPixmap.fromImage(img)
            foo = QLabel()
            foo.setPixmap(pixmap)
            self.addWidget(foo)
            self.setAlignment(foo, QtCore.Qt.AlignCenter)
    
    def clearLayout(layout):
        """Function to clear self (which is a layout) of all its child widgets"""
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        
    
    def repaint(self, width=1):
        """ Force repaint (to be used when size of container has changed)
            - Checks first that document exists and that the size needs to be updated
            - creates Qlabels containing new images
            - clears old layout
            - immediatly fills it back with the images
        """
        #Check that document exists and that the size of the container has changed
        if not self.document or self.parentWidth==width:
            return
        
        #Keep track of new width for later
        self.parentWidth = width
        
        #Create new QLabels
        frac = width/self.pagewidth
        dpi = self.dpi*frac
        foo = []
        for page in self.pages:
            img = page.renderToImage(dpi, dpi)
            pixmap = QPixmap.fromImage(img)
            foo.append(QLabel())
            foo[-1].setPixmap(pixmap)
        
        #Clean old layout
        self.clearLayout()
        
        #add new QLabels to self (which is a layout)
        for f in foo:
            self.addWidget(f)
            self.setAlignment(f, QtCore.Qt.AlignCenter)

    
    def createPdf(self, filename):
        """Creates a new layout with a new pdf"""
        self.clearLayout()
        self.document = Poppler.Document.load(filename)
        if self.document is not None:
            self.document.setRenderHint(Poppler.Document.TextAntialiasing)
        self.render()
