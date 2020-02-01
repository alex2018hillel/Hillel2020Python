def palindrome(s):
    """Check on palindrome"""
    if ''.join(reversed(s)) == s:
        return True
    else:
        return False

s = input("Input string: ")
print(palindrome(s))