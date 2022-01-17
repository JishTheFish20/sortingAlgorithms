from graphics import *
import random
import time
import algorithms


unSortedList = [5,1,8, 2, 6]

def main():
    win = GraphWin("Graphics Window", 500,500)
    createRectangles(unSortedList,win)
    win.getMouse()
    win.close()

def createRectangles(someList, win):
    names = []
    rects = []
    position = 40
    increment = (500 - position)/ len(someList)
    for x in range(len(someList)):
        names.append("rect" + str(x))
        names[x] = Rectangle(Point(position,150 - someList[x] * 10),Point(20 + position,400))
        print(names[x])
        position += increment
        color = color_rgb(225 - someList[x]*15,0,0)
        names[x].setFill(color)
        names[x].draw(win)
        rects.append([x, (names[x].getP1()).getX(), (names[x].getP1()).getY(), color])
    moveRetangles(rects, names, win)

def moveRetangles(rects, rectList, win):
    green = color_rgb(0,255,0)
    time.sleep(0.5)
    for x in range(len(rects)): # goes through the entire list

        for y in range(0, (len(rects) - x - 1)): # goes through the the list - x each time
           # print(rects[y][2], rects[y+1][2])
            if(rects[y][2] > rects[y+1][2]): # if pointer 1 > pointer 2 swap them
                print(rects[y][1], rects[y+1][1], rects[y][1] - rects[y+1][1])
                change = rects[y][1] - rects[y+1][1]


                #rectList[y].setFill(green)
                rectList[y].move(-change, 0)
                time.sleep(0.5)
                #rectList[y].setFill(rects[y][3])

                #rectList[y+1].setFill(green)
                rectList[y+1].move(change, 0)
                time.sleep(0.5)
                #rectList[y+1].setFill(rects[y+1][3])
                print(rectList)
                rects[y], rects[y+1] = rects[y+1], rects[y]

                print(rects)



main()


