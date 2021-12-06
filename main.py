from graphics import *
import random


unSortedList = [5,2,8,4,10,1,3]

def main():
    win = GraphWin("Graphics Window", 500,500)
    #c = Circle(Point(50,50), 10)
    # rect = Rectangle(Point(10,100),Point(100,400))
    # rect.setFill("Red")
    # rect.draw(win)
    createRectangles(unSortedList,win)
    #c.draw(win)
    win.getMouse()
    win.close()

def createRectangles(someList, win):
    position = 0
    for x in range(len(someList)):
        print(random.randrange(3, 9))
        position = random.randrange(10, 450, 2)
        print(position)
        rect = Rectangle(Point(position,100+x*20),Point(20 + position,400))
        color = color_rgb(225 - x*20,0,0)
        rect.setFill(color)
        rect.draw(win)

main()


