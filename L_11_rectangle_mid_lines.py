# - - - - - -
#|           |
#|           |
#|           | 
# - - - - - -
#
#

import os 

os.system("cls")

w=int(input("width: "))
h=int(input("heigth: "))
halfw=w//2
halfh=h//2
w_odd=w%2
h_odd=h%2

for i in range(h):
    for j in range(w):
        if i == 0 or i ==h-1:
            print("-",end="")
        elif i==halfh and h_odd==1:
            print("-",end="")    
        elif j==0:
            print("|",end="")
            
        elif j==w-1:
            print("|", end="")    
        elif j==halfw and w_odd==1:
            print("|",end="")    
        else:         
            print(" ",end="") 
            
          
    
    print()
