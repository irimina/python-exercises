# pig latin translator

print('Welcome to the Pig Latin Translator!')

#create a variable to hold our translation suffix.
pyg = 'ay'

original = input('Enter a word: ')

# checking if the user enetered some words

if len(original) and original.isalpha() > 0:
    # isalpha checks if only alphabetical characters were enetered by the user
    # test multiple inputs ( empty, numeric etc) to test the code
    #print(original)
    word = original.lower()
    first = word[0]
    #print(first)
    # Now that we have the first letter stored, we need to add both the letter and the string stored in pyg to the end of the
    # original string.
    new_word = word[1:len(word)] + first + pyg
    print(new_word)
    # this is similar to new_word=[1:]
else:
    print('empty')


