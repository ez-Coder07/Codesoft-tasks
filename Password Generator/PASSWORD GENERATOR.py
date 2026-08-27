import random
import string


def printSeprator(n:int=50, sepr:str="-"):
    print(sepr * n)

printSeprator()

while True:
    try:
        l = int(input("enter the length of the password :"))
        if l<=0:
            raise ValueError
    except ValueError:
        print("Invalid input. Try again.")
        continue
    else:
        break

printSeprator()
print("1)numeric only")
print("2)alphabets only")
print("3)alphaNumeric")
print("4)alphaNumeric+special characters")
printSeprator()

while True:
    try:
        choice = int(input("select password type :"))
        if choice not in (1,2,3,4):
            raise ValueError
    except ValueError:
        print("Invalid input. Try again.")
        continue
    else:
        break

actions = {
    1: lambda: random.choices(string.digits,k=l),
    2: lambda: random.choices(string.ascii_letters,k=l),
    3: lambda: random.choices(string.ascii_letters+string.digits,k=l),
    4: lambda: random.choices(string.ascii_letters+string.digits+string.punctuation,k=l)}

passList = actions[choice]()
passStr = ""
for i in passList:
    passStr += i
print("+" + "-" * (l+5) + "+")
print(f"| {passStr:<{l+3}} |")
print("+" + "-" * (l+5) + "+")