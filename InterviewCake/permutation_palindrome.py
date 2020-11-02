"""
https://www.interviewcake.com/question/python3/permutation-palindrome?course=fc1&section=hashing-and-hash-tables
"""

def is_palindrome(text):

    # print(text[::-1]) # Easy way to reverse string

    len_text = len(text)
    reversed_text = ""
    while len_text > 0:
        reversed_text = reversed_text + text[len_text-1]
        len_text -= 1
    print(reversed_text)
    if reversed_text == text:
        return True
    else:
        return False

def permutation(text):
    dict = {}
    for t in text:
        if t in dict:
            dict[t] = 1
        dict[t] = dict.get(t, 0) + 1
    print(dict)
    # for t in dict:


text = "kkppppkk"
# print(isPalindrome(text))
permutation(text)
