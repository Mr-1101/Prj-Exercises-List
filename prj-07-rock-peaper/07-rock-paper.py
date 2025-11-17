import random

# variable ----------------------------------
maxPlay = 7

getItem = ""
result = ["rock","paper","scissors"]


# main -------------------------------------
def palying():
    winCounter = 0
    lossCounter = 0
    equal = 0
    for i in range(0,maxPlay):
        
        getItem = input("enter your chousess like this ----> rock ----> paper ---> scissors--->  ")

        if getItem == "scissors":
            result1 = random.choice(result)
            if result1 != "scissors":
                if result1 == "paper":
                    winCounter += 1
                    print(f"you win for {winCounter} times cpu choises {result1}")
                elif result1 == "rock":
                    lossCounter += 1
                    print(f"you loss for {lossCounter} times cpu choises {result1}")
            else:
                equal += 1
                print(F"you choise {getItem} and the cpu choise {result1}")
        elif getItem == "paper":
            result1 = random.choice(result)
            if result1 != "paper":
                if result1 == "rock":
                    winCounter += 1
                    print(f"you win for {winCounter} times cpu choises {result1}")
                elif result1 == "scissors":
                    lossCounter += 1 
                    print(f"you loss for {lossCounter} times cpu choises {result1}")
            else:
                equal += 1
                print(F"you choise {getItem} and the cpu choise {result1}")
        elif getItem == "rock":
            result1 = random.choice(result)
            if result1 != "rock":
                if result1 == "scissors":
                    winCounter += 1
                    print(f"you win for {winCounter} times cpu choises {result1}")
                elif result1 == "paper":
                    lossCounter += 1 
                    print(f"you loss for {lossCounter} times cpu choises {result1}")
            else:
                equal += 1
                print(F"you choise {getItem} and the cpu choise {result1}")
        else:
            print("enter the courect value ---> ")
    print(f"your game result: you win {winCounter} and loss {lossCounter} and {equal} same gase")


palying()