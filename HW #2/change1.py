# File: change1.py
# makes change in the correct plural words
#
# Helen Chac, ECS 10, Fall 2012
#

# set up the loop
go_on = "yes"

while go_on == "yes":

    # c is change that the user is inputting
    c = input("How many cents do you want me to make change for? ")
    # change(the variable) is used to divide the change by the cent amount
    # pchange is used to store the number for when we print it
    change = pchange = int(c)

    # divide by the amount of a quarter (25 cents)
    nquarters = change // 25
    change %= 25

    # if the amount of quarters is 1, then it is a quarter
    if nquarters == 1:
        print (pchange, "cents is", nquarters, "quarter,", end = ' ')
    # if the amount of quarters is anything but 1, then change it to quarters
    else:
        print (pchange, "cents is", nquarters, "quarters,", end = ' ') 

    # divide the current amount by 10 cents for dimes
    ndimes = change // 10
    change %= 10

    # if the amount of dimes is 1, print dime
    if ndimes == 1:
        print (ndimes, "dime,", end = ' ' )
    # if the amount of dimes is not 1, then print dimes
    else:
        print (ndimes, "dimes,", end = ' ')

    # divide the current amount by 5 cents for nickels
    nnickels = change // 5

    #if the amount of nickels is 1, then print nickel
    if nnickels == 1:
        print (nnickels, "nickel,", end = ' ')
    # if the amount of nickels is not 1, then print nickels
    else:
        print (nnickels, "nickels,", end = ' ')

    # the leftover pennies
    npennies = change % 5

    # if the amount of pennies are 1, then print penny
    if npennies == 1:
        print ("and", npennies, "penny.")
    # if the amount of pennies is not 1, then print pennies
    else:
        print ("and", npennies, "pennies.")

    # do another one again?    
    go_on = input("Again ('yes' for yes, anything else to stop): ")
