pyg = 'ay'

original = input('Enter a word: ')

if len(original) > 0 and original.isalpha():
    print ("Original : ", original) 
    word = original.lower()
    first = word[0]
    new_word = word + first + pyg
    new_word = new_word[1:len(new_word)]
    print ("Pig Latin : ", new_word)
else:
    print ('Error: Invalid Input')
