# File Name: anagrams.py
#
# This file looks for the anagrams of the word in the dictionary and prints it out.
#
# Helen Chac, ECS 10, Fall 2012
#
# Homework # 5

def main():
    # use to catch EOFError, ctrl + D. 
    try:
        # loop the function until the user enters ctrl + D
        while True:
            # ask user what word to look for in the text file
            userinput = input ("Your word? ")
            #open file
            file = open("dict.txt", "r")
            # create an empty list to use to catch the anagrams
            anagramlist = []
            # count is used for counting words
            count = 0
            # reading every word in the file
            for word in file:
                # change the word into lower case
                word = word.lower()
                # strip away the white spaces & return button
                word = word.strip()
                # both the lengths of the word is the same continue on
                if len(userinput) == len(word):
                    # store the sorted inputted words into sort_userinput
                    # store the sorted words of the list into sort_word
                    sort_userinput = sorted(list(userinput))
                    sort_word = sorted(list(word))
                    # if the words sorted are the same
                    if sort_userinput == sort_word:
                        # and if the word is not the same as te input
                        if word != userinput:
                            # add word to the anagram list
                            anagramlist = anagramlist + [word]
                        # otherwise count
                        else:
                           count = count +1
            # if the count is 0 , meaning if the word is not in the dictionary
            if count == 0:
                # print that it is not in the dictionary
                print('The word', userinput, 'is not in the dictionary')
            # if the anagram list length is 0 it means that tere are no anagrams
            elif len(anagramlist) == 0:
                print('There are no anagram for', userinput)
            # if there is one anagram, print it out
            # this is so the commas are correct
            elif len(anagramlist) == 1:
                print("The anagrams for", userinput, 'is', anagramlist[0])
            # if there is two anagrams, print it and then have 'and'
            elif len(anagramlist) == 2:
                print("The anagrams for", userinput, 'is', anagramlist[0], "and", anagramlist[1])
            # if there is more than 2 anagrams, print it so that the there are commas
            elif len(anagramlist) > 2:
                print("The anagrams for", userinput, 'is ', end = '')
                # for every word that happened before the last word print it with commas
                for i in anagramlist[0:-1]:
                    print(i, ", ", end = '', sep ='')
                # print 'and' and the last word
                print('and', anagramlist[-1])
                
    # exception error                
    except EOFError:
        print ('')

    # close file
    file.close()

# run program
main()
