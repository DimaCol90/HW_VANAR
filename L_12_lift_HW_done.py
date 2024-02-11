
import os
DIR_UP              =-1
DIR_STOP=           0
DIR_DOWN            =1


building_roof       =True
building_floors     =9
building_parking    =True

lift_floor          =9
lift_open           =False
lift_dir            =DIR_DOWN

human_floor         =7
human_in_lift       =False


###################-RENDER-FRAME-###########

os.system("cls")
if building_roof:
    print(        "---|-----|----")
    print(        ' R |     |----')
else:
    print(        "---|-----|----")    
for floor in range(9,0,-1):
    if floor ==lift_floor-1:
        b='|---|'
    else:
        b='     ' 
    if floor ==lift_floor:
        b='|---|'
    
  
    print(        f"---|{b}|----")
    
    if floor==human_floor and not human_in_lift:
        h= ' H '
        
    else:
        h= "   "

   
    if floor==lift_floor+1:
        if lift_open:
            l=           ' < > '
        else:
            if lift_dir==DIR_UP:
                l='  ^  '
            elif lift_dir==DIR_DOWN:
                l='  v  '        
            else:    
                l=            '     '
                
    else:
        l=            '     '    
    if floor==lift_floor:
        l=           '|   |'
    if floor==lift_floor and human_in_lift:
        l      =     '| H |'  

    print(f'{floor:^3}|{l}|{h}')


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
    

#HW1: logic for no roof and no parking + 
#HW2: human in and out of lift
#HW3: write the logic for the lift top. + 