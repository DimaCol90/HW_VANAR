import os
os.system("cls")

def printStar():
    print("*",end=" ")

def printStarRow(w):
    for i in range(w):
        printStar()
    print()

def printStarRect(w,h):
    if w>0 and h>0:
        for i in range(h):
            printStarRow(w)
    else:
        print("Dimension cannot be NEGATIVE!!")        


printStarRect(5,5)


#Draw diagram

