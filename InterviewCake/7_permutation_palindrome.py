"""
https://www.interviewcake.com/question/python3/permutation-palindrome?course=fc1&section=hashing-and-hash-tables
"civic" should return True
"ivicc" should return True
"civil" should return False
"livci" should return False
"""

# def is_palindrome(text):
#
#     # print(text[::-1]) # Easy way to reverse string
#
#     len_text = len(text)
#     reversed_text = ""
#     while len_text > 0:
#         reversed_text = reversed_text + text[len_text-1]
#         len_text -= 1
#     print(reversed_text)
#     if reversed_text == text:
#         return True
#     else:
#         return False
#
# def permutation(text):
#     dict = {}
#     for t in text:
#         if t in dict:
#             dict[t] = 1
#         dict[t] = dict.get(t, 0) + 1
#     print(dict)
#     # for t in dict:
#
#
# text = "kkppppkk"
# # print(isPalindrome(text))
#
# permutation(text)

def is_palindrome(text):

    # Convert to dict
    text_dict = {}
    for letter in text:
        if letter not in text_dict:
            text_dict[letter] = 0
        text_dict[letter] = text_dict[letter] + 1
    print(text_dict)

    # If more than 1 keys are odd then not palindrome
    result = 0
    for letter in text_dict:
        if text_dict[letter] % 2 != 0:
            result += 1
    if result > 1:
        return False
    else:
        return True


text = "civic"
print(is_palindrome(text))
