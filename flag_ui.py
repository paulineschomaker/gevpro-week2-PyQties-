# This is where the magic shall happen :3

#!/usr/bin/env python

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from objectReturnFunctie import *
from flag_color import *
import sys

class CountryWindow(QDialog):
    def __init__(self):
        """Maakt een Interface aan met Combobox en QFrame"""
        QWidget.__init__(self)
        self.countriesFile = "countries_list.txt"
        self.countriesList = countriesFileToList(self.countriesFile)
        self.countriesList2 = countriesFileToList(self.countriesFile)
        self.countriesList3 = countriesFileToList(self.countriesFile)
 
        # UI #
        #Combobobox
        self.countryPicker = QtGui.QComboBox(self)
        self.countryPicker.move(40,20)
        for thisCountry in self.countriesList:
            self.countryPicker.addItem(thisCountry.country)
        self.countryPicker.currentIndexChanged.connect(self.updateUI)
        
        #QFrame bovenste balk vlag
        self.countryFrame = QtGui.QFrame(self)
        self.countryFrame.setGeometry(250,50,120,30)
        self.countryFrame.move(90,70)
        
        #QFrame middelste balk vlag
        self.countryFrame2 = QtGui.QFrame(self)
        self.countryFrame2.setGeometry(250,50,120,30)
        self.countryFrame2.move(90,100)
        
        #QFrame onderste balk vlag
        self.countryFrame3 = QtGui.QFrame(self)
        self.countryFrame3.setGeometry(250,50,120,30)
        self.countryFrame3.move(90,130)
        
        #Window
        self.setGeometry(500, 200, 300, 300)
        self.setWindowTitle('Country')
        self.show()
        
        #Update
    def updateUI(self):
        """Deze functie zoekt de kleuren die bij het land horen en stelt de kleur in"""
        newCountry = self.countryPicker.currentText()
        for findCountry in self.countriesList:     #bovenste balk
            if (findCountry.country == newCountry):
                self.countryFrame.setStyleSheet("QFrame { background-color: %s }" % findCountry.color.name())
        newCountry2 = self.countryPicker.currentText() #middelste balk
        for findCountry in self.countriesList2:
            if (findCountry.country == newCountry2):        
                self.countryFrame2.setStyleSheet("QFrame { background-color: %s }" % findCountry.color.name())
        newCountry3 = self.countryPicker.currentText() #onderste balk
        for findCountry in self.countriesList3:
            if (findCountry.country == newCountry3):        
                self.countryFrame3.setStyleSheet("QFrame { background-color: %s }" % findCountry.color.name())
				
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = CountryWindow()
    app.exec()
