from arial_distance.arial_distance import get_distance
import sys
import os
class DistanceCalc:
        def __init__(self):
                pass
        def test_distance(self,x,y):
                source = 52.575985, 1.136588 #netmatters wymondham coordinates
                destination = x, y
                print(get_distance(source, destination))
                #new = TestArialDistance() - code for when the class was TestArialDistance()
                #new.test_distance()
                        

        #print(test_distance(52.2517169,0.7125594))
        #new = TestArialDistance() 
                #print(test_distance(52.2517169,0.7125594))