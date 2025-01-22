#values = [10000,100000,500000,750000,1250000,2500000,10000000]
rating=[1,2,3,4,5,6,7,8,9,10]
#x = 250000
#counter = 0
#while str(values) <= str(x):
#        print(values)
#        rating = str(rating[counter])
#        x = x + 250000
#        counter = counter +1
#print(x)8

def ratingSystem(value):
    values_ = {}
    for i in range(1, 11):
        if i < 10:
            values_[i] = i*250000
        else:
            values_['x'] = i*250000

    for i, val in enumerate(values_):
        if value == val[1]:
            return val[0]
        
        elif (value > val[0]) and (value < values_[i+1]):
            return val[0]
        
        else:
            if value >= values_['x']:
                return 10
            else:
                return values_[i+1]




ratingSystem(350000)
    