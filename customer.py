import csv 
import random
import GUI_
import sys
import os

from arial_distance.arial_distance import get_distance

class customer: 
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
    

    def howManyCompanies(self,fileToOpen): 
        print(len(fileToOpen)) 
     
    def test_distance(self,x,y):
        # Write your test case here
        source = 52.575985, 1.136588 #netmatters wymondham coordinates
        destination = x, y
        print(get_distance(source, destination))
        #new = TestArialDistance() - code for when the class was TestArialDistance()
       # new.test_distance()
        
    
   


     

     