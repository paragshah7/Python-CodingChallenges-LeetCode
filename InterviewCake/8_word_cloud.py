"""
https://www.interviewcake.com/question/python3/word-cloud?course=fc1&section=hashing-and-hash-tables
'After beating the eggs, Dana read the next step:'
'Add milk and eggs, then add flour and sugar.'
"We came, we saw, we conquered...then we ate Bill's (Mille-Feuille) cake."
'The bill came to five dollars.'

Count of every word in a dictionary with punctuations handled (using regex)
"""
from icecream import ic as print

def word_cloud(text_list):
    word_list = []
    word_dict = {}

    for text in text_list:
        word_list.extend(text.split())

    for word in word_list:
        word = ''.join(letter for letter in word if letter.isalpha())   # Most imp line, removes all punctuation
        if word.lower() not in word_dict:   # removes all caps
            word_dict[word.lower()] = 1
        else:
            word_dict[word.lower()] += 1
    print(word_dict)


text_list = ['After beating the eggs, Dana read the next step:',
             'Add milk and eggs, then add flour and sugar.']
word_cloud(text_list)
