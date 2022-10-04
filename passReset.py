#########################
#### NOT WORKING YET ####
#########################


import string


def hasUppers(a):
    for i in a:
        if i in string.ascii_uppercase:
            return True
            break
        else:
            return False
def hasLowers(a):
    for i in a:
        if i in string.ascii_lowercase:
            return True
            break
        else:
            return False 
password = str()

while len(password) < 8 or not (hasLowers(password) and hasUppers(password)):
    password = input("What's your password? ")
    if not len(password) < 8 or not (hasLowers(password) and hasUppers(password)):
        password2 = input("Retype the password: ")
if password == password2:
    print("Correct Password!!")
else:
    password()
