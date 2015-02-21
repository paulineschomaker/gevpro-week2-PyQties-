#!/usr/bin/env python

import sys

# Dit is een Country-class, doet echt weinig stoers.
class Country():
    def __init__(self, country):
        self.country = country
    
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

if __name__ == '__main__':
    putYoCountriesInAList(countries_list.txt)
    print(country)
