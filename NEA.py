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
                openFile = open(fileToOpen, "w") 
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
     
    def distanceMatrix(client, origins, destinations,
                mode=None, language=None, avoid=None, units=None,
                departure_time=None, arrival_time=None, transit_mode=None,
                transit_routing_preference=None, traffic_model=None, region=None):
        
            
        
        params = {
                "origins": convert.location_list(origins),
                "destinations": convert.location_list(destinations)
            }

        if mode:
            
                # NOTE(broady): the mode parameter is not validated by the Maps API
                # server. Check here to prevent silent failures.
            if mode not in ["driving", "walking", "bicycling", "transit"]:
                raise ValueError("Invalid travel mode.")
            params["mode"] = mode

        if language:
            params["language"] = language

        if avoid:
            if avoid not in ["tolls", "highways", "ferries"]:
                raise ValueError("Invalid route restriction.")
            params["avoid"] = avoid

        if units:
            params["units"] = units

        if departure_time:
            params["departure_time"] = convert.time(departure_time)

        if arrival_time:
            params["arrival_time"] = convert.time(arrival_time)

        if departure_time and arrival_time:
            raise ValueError("Should not specify both departure_time and"
                             "arrival_time.")

        if transit_mode:
            params["transit_mode"] = convert.join_list("|", transit_mode)

        if transit_routing_preference:
            params["transit_routing_preference"] = transit_routing_preference

        if traffic_model:
            params["traffic_model"] = traffic_model

        if region:
            params["region"] = region

        return client._request("/maps/api/distancematrix/json", params)        

    
    
    def report(self, CompanyName): 
        print("Target Market Group Report: \n") 
        print(str(CompanyName) + ", the company group you should be targeting the most is ___, as they have a score of 12, and will be best suited for your business") 
        print("-The next company groups you should target are, ___, ___, ___\nas they have scores 11,10 and 9 respectively.\n") 
        print("-The companies with moderately good profitability are, ___, ___, ___\nas they have scores 8,7 and 6 respectively.\n") 
        print("-The final company group to target are __, they have a score of 5.\n") 
        print("-Company groups to avoid are those below a score of 5, such as ___,___,___ and ___.\n") 
        print("") 

     