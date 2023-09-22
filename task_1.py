def is_not_punct(world):
    world_return = []
    for i in range(len(world)):
        if  world[i].isdigit() or world[i].isalpha():
            world_return.append(world[i])
    return "".join(world_return)



def is_palindrome(string):
    string = str(string)
    string_pol = string.lower().split()
    for i in range(len(string_pol)):
        string_pol[i] = is_not_punct(string_pol[i])
    string_pol = "".join(string_pol)
    return string_pol == string_pol[::-1]


print(is_palindrome(",A man, a plan, a canal -- Panama"))
print(is_palindrome("Madam, I'm Adam!"))
print(is_palindrome(333))
print(is_palindrome(None))
print(is_palindrome("Abracadabra"))