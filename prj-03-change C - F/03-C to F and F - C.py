# variable  ---------------------
degree = 0
degreeKind = ""
result = 0

# main --------------------------
degree = int(input("enter your degree to convert --->"))
degreeKind = input("plz enter the kind of your degree?(C - F) -->  ").upper()
print(degreeKind)
def c2f(degree):
    result = (degree * 1.8)+32
    return print(f"this degree {degree} to farenhide is {result} ")

def f2c(degree):
    result = (degree - 32)*1.8
    return print(f"this degree {degree} to centigreat is {result} ")

if degreeKind == "C":
    print(c2f(degree))
elif degreeKind == "F":
    print(f2c(degree))
else:
    print("enter the corect value !!! ")