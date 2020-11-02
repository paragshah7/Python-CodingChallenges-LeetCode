def is_palindrome_pythonic(text):
    return True if text == text[::-1] else False

def is_palindrome(text):
    if text == ''.join(reversed(text)):
        return True
    else:
        return False


print(is_palindrome('naan'))