import string
from inspect import currentframe

def get_linenumber():
    cf = currentframe()
    return cf.f_back.f_lineno

valid = True

legalChars = string.ascii_letters + string.digits
possible = string.ascii_letters + string.digits + ".@"

email = input("What's your email? ")
for letter in email:
    if letter not in possible:
        print(i, "Is not a valid character.")
        break
        valid = False
if email.count("@") != 1:
    print("No/too many @ symbol")
    valid = False
if not email.count(".") >= 1:
    print("No dots.")
    valid = False

for i in email[:email.index("@")]:
    if i not in legalChars:
        print(f"{i} is not a valid charecter.",get_linenumber())
        valid = False
for i in email[email.index("@")+1:]:
    if i not in legalChars + ".":
        print(f"{i} is not a valid charecter.",get_linenumber())
        valid = False
if "." not in email[email.index("@"):]:
    print("There's no dot in the email.",get_linenumber())
    valid = False

if valid:
    print("Your email is VALID!")