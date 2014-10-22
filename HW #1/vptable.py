# File: vptable.py
# print a table in intervals of 5 from -20 to 50 with temperature on the left side and vapor pressure on the right
#
# Helen Chac, ECS 10, Fall 2012
#

import math

#
# Setting up the top of the table
# temp is for temperature, and pressure is for vapor pressure
# ----'s to seperate the numbers and what it is
#

print("temp\tpressure")
print("----\t--------")

# converts the temperature into vapor pressure and stores it in vp(i) for every i

def vp(i):
    return(6.112*(math.exp((17.67*i)/(i+243.5))))

# i is temperature
# range is numbers in intervals of 5 between -20 and 50

for i in range(-20, 51, 5):
    print("%3d\t%6.2f" % (i , vp(i)))
