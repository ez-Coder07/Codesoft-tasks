from random import choice

score = {}
f = 0
def validInputTaker(statement, *validValues, datatype=str):
    while True:
        try:
            tempInput = datatype(input(statement).lower())
            if validValues and tempInput not in validValues:
                raise ValueError 
        except ValueError:
            print("an err occurred try again!")
            continue
        else:
            return tempInput
  
def new_game():
    global f
    if f == 1:
        s1 = "Are you sure you want to start a new game ? [y/N](default = N): "
        new = validInputTaker(s1)
        if new == "y":
            first_interface_btns.pop("Continue")
            f = 0
        else :
            firstInterface()
    score.update({"you": 0, "computer": 0})

def printscore():
    print("\n" + "=" * 25)
    print("      SCOREBOARD")
    print("=" * 25)
    for x, y in score.items():
        print(f"{x.capitalize():<10}: {y}")
    print("=" * 25 + "\n")

def cuntinue():
    pass

# def initialise():
#     global f
#     f = 1
#     score.update({"you": 0 ,"computer": 0})



first_interface_btns = {"exit": exit, "New Game": new_game}


def firstInterface():
    btnList1 = list(first_interface_btns.keys())
    btnList1.reverse()
    tempTuples = enumerate(btnList1, start=1)
    for i,btns in tempTuples:
        print(f"{i}) {btns}")
    tempChoices = list(range(1, len(btnList1)+1))
    choose = validInputTaker(f"Please enter {tempChoices} :", *tempChoices, datatype=int)
    first_interface_btns.get(btnList1[(choose-1)])()

def core():
    if(computer == you):
                print("Its a draw")
    else:
        if((computer - you) == -1 or  (computer - you) == 2 ):
            print("You lose!")
            score["computer"]+= 1
        else:
            print("You win!") 
            score["you"]+= 1

firstInterface()
while True:
    print("r for rock , p for paper , s for scissors (b for back to menu)")
    computer = choice([-1, 0, 1])
    youDict = {"r": 1, "p": -1, "s": 0}
    youStr = validInputTaker("Enter your choice (r/p/s): ", "r","p","s","b")
    if youStr == "b":
        firstInterface()
    else:
        f=1
        first_interface_btns.update({"Continue": cuntinue})
        reverseDict = {1: "rock", -1: "paper", 0: "scissors"}
        you = youDict[youStr]
        print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")
        core()
        printscore()