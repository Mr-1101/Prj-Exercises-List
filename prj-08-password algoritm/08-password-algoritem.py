# variable -----------------------------------------
yourPassword = ""
# main---------------------------------------------

def checkPassword():
    
    passUpper = 0
    passLower = 0
    passNumbers = 0
    passSymbol = 0
    symbol = ["@","!","#","$","%","&"]

    yourPassword = input("enter your password to check level ---> ")
    if len(yourPassword) == 12:
        for a in yourPassword :
            if a.isupper():
                passUpper = 1
            elif a.islower():
                passLower = 1
            elif a.isdigit():
                passNumbers = 1
            elif a in symbol:
                passSymbol = 1
        
        result = passUpper + passLower + passNumbers + passSymbol
        if result == 1 :
            print("your password is  so weak")
        elif result == 2 :
            print("your password is weak")
        elif result == 3:
            print("your password is good")
        else:
            print("your password is strong")

        print(f"your password level is {result}")


    else:
        print("your password less or more than 12 characters")




def makePass():
    
    print()






checkPassword()
