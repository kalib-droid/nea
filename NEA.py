import csv 
import random
import googlemaps
from googlemaps import convert

class customer(): 
    companyName = "" 
    regNumber = 0 
    SICcodes = 0 
    address = "" 
    turnover = 0 
    turnoverPeriod = "" 
    salesInPeriod = 0 
    salesPeriod = "" 
    profit= 0 

    def __init__(self, externCompanyName, externRegNumber, externSICcodes, externAddress,externTurnoverPeriod,externTurnoverInPeriod,externSalesInPeriod,externSalesPeriod,externProfit): 
        companyName = externCompanyName 
        regNumber = externRegNumber 
        SICcodes = externSICcodes 
        address = externAddress 
        turnoverPeriod = externTurnoverPeriod
        turnoverPeriod = externTurnoverPeriod 
        salesInPeriod = externSalesInPeriod 
        salesPeriod = externSalesInPeriod 
        profit = externProfit 
    def openFile(self): 
        fileToOpen = input("What file would you like to open?") 
        while True: 
            try: 
                openFile = open(fileToOpen, "r") 
                array = [] 
                for line in openFile: 
                            line = line.strip("\n") 
                            lineSplit = line.split(" ") 
                            array.append(lineSplit) 
                openFile.close() 
                return array 
            except IOError as e: 
                #print("Could not find file :" + fileToOpen + " . Perhaps you forgot your file extension") 
                pass
 

    def howManyCompanies(self,fileToOpen): 
        print(len(fileToOpen)) 
     
    
    def report(self, CompanyName): 
        print("Target Market Group Report: \n") 
        print(str(CompanyName) + ", the company group you should be targeting the most is ___, as they have a score of 12, and will be best suited for your business") 
        print("-The next company groups you should target are, ___, ___, ___\nas they have scores 11,10 and 9 respectively.\n") 
        print("-The companies with moderately good profitability are, ___, ___, ___\nas they have scores 8,7 and 6 respectively.\n") 
        print("-The final company group to target are __, they have a score of 5.\n") 
        print("-Company groups to avoid are those below a score of 5, such as ___,___,___ and ___.\n") 
        print("") 

     