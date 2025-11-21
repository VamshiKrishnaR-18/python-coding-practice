def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

print(is_palindrome(121))
