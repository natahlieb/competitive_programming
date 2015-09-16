__author__ = 'natahlie'

word = list(raw_input())

#divide string in half
word_len = len(word)

current_spot = 0

for char in word:
    i =0
    while i <= word_len:
        temp_word = list(word)
        temp_word.insert(i, char)
        temp_reversed = list(temp_word[::-1])
       # print temp_word
        #print temp_reversed
        if (temp_word == temp_reversed):
            print ''.join(temp_word)
            exit()
        i+=1

print "NA"
