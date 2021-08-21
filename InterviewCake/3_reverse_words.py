"""
message = [ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ]

reverse_words(message)

# Prints: 'steal pound cake'
print(''.join(message))

https://www.interviewcake.com/question/python3/reverse-words?course=fc1&section=array-and-string-manipulation

"""

def reverse_words(message: list):

    # O(n)
    _reverse_chars(message, 0, len(message)-1)
    left = 0

    # Here wring i == len(message) before or condition is very important and
    # iterating for till len + 1 to avoid calling _reverse_chars method for last word
    for i in range(len(message) + 1):
        # Found the end of the current word!
        if i == len(message) or message[i] == " ":
            _reverse_chars(message, left, i - 1)
            left = i + 1

# Helper function to reverse characters
def _reverse_chars(message, left, right):

    while left < right:
        message[left], message[right] = message[right], message[left]
        left += 1
        right -= 1


message = [ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ]
reverse_words(message)
print(''.join(message))
