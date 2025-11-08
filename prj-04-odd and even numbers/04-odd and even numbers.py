# variable ---------------------
oddNumbers = []
evenNumbers = []

# main -----------------------
enterNumber = input("plz enter the numbers like 12,15,18,... ---> ")
sNumbers = enterNumber.split(",")

numbers = [int(i) for i in sNumbers]
print(numbers)
for i in numbers:
    if i % 2 == 0:
        oddNumbers.append(i)
    else:
        evenNumbers.append(i)

print(f'you have {len(oddNumbers)} odd numbers list is --> {oddNumbers}')
print(f'you have {len(evenNumbers)} even numbers list is --> {evenNumbers}')
print(type(oddNumbers))