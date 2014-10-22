# File: bday.py
#
# Helen Chac, ECS 010, Fall 2012
#
# There needs to be at least 22 people in the room to have a probability of .5
# There needs to be at least 40 people in the room to have a probability of .9
#


# import random numbers for the simulation
import random

# hasduplicates() is a function that returns True if the list contains a duplicate
# returns False if function does not contain a duplicate
def hasduplicates(l):
    # loop the function by the length of the list
    for i in range (len(l)):
        # count the number of duplicates there are in the list
        count = l.count(l[i])
        # when the list becomes empty, return False
        if len(l) == 0:
            return False
        # if the list has a duplicate, return True
        elif count >= 2:
            return True
        # if there are no duplicates, continue the function, but split the first part of the list
        elif count == 1:
            return hasduplicates(l[1:])
        return hasduplicates(l)

def onetest(count):
# create random numbers which represents the days in a year for birthday
    l = []
    # l = empty list
    # create random birthdays for the number of people
    for i in range(count):
        # add number to list
        l.append(random.randint(1, 365))
    return hasduplicates(l)
    # run hasduplicates(l)
    # return True for every True in hasduplicates(l)
    if hasduplicate(l) == True:
        return True
    # return False for every False in hasduplicate(l)
    elif hasduplicates(l) == False:
        return False
    
def probab(count, num):
# count the number of duplicates there
    # use numofdup as a count
    numofdup = 0
    # loop the function in order to count the number of duplicates
    for i in range(num):
        if onetest(count) == True:
            numofdup += 1
    # find the average, which is numofdup divide by the num 
    return numofdup / num 
        
    
def main():
    # num is the number of tests run
    num = 5000
    # count is the number of people
    count = 2
    # continue running the program until the probability is .9
    while (float(probab(count, num)<=.9)):
        # return the probability into the variable probability
        probability = probab(count,num)
        print("For", count, "people, the probability of 2 birthdays is", probability)
        count = count + 1
        # keep adding 1 to the number of people until the while loop is met.

# run the function
main()
