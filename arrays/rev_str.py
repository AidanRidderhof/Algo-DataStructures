def reverse (string):
    if not isinstance(string, str):
        raise AttributeError("not a string")
    else:
        #method 1
        newstring = string[::-1]

        #method 2
        #newstring = ''.join(reversed(string))

        #method 3
        #newstring = ''
        #for char in string:
            #newstring = char + reversed_string

        print(newstring)


reverse("hello there")