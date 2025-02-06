class Sales():


    
    rating=[1,2,3,4,5,6,7,8,9,10]
    
    def __init(self,externRating):
        externRating = rating 

    def SalesCalc(value):
        #setting values as an empty list
        values_ = {}
        #values_.append(str(value))
        for i in range(1, 11):
            #between the range of 1-10, checks if value is less than 10,then finds the value of i, multiplies by the range and matches with key value pair
            if i < 10:
                values_[i] = i*25000
            else:
                values_['x'] = i*25000

        #prints the key value pairs, showing which rating corresponds to which number
        print(values_)
        keys = list(values_)
        for i, val in enumerate(values_):
            #print(keys[i])
            if values_[keys[i]] == values_:
                return values(keys[i])
            
            elif (values_[keys[i]] > values_[keys[i-1]] )and (value < values_[i+1]):
                return keys[i-1]
            
            else:
                if value >= values_['x']:
                    return 10
                
    print(SalesCalc(150000))