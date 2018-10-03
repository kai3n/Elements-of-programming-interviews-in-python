def is_palindromic(s):
    return s == s[::-1]

print(is_palindromic("asf"))
print(is_palindromic("asdfdsa"))
print(is_palindromic("aaaaa"))