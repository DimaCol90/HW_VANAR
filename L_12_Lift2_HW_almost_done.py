
import os
from time import sleep
DIR_UP              =-1
DIR_STOP=             0
DIR_DOWN            = 1


building_roof       = True
building_floors     = 9
building_parking    = True

lift_floor          = 5
lift_open           = True
lift_dir            = DIR_UP
lift_target_floor   = 9

human_floor         = 3
human_in_lift       = True


os.system("cls")
while True:
    
    human_floor=int(input('\n\n------------\n\nWhere is the human? '))
    human_in_lift=input('Is human inside the lift?(y/n) ')=='y'
    call_lift = input('call the lift? y/n ')=='y'

    if call_lift:
        if not human_in_lift:
            lift_target_floor=human_floor
        else:
            lift_target_floor=int(input('Where to? '))
    lift_open=False        

    if lift_floor<lift_target_floor:
        speed=+1
        lift_dir=DIR_UP
    if lift_floor>lift_target_floor:
        speed=-1
        lift_dir=DIR_DOWN
    if lift_floor==lift_target_floor:
        speed=0    
    

    while True:
        lift_floor +=speed
        if lift_floor==lift_target_floor:
            lift_open=True
            lift_dir=DIR_STOP
        
        ###################-RENDER-FRAME-###########

        os.system("cls")
        
        if building_roof:
            a="     "
            if lift_floor==9:
                a=' < > '
                print(        "---|-----|----")
                print(       f" R |{a}|----")
            elif lift_floor!=9:
                print(        "---|-----|----")
                print(       f" R |{a}|----")  
        else:
            print(        "---|-----|----")    
        for floor in range(9,0,-1):
            t='     '
            a='     '
            s=''
            
            if floor==lift_floor+1:
                if lift_dir==DIR_DOWN:
                    a='  v  '
                elif lift_dir==DIR_UP:
                    a='  ^  '
                elif lift_dir==DIR_STOP and lift_open:
                    a=' < > '       
            elif floor==lift_floor:  #HW: omul dispare liftul
                a='|   |'
                t='|---|'
                if human_in_lift:
                    a='| H |'
                if human_in_lift and lift_target_floor==lift_floor:
                    a='|   |'
                    s="H"

                if human_floor == lift_floor and not human_in_lift:
                    s = "H"
                    
       


                
            elif floor==lift_floor-1:
                t='|---|'
            elif floor==human_floor:
                if not human_in_lift:
                    s="H"    
            print(       f"---|{t}|----")    
            
            print(f'{floor:^3}|{a}| {s}')    

            


        if building_parking and floor ==lift_floor:
            print(        '---||---||----')  
            print(        " P |     |----")
            print(        '---|-----|----')
        elif building_parking:
            print(        '---|     |----')  
            print(        " P |     |----")
            print(        '---|-----|----')
            
        else:     
            print(        '---|-----|----')   
        ###################-RENDER-FRAME-###########
            
        sleep(.5)
        if lift_floor==lift_target_floor:
            break

#HW3 - fix the bug with H dissappearing when lift arrives
#HW1 - fix the bug with lift bottom  + 
#HW2 - fix the bug with the lift indicator at floor 9 + 

#HW4 - add code when lift arrives -human exits +                 
    