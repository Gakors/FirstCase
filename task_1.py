def is_palindrome(string):
    string = str(string)
    string = string.lower()
    string_return = []
    for i in range(len(string)):
        if string[i].isalpha() or string[i].isdigit():
            string_return.append(string[i])
    return string_return == string_return[::-1]


print(is_palindrome(",A man, a plan, a canal -- Panama"))
print(is_palindrome("Madam, I'm Adam!"))
print(is_palindrome(333))
print(is_palindrome(None))
print(is_palindrome("Abracadabra"))