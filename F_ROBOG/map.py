#this module contains the map logic

rr=4
rc=1

mr=0
mc=0

gameMap=[
    [0,0,0,0,0,0,0,0,0,0],
    [1,1,1,1,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,1,1,1,0,0,1],
    [0,0,0,0,0,1,0,0,0,1],
    [1,1,1,1,0,1,0,0,0,0],
    [0,0,0,0,0,1,0,0,0,0],
    [0,0,0,0,0,1,0,0,0,1],
    [0,0,0,0,0,0,0,0,0,1]
    ]

gameMap[rr][rc]=2
gameMap[mr][mc]=3

def p(c):
    print(c+" ",end="")

def printMap(m):
    for ri in range(10):
        for ci in range(10):
            p(".") if m[ri][ci]==0 else None
            p("#") if m[ri][ci]==1 else None
            p("R") if m[ri][ci]==2 else None
            p("x") if m[ri][ci]==3 else None
        print()            