# File: ftoc.py
# Fix the two problems that made the error message
#
# Helen Chac, ECS 10, Fall 2012
#

# Add float to be able to get float before input to get floating numbers
# Don't want to get rid of the decimals with 5//9
# Use 5/9 instead to get real decimal values
#

ftemp = float( input ("Enter degrees here in Fahrenheit: "))
ctemp = (5 / 9) * (ftemp - 32)
print (ftemp, "degrees Fahrenheit is", ctemp, "degrees centigrade.")

