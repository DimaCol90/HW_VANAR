import os

def clear():
    os.system("cls")

def controls():
    print("Use a,d,s,w for movement")
    key=input(">> ")
    return key
