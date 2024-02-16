import os
import time
option = ""
over = False
robox = 5
hp = 100
gmap = ['  ', '  ', '  ', '  ', '❗ ', '🤖 ', '  ', '  ', '  ', '❗ ']  # the map -> 10 values

print('-' * 20)

while option != 'x':
    os.system("cls")
    print('-' * 20)

    # PRINT THE MAP
    for i in range(len(gmap)):
        print(gmap[i], end="")

    print()
    print('-' * 20)

    for i in range(len(gmap)):
        print(i, end=" ")

    print(f"\n\nHP: {hp}")

    print("""\n\nCONTROLS:
    a-left 
    d-right
    q-quit game           
        """)
    # CONTROLS
    if over:
        print("You failed this simple game")
        break
    option = input(">> ").lower()

    if option == "a":
        if robox > 0:  
            gmap[robox] = "  "  # remove from current position
            robox -= 1
            if gmap[robox] == "❗ ":
                gmap[robox] = "🕱 "
                hp -= 50
                print("GAME OVER")
                if hp <= 0:
                    print("Your HP reached 0!")
                    time.sleep(2)
                    over = True
                else:
                    print("You lost 50 HP!")
            else:
                gmap[robox] = "🤖 "
        else:
            print("Cannot move further left!")
    elif option == "d":
        if robox < len(gmap) - 1:  
            gmap[robox] = "  "  # remove from current position
            robox += 1
            if gmap[robox] == "❗ ":
                gmap[robox] = "🕱 "
                hp -= 50
                print("GAME OVER")
                if hp <= 0:
                    print("Your HP reached 0!")
                    time.sleep(2)
                    over = True
                else:
                    print("You lost 50 HP!")
            else:
                gmap[robox] = "🤖 "
        else:
            print("Cannot move further right!")
    elif option == "x":
        print("game over")