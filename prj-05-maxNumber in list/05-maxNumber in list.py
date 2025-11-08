# variablr ------------------------------
getNumbers = ""
counter = -1
indexCounter = 0

# main ---------------------------------


sNumbers = input("plz enter your numbers like 1,2,3,4,..... ---> ")
getNumbers = sNumbers.split(",")
numbers = [int(item) for item in getNumbers]



'''
maxNumber = numbers[0]

while indexCounter <= len(numbers):
    for i in numbers:
        if indexCounter <= len(numbers):
            i > maxNumber
            maxNumber = i
            counter = indexCounter
        indexCounter += 1

    print(f"your max number in the list is {maxNumber} it has in this {counter} place of array")
'''

# other way -------------------------------------

maxNum = max(numbers)

for i in numbers:
    if i != 100:
        counter += 1
print(f"your max number is {maxNum} ,and this number.s index {counter}")