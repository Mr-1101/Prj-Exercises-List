# variables------------

fNumber = 0
sNumber = 0
result = 0
action = ""

# input------------------

fNumber = int(input("plz enter the first number ---> "))
action = input("plz tell what you want to do - + * / ---> ")
sNumber = int(input("plz enter the second number ---> "))

#core-------------------
if action == '+':
    result = fNumber + sNumber 
    print (f"your  result is :{result}")
elif action == '-':
    result = fnumber - sNumber
    print (f"your  result is :{result}")
elif action == '*':
    result = fNumber * sNumber
    print (f"your  result is :{result}")
elif action == '/':
    result = fNumber / sNumber
    print (f"your  result is :{result}")
else:
    print('write the corect value !!! ')
