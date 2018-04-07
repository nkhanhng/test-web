from random import choice
import os

w = 4
h = 4

px = 1
py = 1

f1x = 0
f1y = 0
hasFood1 = False

f2x = 1
f2y = 0
hasFood2 = False

f3x = 2
f3y = 3
hasFood3 = False

count_food = 3

g1x = 3
g1y = 0

g2x = 3
g2y = 3

def map():
    for y in range(h):
        for x in range(w):
            if x == px and y == py:
                if px == g1x and py == g1y:
                    print("G",end=' ')
                elif px == g2x and py == g2y:
                    print("G",end=' ')
                else:
                    print("P",end=' ')
            elif x == f1x and y == f1y and not hasFood1:
                if g1x == f1x and g1y == f1y:
                    print("G",end=' ')
                elif g2x == f1x and g2y == f1y:
                    print("G",end=' ')
                else:
                    print("F",end=' ')
            elif x == f2x and y == f2y and not hasFood2:
                if g1x == f2x and g1y == f2y:
                    print("G",end=' ')
                elif g2x == f2x and g2y == f2y:
                    print("G",end=' ')
                else:
                    print("F",end=' ')
            elif x == f3x and y == f3y and not hasFood3:
                if g1x == f3x and g1y == f3y:
                    print("G",end=' ')
                elif g2x == f3x and g2y == f3y:
                    print("G",end=' ')
                else:
                    print("F",end=' ')
            elif x == g1x and y == g1y:
                print("G",end=' ')
            elif x == g2x and y == g2y:
                print("G",end=' ')
            else:
                print("-",end=' ')
        print()


while True:
    map()
    move = input("Your move: ").upper()

    vx = 0
    vy = 0

    g1vx = 0
    g1vy = 0

    g2vx = 0
    g2vy = 0

    pre_g1x = g1x
    pre_g1y = g1y

    if move == "W":
        vy = -1
        g1vx = choice([-1,1])
        g2vy = choice([-1,1])
    elif move == "S":
        vy = 1
        g1vy = choice([-1,1])
        g2vx = choice([-1,1])
    elif move == "A":
        vx = -1
        g1vx = choice([-1,1])
        g2vx = choice([-1,1])
    elif move == "D":
        vx = 1
        g1vy = choice([-1,1])
        g2vy = choice([-1,1])

    nextX = px + vx
    nextY = py + vy

    if nextX < 0:
        nextX = 0
    if nextX >= w:
        nextX = w - 1
    if nextY < 0:
        nextY = 0
    if nextY >= h:
        nextY = h - 1

    px = nextX
    py = nextY

    #ghost1
    newG1x = g1x + g1vx
    newG1y = g1y + g1vy

    if newG1x < 0:
        newG1x = 0
    if newG1x == w:
        newG1x = w - 1
    if newG1y < 0:
        newG1y = 0
    if newG1y == h:
        newG1y = h - 1

    g1x = newG1x
    g1y = newG1y

    #ghost2
    newG2x = g2x + g2vx
    newG2y = g2y + g2vy

    if newG2x < 0:
        newG2x = 0
    if newG2x == w:
        newG2x = w - 1
    if newG2y < 0:
        newG2y = 0
    if newG2y == h:
        newG2y = h - 1

    g2x = newG2x
    g2y = newG2y

    #check collision
    if g1x == g2x and g1y == g2y:
        g1x = pre_g1x
        g1y = pre_g1y
    if px == g1x and py == g1y:
        print("You lost!")
        map()
        break
    elif px == g2x and py == g2y:
        print("You lost!")
        map()
        break

    #get food
    if px == f1x and py == f1y:
        hasFood1 = True
    if px == f2x and py == f2y:
        hasFood2 = True
    if px == f3x and py == f3y:
        hasFood3 = True

    if hasFood1 and hasFood2 and hasFood3:
        print("You won!")
        break
