from graphics import *

def main():
    win = GraphWin("Graphics Window", 500,500)
    #c = Circle(Point(50,50), 10)
    # rect = Rectangle(Point(10,100),Point(100,400))
    # rect.setFill("Red")
    # rect.draw(win)
    createRectangles(4,win)
    #c.draw(win)
    win.getMouse()
    win.close()

def createRectangles(num, win):
    for x in range(num):
        rect = Rectangle(Point(10+50*x,100),Point(20+50*x,400))
        rect.setFill("red"+str(x+1))
        rect.draw(win)

main()


