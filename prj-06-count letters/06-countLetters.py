# variables ----------------------------
letters = {}

# main ---------------------------------
text = input("enter your text to count :  \n")
print(len(text))

for i in text:
    
    if i not in letters.keys():
        letters[i] = 1

    elif i in letters.keys():
        counter = letters.get(i) 
        counter += 1
        letters[i] = counter

print(letters)
