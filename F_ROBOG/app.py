from map import *
from ui import *
import time


while True:
    clear()
    printMap(gameMap)
    key=controls()

    if key=="x":
        break

    gameMap[rr][rc]=0

    if key == "d" and rc + 1 < len(gameMap[rr]) and gameMap[rr][rc + 1] != 1:
        rc += 1

    if key == "a" and rc - 1 >= 0 and gameMap[rr][rc - 1] != 1:
        rc -= 1

    if key == "s" and rr + 1 < len(gameMap) and gameMap[rr + 1][rc] != 1:
        rr += 1

    if key == "w" and rr - 1 >= 0 and gameMap[rr - 1][rc] != 1:
        rr -= 1

    
    gameMap[rr][rc]=2





    #when moving -> radar rc+1, rc+2 - not a mine 
    # in case of danger -> warning         
