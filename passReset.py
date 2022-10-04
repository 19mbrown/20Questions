import string as s
from zxcvbn import zxcvbn 

def hasUppers(a):
    x = bool()
    for i in a:
        if i in s.ascii_uppercase:
            x = True
        else:
            x = False
        if x:
            break
    return x

def hasLowers(a):
    x = bool()
    for i in a:
        if i in s.ascii_lowercase:
            x = True
        else:
            x = False
        if x:
            break
    return x

def passwords():
    p1 = input("What's your password? ")
    p2 = input("Retype the password? ")
    if p1 == p2:
        return [True, p1]
    else:
        return [False, p1]

def passReset():
    global password
    x = 0

    passFunc = passwords()
    password = passFunc[1]
    while not (passFunc[0]):
        print("Passwords dont match! ")
        password = passwords()[1]

    ## check if password has upper and lower case 
    if not (hasUppers(password) and hasLowers(password)):
        print("Must have uppercase and lowercase! ")
        print("PERMISSION DENIED")
        exit(1)

    if len(password) <= 8:
        print("Must be at least 8 characters")
        print("PERMISSION DENIED")
        exit(1)
    
    print("Password entered succesfully! ")
    print(f"Your password is given a score of {int(zxcvbn(password)['score']) * 25}")

passReset()
