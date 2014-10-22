# went over greatest common divisor in class using recursvie functions
# parameters in the else return the back to the function and keep dividing


def gcd(m, n):
    if n == 0:
        return m
    else:
        return gcd(n, m%n)

# when the user does not input 0 , it will continue
def main():
    m = int(input("Enter first number: "))
    while m != 0:
        n = int( input("Enter second number: "))
        result = gcd(m,n)
        print("GCD: ", result)
        m = int( input("Enter first number: "))
main()
