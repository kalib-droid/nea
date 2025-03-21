from GUI_ import * 
from DBreal import *
from TurnoverCalc import *
from SalesCalc import * 
from DistanceCalc import *
from StaffCountCalc import *

class analysis():
    customerID = 0 
    SICcodes = 0 
    postcode = "" 
    lat = 0
    long_ = 0
    turnover_override = 0
    turnover = 0
    estimatedTurnover = 0 
    total_sales = "" 
    profit= 0 
    staff_count = 0

    def __init__(self, externCustomerID, externSICcodes,externLat, externLong,externTurnoverOverride,externTurnover,externEstimatedTurnover,externTotalSales,externStaffCount,externProfit): 
        self.customerID = externCustomerID
        self.SICcodes = externSICcodes 
        self.lat = externLat 
        self.long_ = externLong 
        self.turnover_override = externTurnoverOverride
        self.turnover = externTurnover 
        self.estimatedTurnover = externEstimatedTurnover 
        self.total_sales = externTotalSales
        self.staff_count = externStaffCount
        self.profit = externProfit
        
    def getRating(self):
        return self.rating
    def setRating(self, rating):
        self, rating = self.rating  
  
       
    def getCustomerID(self):
        return self.customerID

    def getSICcodes(self):
        return self.SICcodes

    def getPostcode(self):
        return self.postcode

    def getLat(self):
        return self.lat

    def getLong(self):
        return self.long_

    def getTurnoverOverride(self):
        return self.turnover_override

    def getTurnover(self):
        return self.turnover

    def getEstimatedTurnover(self):
        return self.estimatedTurnover

    def getTotalSales(self):
        return self.total_sales

    def getProfit(self):
        return self.profit

    def getStaffCount(self):
        return self.staff_count 

  
    def setCustomerID(self, customerID):
        self, customerID = self.customerID

    def setSICcodes(self, SICcodes):
        self,SICcodes = self.SICcodes

    def setPostcode(self, postcode):
        self,postcode = self.postcode

    def setLat(self, lat):
        self,lat = self.lat

    def setLong(self, long_):
        self,long_ = self.long_

    def setTurnoverOverride(self, turnover_override):
        self,turnover_override = self.turnover_override

    def setTurnover(self, turnover):
        self,turnover = self.turnover

    def setEstimatedTurnover(self, estimatedTurnover):
        self,estimatedTurnover = self.estimatedTurnover

    def setTotalSales(self, total_sales):
        self,total_sales = self.total_sales

    def setProfit(self, profit):
        self,profit = self.profit

    def setStaffCount(self, staff_count):
        self, staff_count = self.staff_count    

    
    def functionCall(self,parameter):
        pass
        for i, column in enumerate(parameter):
            if i == 2 or i ==3:
                lat = x
                long_ = y
            elif i == 4:
                self.SalesCalc(total_sales)
            elif i == 5 and turnover_override != None
                self.TurnoverCalc(parameter)
                


        
    
