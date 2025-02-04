from customer import *
from GUI_ import *

rating=[1,2,3,4,5,6,7,8,9,10]


def ratingSystem(value):
    values_ = {}
    #values_.append(str(value))
    for i in range(1, 11):
        if i < 10:
            values_[i] = i*250000
        else:
            values_['x'] = i*250000

    #print(values_)
    keys = list(values_)
    for i, val in enumerate(values_):
        #print(keys[i])
        if values_[keys[i]] == values_:
            return values(keys[i])
        
        elif (value > values_[keys[i-1]] )and (value < values_[i+1]):
            return keys[i+1]
        
        else:
            if value >= values_['x']:
                return 10
            
print(ratingSystem(260000))
