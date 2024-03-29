import os
from os.path import exists

option=0
running = True
destinations =[]
prices=[]

def readDestinations():
    global destinations
    file = open("C:\\Users\\User\\Desktop\\PY MASTER\\BASIC\\VS_CODE_PR\\VANAR\\LESSON_15\\Booking\\DATA\\destinations.txt", "r")
    lines=file.readlines()

    for line in lines:
        destinations.append(line.strip("\n"))

    file.close()

def readPrices():
    global prices
    fileP=open("C:\\Users\\User\\Desktop\\PY MASTER\BASIC\\VS_CODE_PR\\VANAR\\LESSON_15\\Booking\\DATA\\prices.txt","r")
    
    linesP=fileP.readlines()

    for lineP in linesP:
        prices.append(float(lineP))

    fileP.close()    

def renderDestinations():
    for i in range(len(destinations)):
        print(f"{destinations[i]:>20} - {prices[i]:10.2f}")
        
    input("hit enter ")




def renderOrder():
    pnc=input("enter your personal number: ")
    if exists(f"C:\\Users\\User\\Desktop\\PY MASTER\\BASIC\\VS_CODE_PR\\VANAR\\LESSON_15\\Booking\\DATA\\{pnc}.txt"):
        file=open(f"C:\\Users\\User\\Desktop\\PY MASTER\\BASIC\\VS_CODE_PR\\VANAR\\LESSON_15\\Booking\\DATA\\{pnc}.txt",'r')
        lines=file.readlines()
        print("Your order details: ")
        for line in lines:
            print(line)
        file.close()
    else:
        print('Your order does not exist')    
    input("hit enter...")    





def searchDestination():
    destination= input("enter destination name: ")
    found=destination in destinations

    if found:
        print(f"Destination {destination} is available") 
        quantity=int(input("how many tickets do you need? "))
        index_dest_price=destinations.index(destination)
        print(f"The total cost of {quantity} tickets would be {quantity * prices[index_dest_price]}")
        confirmation=input("Would you like to buy the tickets?(y/n)")=="y"
        if confirmation:
            print(f"{quantity} tickets sent to your email")
            pnc=input("Enter your ID number: ")
            file=open(f"C:\\Users\\User\\Desktop\\PY MASTER\\BASIC\\VS_CODE_PR\\VANAR\\LESSON_15\\Booking\\DATA\\{pnc}.txt",'w')
            file.write(f'{destination}\n')
            file.write(f'{quantity}\n')
            file.write(f"{quantity*prices[index_dest_price]}")
            file.close()
            print("order saved")
            
        else:
            print("Come back when ready")    
    else:
        print(f"Destination {destination} is unavailable")     
    input("hit enter ")

def deleteOrder():
    pnc=input("Enter your personal number: ")
    file_path = f"C:\\Users\\User\\Desktop\\PY MASTER\\BASIC\\VS_CODE_PR\\VANAR\\LESSON_15\\Booking\\DATA\\{pnc}.txt"

    if os.path.exists(file_path):
        os.remove(file_path)
        print("File removed successfully.")
    else:
        print("File does not exist.")    

def renderMenu():
    os.system("cls")
    global option
    print("OPTIONS")
    print("""
    1. Search destination
    2. Show destinations
    3. Search order
    4. Delete order
    0. Exit
        """)
    option=int(input("choose>>>> "))



      #HW3 continue the idea: 
         # ask for ticket quantity
         # calculate total cost: 3 x tickets to Paris = 600 
         # ask for confirmation 