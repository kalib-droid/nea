class Staff:
    rating=[]

    #rating=[1,2,3,4,5,6,7,8,9,10]
    def init(self, externRating):
        externRating = self.rating
    def StaffCountCalc(self, value): 
        #setting values as an empty list
        values = {}
        #values.append(str(value))
        for i in range(1, 11):
            #between the range of 1-10, checks if value is less than 10,then finds the value of i, multiplies by the range and matches with key value pair
            if i < 10:
                values[i] = i*50
            else:
                values['x'] = i*50

        #prints the key value pairs, showing which rating corresponds to which number
        #print(values)
        keys = list(values)
        for i, val in enumerate(values):
            #print(keys[i])
            if values[keys[i]] == values:
                return values(keys[i])

            elif (values[keys[i]] > values[keys[i-1]] )and (value < values[i+1]):
                return keys[i-1]

            else:
                if value >= values['x']:
                    return 10

