from NEA import*
import googlemaps
from googlemaps import convert


class analysis():
    companyName = "" 
    regNumber = 0 
    SICcodes = 0 
    address = "" 
    turnover = 0 
    turnoverPeriod = "" 
    salesInPeriod = 0 
    salesPeriod = "" 
    profit= 0 

    def __init__(self, externCompanyName, externRegNumber, externSICcodes, externAddress,externTurnover,externTurnoverInPeriod,externSalesInPeriod,externSalesPeriod,externProfit): 
        self.companyName = externCompanyName 
        self.regNumber = externRegNumber 
        self.SICcodes = externSICcodes 
        self.address = externAddress 
        self.turnover = externTurnover 
        self.turnoverPeriod = externTurnoverPeriod 
        self.salesInPeriod = externSalesInPeriod 
        self.salesPeriod = externSalesInPeriod 
        self.profit = externProfit
        
        def distanceMatrix(client, origins, destinations,
                    mode=None, language=None, avoid=None, units=None,
                    departure_time=None, arrival_time=None, transit_mode=None,
                    transit_routing_preference=None, traffic_model=None, region=None):
            
            return client._request("/maps/api/distancematrix/json", params)
        
            
            
            
        
    
