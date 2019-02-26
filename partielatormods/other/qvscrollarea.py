from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt


class QVScrollArea(QtWidgets.QScrollArea):
    """ A vertical scroll area that never needs a horizontal scrollbar.
        https://forum.qt.io/topic/13374/solved-qscrollarea-vertical-scroll-only/8
    """
    def __init__(self, parent=None, fun=lambda:None):
        super(QVScrollArea, self).__init__()
        
        #Scrollbars and such
        self.setWidgetResizable(True)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        #Timer to not throw resizeEvents too often
        self.delayTimeout = 100
        self._resizeTimer = QtCore.QTimer(self)
        self._resizeTimer.timeout.connect(self._delayedUpdate)
    
    def resizeEvent(self, event):
        self._resizeTimer.start(self.delayTimeout)
        return super(QVScrollArea, self).resizeEvent(event)
    
    def _delayedUpdate(self):
        self._resizeTimer.stop()
        self.fun()