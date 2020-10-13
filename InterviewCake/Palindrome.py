# def isPalindrome(text):
#     return True if text == text[::-1] else False

def isPalindrome(text):
    if text == ''.join(reversed(text)):
        return True
    else:
        return False


print(isPalindrome('naan'))