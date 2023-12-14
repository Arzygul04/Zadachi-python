def is_palindrome(s):
    s = s.lower()
    s = ".join(e for e in s if e.isalnum())
    return s == s[::-1]

user_input = input("Введите строку: ")
print(is_palindrome(user_input))
