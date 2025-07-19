def reversestr(string):
    if len(string) == 0:
        return ""
    return reversestr(string[1:]) + string[0]

print(reversestr("hello")) 