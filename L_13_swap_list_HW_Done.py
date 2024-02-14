import os
os.system("cls")
people = ["Johny", "Marry","Francis","Jora","Leonid","Borea"]

print("BEFORE",people)

index1 = int(input("Enter the index of the first person you want swapped: "))
index2 = int(input("Enter the index of the second person you want swapped: "))

if index1 >= 0 and index1 < len(people) and index2 >= 0 and index2 < len(people):
    temp = people[index1]
    people[index1] = people[index2]
    people[index2] = temp

    print("AFTER",people)
else:
    print("Invalid indices. Please enter indices in the following range (0 - {}).".format(len(people)-1))

#HW add code so that use can indicate which places should be swapped
#HW* check boundaries