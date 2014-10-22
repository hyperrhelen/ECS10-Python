# File: gcd.py
# to find the greatest common divisor or factor of two numbers
# 
# Helen Chac, ECS 10, Fall 2012
#

#define gcd
def gcd(m, n):
    #keep looping until n is 0
    while(n != 0 ):
        # call result m % n - that's the function that we're using
        result = m%n
        # swap m with n , and n with (m % n ) which is result - Euclid's algorithm

        m = n
        n = result

    return m

#define main
def main():

    # ask user to input first number
    m = int(input("First number (0 to stop): "))

    # if first number is not equal to zero, continue on
    # if first number is 0 , the program stops
    while( m != 0 ):

        # ask user for second number
        n = int(input("Second number: "))

        # place gcd (m, n) in a variable (k- the number that evenly divides m & n)
        k = gcd(m, n)
        
        print("The greatest common divisor of", n , "and", m , "is" , k)

        # ask user for next set first number and it will continue to loop
        m = int(input("First number (0 to stop): "))

main()
