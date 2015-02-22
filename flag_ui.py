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
        self.setWindowTitle('Window thing')
        self.countriesFile = "countries_list.txt"
        self.countriesList = countriesFileToStr(self.countriesFile)
 
        # UI #
        self.countryPicker = QComboBox()
        self.countryPicker.addItems(self.countriesList)
        
        # Grid #
        grid = QGridLayout()
        grid.addWidget(self.countryPicker, 0, 0)
        self.setLayout(grid)
        
        # Change on updates #
        #self.connect(self.fromCurrencyCombo, SIGNAL("currentIndexChanged(int)"), self.updateUI)
        #self.connect(self.toCurrencyCombo, SIGNAL("currentIndexChanged(int)"), self.updateUI)
        #self.connect(self.fromCurrencySpin, SIGNAL("valueChanged(double)"), self.updateUI)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    converter = CountryWindow()
    converter.show()
    app.exec()
