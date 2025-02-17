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
    
    def saveTwoDlistToCSVFile(filename, externList):
        myFile = open(fileName, "w")
        for keyword in externList:
            counter = 0
            lineToWrite=""
            while counter < len(keyword)-1:
                lineToWrite = lineToWrite+keyword[counter]+ ","
                counter = counter+1
            lineToWrite = lineToWrite + keyword[len(keyword)-1] + "\n"
            myFile.write(lineToWrite)
        myFile.close()
        def howManyCompanies(self,fileToOpen): 
            print(len(fileToOpen)) 
    def print2DListWithoutTheCrap(listToPrint):
        column = 0
        while column < len(keywords):
            row=0
            lineToPrint = ""
            while row < len(keywords[column]):
                lineToPrint = lineToPrint + keywords[column][row] + " "
                row = row + 1
            column = column + 1
            print(lineToPrint)


    def openFileInto2DList(fileName):
        myFile = open("myText.txt" , "r")
        keywords= []
        for line in myFile:
            line = line.strip("\n")
            keywordsAndDefinition = line.split(",")
            keywords.append(keywordsAndDefinition)
        myFile.close()
        return keywords
        keywords = openFileInto2DList("myText")
        print2DListWithoutTheCrap(keywords)
    
        
    
   


     

     