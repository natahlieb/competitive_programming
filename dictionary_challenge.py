__author__ = 'natahlie_beavers'
import math

#get input, sort  alphabetically
word = list(raw_input())
sorted_word = sorted(word)
word_length = len(word)

#position of the word in the dictionary that we'll be returning
position = 1

#index of the character we're interested in from our original word
original_word_position_examined = 0

#loop through our word, examining every character in it
while original_word_position_examined != (word_length-1):

        #number of characters occuring in the alphabet before the character in the word we're interested in
        greater_than_first = 0

        #characters that have not been examined yet in the sorted list of characters from our original word
        characters_remaining = len(sorted_word) - 1

        #iterate through our list of sorted characters,
        #try to see how many occur in the alphabet before the character we're currently examining from the original word
        i = 0
        while(sorted_word[i]!= word[original_word_position_examined]):
            greater_than_first+=1
            i+=1


        #check to see how many duplicates  are currently in our sorted string
        #use these values to calculate the divisor in the function used to find the number of permutations
        divisor = 1
        d = dict.fromkeys(sorted_word, 0)
        for character in sorted_word:
            d[character] += 1
        for key in d:
            if d[key] > 1:
                divisor *= math.factorial(d[key])

        #add to our previosly calculated position for our input word
        position += (greater_than_first * math.factorial(characters_remaining))/divisor

        #on next iteration, see how many characters in our sorted list occur alphabetically before the next character in our input word
        #remove the character from the original word that we just examined from our sorted list- we've already considered what characters may have come before it alphabetically
        original_word_position_examined +=1
        sorted_word = sorted(word[original_word_position_examined:word_length])

print str(position)
