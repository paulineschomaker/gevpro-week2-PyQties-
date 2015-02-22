#!/usr/bin/env python

import sys
from flag_color import *
from PyQt4 import QtCore, QtGui

# Dit is een Country-class, doet echt weinig stoers.
class Country():
    def __init__(self, country, countryFile):
        self.country = country
        self.countryFile = countryFile
    
    def __str__(self):
        return self.country
        
# Dit is de functie die lijsten van Country's maakt (countryList)
    def putYoCountriesInAList(countryFile):
        infile = open(countryFile, "r")
        countryList = []
	    
        for line in infile:
            newCountry = Country(line) #haha, Country(line)dancing.
            countryList.append(newCountry)
            return countryList
            
# Dit is de functie die de kleur bepaalt    
    def flagColor():
         color = flag_color()
      
def main():
    country = Country("Landje", "countries_list.txt") 
    print(country)
         
if __name__ == '__main__':
	main()
    
