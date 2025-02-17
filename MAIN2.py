from StaffCountCalc import *
from TurnoverCalc import *
from DistanceCalc import *
from SalesCalc import * 
#main method for function calls!
x = Staff()
print(x.StaffCountCalc(100))#StaffCountCalc is function Staff is class

y = Turnover()
print(y.TurnoverCalc(2500000))#TurnoverCalc is function Turnover is class

z = DistanceCalc()
print(z.test_distance(52.2517169,0.7125594))#test_distance is function DistanceCalc is class

a = Sales()
print(a.SalesCalc(250000))#SalesCalc is function  Sales is class