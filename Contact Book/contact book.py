import json

Persons = []

class Person:
    def __init__(self, name, phoneNo, email, address):
        self.name = name
        self.phoneNo =  phoneNo 
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name:<20} Mobile No.: {self.phoneNo}"

    def details(self):
        for key, values in self.__dict__.items():
            print(f"{key} :{values}")
        printlines()

    def updateContact(self):
        self.name,self.phoneNo,self.email,self.address = inputTaker(self.name,self.phoneNo,self.email,self.address)
        save("Contact Updated")
        self.details()

    
def inputTaker(*defaults):
    nam = inputWithDefault("Name", defaults[0])
    while True:
        phone = inputWithDefault("Phone No.",defaults[1])
        if str(phone).isdecimal():
            phone = int(phone)
            break
        else:print("Invalid Number")
    email = inputWithDefault("email", defaults[2])
    address = inputWithDefault("address", defaults[3])
    printlines()
    return [nam, phone, email, address]

def loadContacts():
    rawData = []
    Persons.clear()
    try:
        with open("Contact List.json", "r") as cL:
            rawData = json.load(cL)
    except (FileNotFoundError, json.JSONDecodeError):
        with open("Contact List.json", "w") as cL:
            json.dump([], cL)
            return
    for d in rawData:
        Persons.append(Person(**d))

def addContact():
    a = inputTaker(None, None, None, None)
    p1 = Person(*a)
    Persons.append(p1)
    save("New Contact Added")

def save(message:str = "Saved"):
    with open("Contact List.json", "w") as cL:
        json.dump([i.__dict__ for i in Persons], cL, indent=3)
    print(message)
    printlines()

def showAll():
    if not Persons:
        print("No contacts found.")
        printlines()
        return
    else:
        i=1
        for p in Persons: 
            print(f"{i:<3}) {p}")
            i+=1
    printlines()
    selected = selectContact(i-1)
    if selected:
        openContact(selected-1)

def search():
    query = input("enter name or number :")
    printlines()
    results = {}
    for i,person in enumerate(Persons):
        if query in person.name.lower() or query in str(person.phoneNo):
            results.update({i:person})
            
    if not results:
        print("No contacts found.")
        printlines()
        return
    else:
        for i,p in enumerate(results, start=1): print(f"{i:<3}) {Persons[p]}")
        printlines()
        selected = selectContact(len(results))
        if selected:
            openContact(list(results.keys())[selected-1])

def selectContact(x:int):
    while True:
        try:
            num = input(f"enter between 1 to {x} (b or enter to go back) :")
            printlines()
            if (num in ("b", "")): return 0
            elif int(num) in range(1,x+1): return int(num)
            else: raise ValueError
        except ValueError:
            print("Invalid input")

def openContact(index:int):
    Persons[index].details()
    actions = {1:Persons[index].updateContact, 2:lambda: deleteContact(index), 3:back}
    print("1)Edit          2)Delete          3)Back")
    printlines()
    while True:
        try:
            choice = input("select your choice :")
            if int(choice) in (1,2,3): 
                printlines()
                actions[int(choice)]()
                break
            raise ValueError
        except ValueError:
            print("Invalid input")

def back():
    pass

def deleteContact(index:int):
    Persons.pop(index)
    save("Contact Deleted")
    print("*Delete 'Contact.json' file to DELETE ALL contacts")
  
def inputWithDefault(prompt:str,default=None):
    if default==None:
        return input(prompt+" :")
    return input(f"New {prompt} [default={default}] :") or default

def printlines(n:int = 30, symb = "-"):
    print(symb * n)

def main():
    loadContacts()
    printlines()
    while True:
        actions = {1: addContact, 2:showAll, 3:search, 4:exit}
        print("1) Add a contact")
        print("2) List all Contacts")
        print("3) Search a contact")
        print("4) Exit")
        printlines()
        while True:
            try:
                choice = input("select your choice :")
                if int(choice) in actions: break
                raise ValueError
            except ValueError:
                print("Invalid input")
        printlines(100)
        actions[int(choice)]()
        printlines(100, "#")
        printlines(100)

main()