# File: vp.py
# Convert the temperature into vapor pressure
#
# Helen Chac, ECS 10, Fall 2012
#

import math

# Ask user to input the temperature

t = float(input("Enter temperature in degrees C: "))

# define vp : convert the input temperature to vapor presssure.
# "%.2f" % rounds up to two decimal places
def vp(t):
    return( "%.2f" %(6.112*(math.exp((17.67*t)/(t+243.5)))))

# This prints "At this temperature, the vapor pressure is,(vp), millibars."
def main():
    print("At this temperature, the vapor pressure is " + vp(t), "millibars.")

main()
