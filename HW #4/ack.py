# File Name: ack.py
#
# Helen Chac, ECS 010, Fall 2012


def A(m,n):
    # if m or n is negative function won't work
    if m < 0 or n < 0:
        print ("no negative numbers!")
    # if m is 0, return n + 1
    elif m == 0:
        return n + 1
    # if m is greater than 0 and n = 0 return the function with n as 1 and m -1 
    elif m > 0 and n == 0:
        return A(m-1, 1)
    # if m is greater than 0 and n is greater than 0, return m as a m -1 and call the function again in the parameters
    elif m > 0 and n > 0:
        return A(m-1, A(m, n-1))

def main():
    # ask user for input
    m = int(input("m? "))
    # if m is negative, print "no negative numbers"
    if m < 0:
        print ("no negative numbers!")
    # otherwise, ask user to input n 
    else:
        n = int(input("n? "))
        # if n is negative, print "no negative numbers"
        if n < 0:
            print ("no negative numbers!")
        # otherwise print the answer returned at function A(m,n)
        else:
            print (A(m, n))
#run it
main()
