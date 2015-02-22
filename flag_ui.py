# This is where the magic shall happen :3

#!/usr/bin/env python

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from objectReturnFunctie import *
from flag_color import *
import sys

class CountryWindow(QDialog):
    def __init__(self):
        QWidget.__init__(self)
        self.countriesFile = "countries_list.txt"
        self.countriesList = countriesFileToStr(self.countriesFile)
 
        # UI #
        #Combobobox
        self.countryPicker = QtGui.QComboBox(self)
        self.countryPicker.addItems(self.countriesList)
        self.countryPicker.currentIndexChanged.connect(self.updateUI)
        
        #QFrame
        self.countryFrame = QtGui.QFrame(self)
        self.countryFrame.setGeometry(250,50,50,25)
        self.countryFrame.move(10,50)
        
        #Color
        self.Color = QtGui.QColor(200,5,20)
        
        # Grid #
        self.setGeometry(500, 200, 300, 300)
        self.setWindowTitle('Raampje')
        self.show()
        
        #Update
    def updateUI(self):
        self.Color = FlagColor()
        self.countryFrame.setStyleSheet("QFrame { background-color: %s }" % self.Color.name())
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = CountryWindow()
    app.exec()