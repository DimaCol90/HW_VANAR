from json import loads
import os

#Load from file
def loadFood():
    file = open("C:\\Users\\User\\Desktop\\PY MASTER\\BASIC\\VS_CODE_PR\\VANAR\\LESSON_18\\FOOD_ORDER\\food.json","r")
    food = loads(file.read())
    return food

#print the menu
def printFood(food):
    os.system("cls")
    print("#"*50)    
    for i in range (len(food)):
        
        print(f"{i+1}) {food[i]['name']:20} {food[i]['price']['amount']:8.2f} {food[i]['price']['currency']}")
    print("#"*50)

def printMenu():
    os.system("cls")
    print("#"*50)
    print("1. Show menu")
    print("2. Add to order")
    print("0. Exit")
    print("#"*50)
    option = int(input(">>>>>> "))
    return option