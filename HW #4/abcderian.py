# Homework #4
# File Name: abcderian.py
# 
# Ask the user for a string and tell the user whether or not it is abcderian or not
# 
# Helen Chac, ECS 010, Fall 2012
#
#

# 
# If the word is abcderian it will return True
# If the word is not abcderian it will return False
def isabcde(s):
    # The range will be how long the word is
    for i in range (len(s)):
        # when the length of the word is 1, return True
        if len(s) == 1:
            return True
        # compare two letters at a time
        # if one letter is smaller than the other, call the function
        elif s[i] <= s[i+1]:
            return isabcde(s[1:])
        # if it isn't any of them, return false.
        else:
            return False

# this function will extract the symbols and number from the word
def extract(s):
    # start with nothing in the string
    result = ''
    for i in range (len(s)):
        # if the character is an alphabet, add it to the string
        if s[i].isalpha()== True:
            result = result + s[i]
        # if the character is not an alphabet, add blank to the string
        elif s[i].isalpha() == False:
            result = result + ''
    return result 


def main():
    # use try to catch the EOFError
    try:
        # use while to loop
        while True:
            # ask user for a string
            x = str(input("The string? "))
            # convert the string into all lowercase letters
            s = x.lower()
            # call extract(s) into extracted
            extracted = extract(s)
            # use extracted in the function isabcde(s)
            abcderian = isabcde(extracted)

            # if extracted = nothing, print it is an abcderian
            if extracted == '':
                print (x, 'is abcderian')
            # if False, print that it is not abcderian
            elif abcderian == False:
                print (x, 'is not abcderian.')
            # if True, print that it is an abcderian
            elif abcderian == True:
                print (x, 'is abcderian')
    except EOFError:
        print('')
        
main()
