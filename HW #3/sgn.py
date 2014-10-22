# File Name: sgn.py
# An inputted number of 0 will print sgn(#) = 0
# An inputted number greater than 0 will print 1
# An inputted number is less than 0 will print -1
#
# Helen Chac, ECS 010, Fall 2012
# 

def main():
    
    #try & except to catch EOFError
    try:
        
        x= float (input ("Please enter a number: "))
        
        while True:
            
            # if 0, print 0
            if x == 0:
                print ('sgn(', "%.2f" %x,') = 0 ')
                
            # if greater than 0, print 1
            elif x > 0:
                print ('sgn(', "%.2f" %x,') = 1 ')

            # otherwise, print -1
            else:
                print ('sgn(', "%.2f" %x,') = -1')

            # program will continue
            x = float (input("Please enter a number: "))

    # if someone inputs control + D, the program will stop
    except EOFError as msg:
        print(end = '')

# call main
main()
