# variable ---------------------
oddNumbers = []
evenNumbers = []
number = 0

# main -----------------------

while number != 100:
    number = input("enter your number to make a list or send 100 to end ---> ")
    if int(number) % 2 == 0:
        oddNumbers.append(number)
    elif int(number) % 2 != 0:
        evenNumbers.append(number)
    else:
        print("enter corect numbers")
    
print(f'you have {oddNumbers.len()} odd numbers list is --> {oddNumbers}')
print(f'you have {evenNumbers.len()} even numbers list is --> {evenNumbers}')