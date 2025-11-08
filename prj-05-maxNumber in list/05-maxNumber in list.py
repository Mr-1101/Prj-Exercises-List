# variablr ------------------------------
maxNumber = 0
getNumbers = ""
counter = 0
# main ---------------------------------
sNumbers = input("plz enter your numbers like 1,2,3,4,..... ---> ")
getNumbers = sNumbers.split(",")
numbers = [int(item) for item in getNumbers]

while numbers[counter] <= len(numbers):
    print( numbers[counter], len(numbers))
    for i in numbers:
        if numbers[counter] > maxNumber:
            maxNumber = i
            counter += 1

    print(f"your max number in the list is {maxNumber} it has in this {counter} place of array")


