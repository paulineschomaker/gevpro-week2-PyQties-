import sys
from random import randrange
from PyQt4 import QtCore, QtGui

class FlagColor(QtGui.QColor):
    def __init__(self):
        super().__init__()
        self.setBlue(randrange(0,255))
        self.setGreen(randrange(0,255))
        self.setRed(randrange(0,255))
       


