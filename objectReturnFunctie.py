#!/usr/bin/env python

import sys
from flag_color import *
from PyQt4 import QtCore, QtGui

# Dit is een Country-class, doet echt weinig stoers.
class Country():
    def __init__(self, country):
        self.country = country
        self.flagColor()
    
    def returnName(self):
        return self.country
    
    def returnColor(self):
        return self.color
        
    # Dit is de functie die de kleur bepaalt    
    def flagColor(self):
         self.color = FlagColor()
    
    def __str__(self):
        return self.country
        
# Dit is de functie die lijsten van Country's maakt (countryList)
def countriesFileToList (countryFile):
    infile = open(countryFile, "r")
    countryList = []
    
    for line in infile:
        newCountry = Country(line.strip()) #haha, Country(line)dancing.
        countryList.append(newCountry)
    
    return countryList

def main():
    country = countriesFileToList("countries_list.txt")
    print(country)
         
if __name__ == '__main__':
	main()
    
