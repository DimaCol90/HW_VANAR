import os

Length = int(input("Length: "))
Heigth= int(input("heigth: "))

size=Length*Heigth
n=1
print()
while n<=size:
    
    print("+ ",end="")

    if n%Length==0:
       print() 

    n+=1

print()



#HW: refactor code so it can draw any size recatangle