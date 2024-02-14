import os   
friends=[]

os.system("cls")
while len(friends)<100:
    name=input("Add friend name / Enter no: ")
    if name == "no":
        break
    if name in friends:
        print(f"You've already added {name} to your list" )

    else:
        friends.append(name)

print("You have",len(friends),"friends")
for i in range(len(friends)):
    print("  ",i,">>",friends[i])        



#HW1 before append check if the name is in the list.     