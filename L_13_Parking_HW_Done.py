import os
import time
os.system("cls")
p = [None,None,"BMW",None,None,"Toyota","BMW"]

user_car_brand = input("Name your brand: ")
user_park_index = int(input("What place: "))
if p[user_park_index] == None:
    print("You can park there")
    p[user_park_index] = user_car_brand
else:
    print("This place is occupied") 


total = len(p)
free = 0
for i in range(len(p)):
    if p[i] == None:
        free += 1
print(f"""
-------------------------------------------------
Parking (free/total):{free} / {total} places
      
      """)
time.sleep(2)
os.system("cls")
car_stats = {}
for car in p:
    if car is not None:
        if car in car_stats:
            car_stats[car] += 1
        else:
            car_stats[car] = 1

print("     Car brand statistics:")
for brand, count in car_stats.items():
    print(f'    {brand} - {count}')

print()


for i in range(len(p)):
    print(i, p[i])

