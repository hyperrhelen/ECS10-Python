# File: collatz.py
# to find the shopping time of a number
#
# Helen Chac, ECS 10, Fall 2012
#

# def the function collatz
def collatz(n):
    count = 0  
    # stop looping when n is 1
    while (n!=1):
        
        if (n%2==0): # when n is even
            n = n /2

        else: 
            n = 3*n+1 # when n is odd
        print (int(n), end = ' ') # prints integer and doesn't return to the next line
        count = count+1 # counts every iteration made 
    return count

def main():
    # ask user for input
    n = int (input ("To find the stopping time of a number, enter a number:"))
    print (n, end = ' ')
    count = collatz(n)
    # \n returns a to the next line
    print ("\nThe total stopping time for", n, "is", count)

# call and run main function which is defined above
main()
