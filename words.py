# def print_upper_words(list_of_words):
#     '''Takes a list of words and prints them in all uppercase'''

#     for word in list_of_words:
#         print(word.upper())

# def print_upper_words(list_of_words):
#     '''Takes a list of words, searches for words that start with the letter 'e' or 'E', and prints them in all uppercase'''

#     for word in list_of_words:
#         if word.find('e', 0, 1) == 0 or word.find('E', 0, 1) == 0:
#             print(word.upper())

def print_upper_words(list_of_words, letter):
    '''Takes a list of words and a starting letter and prints all the words in the list that start with that letter in uppercase'''

    for word in list_of_words:
        if word.find(letter, 0, 1) == 0 or word.find(letter.upper(), 0, 1) == 0 or word.find(letter.lower(), 0, 1) == 0:
            print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], 'H')