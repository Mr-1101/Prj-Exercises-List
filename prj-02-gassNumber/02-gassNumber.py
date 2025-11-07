import random

# variable ----------------

maxRange = 0
gessNumber = 0
counter = 0
maxCounter = 5
# main --------------------

maxRange = int(input("enter the max of renge you want to gess ---> "))
corectNumber = random.randint(0, maxRange)

while counter != maxCounter :
    gessNumber = int(input("enter your Number ---> "))
    if gessNumber > corectNumber:
        counter +=1
        print(f"your number is more than corect number ")
        if counter == maxCounter:
            print(f"sory you loss the game the corect number was {corectNumber}")
            break
    elif gessNumber < corectNumber:
        counter +=1
        print(f"your number is less than corect number")
        if counter == maxCounter:
            print(f"sory you loss the game the corect number was {corectNumber}")
            break
        print(counter)
    elif gessNumber == corectNumber:
        print(f"your gess is corect you win the number was {corectNumber}")
        break
    else:
        print(f"sory you loss the game the corect number was {corectNumber}")
    


