import sys
import os

from arial_distance.arial_distance import get_distance
# from arial_distance import arial_distance

class TestArialDistance:
    def test_distance(self,x,y):
        # Write your test case here
        source = 52.575985, 1.136588 #netmatters wymondham coordinates
        destination = x, y
        print(get_distance(source, destination))
        
        
new = TestArialDistance()
new.test_distance()