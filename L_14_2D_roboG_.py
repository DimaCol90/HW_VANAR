import os
import random



gmap=[
    [' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ']
]

i=0
hp=3
option=""

############### PLACE RANDOM ROBOT ########
robo_r=random.randint(0,4)
robo_c=random.randint(0,4)
gmap[robo_r][robo_c]="♙"
############### PLACE RANDOM ROBOT ########


############# PLACE RANDOM MINES ##############
while i < 3:
    mine_r = random.randint(0, 4)
    mine_c = random.randint(0, 4)
    if gmap[mine_r][mine_c] != '♙' and gmap[mine_r][mine_c] != '⚛':
        gmap[mine_r][mine_c] = '⚛'  # Place the mine
        i += 1
#############PLACE MINES##############        

    
while option !="q":
    if hp!=0:
    ######### PRINT THE MAP ######### 
        os.system("cls")
        print(f"You HP is {hp} now")   
        print("-"*12)
        for r in range(5):
            print("|",end="")
            for c in range(5):
                print(gmap[r][c],end=" ")
            print("|")    

        print("-"*12)
        print("\n\nCONTROLS\na - left\nd - right\nw - up\ns - down\nq - quit")
        ######### PRINT THE MAP ######### 

        ######### CONTROLS ##############
        option = input(">> ")

        if option=="d" and robo_c < 4:
            if gmap[robo_r][robo_c+1]=="⚛":
                hp-=1
                    
            gmap[robo_r][robo_c]=' '
            robo_c+=1
            gmap[robo_r][robo_c]='♙'
                    
        elif option=="s" and robo_r < 4:
            if gmap[robo_r+1][robo_c]=="⚛":
                hp-=1
                print(f"You HP is {hp} now")    
            gmap[robo_r][robo_c]=' '
            robo_r+=1
            gmap[robo_r][robo_c]='♙'
            
        elif option=="a" and robo_c > 0:
            if gmap[robo_r][robo_c-1]=="⚛":
                hp-=1
                print(f"You HP is {hp} now")  
            gmap[robo_r][robo_c]=' '
            robo_c-=1
            gmap[robo_r][robo_c]='♙'      
        elif option=="w" and robo_r > 0:
            if gmap[robo_r-1][robo_c]=="⚛":
                hp-=1
                print(f"You HP is {hp} now")  
            gmap[robo_r][robo_c]=' '
            robo_r-=1
            gmap[robo_r][robo_c]='♙'
        elif option=="q":
            break     
    else:
        os.system("cls")
        print("Eye laws dug aim ")
        break            
    ######### CONTROLS ##############        
        


#HW1 add left and up movement  +    
# add limits     
# add mines + HP and game over conditions        