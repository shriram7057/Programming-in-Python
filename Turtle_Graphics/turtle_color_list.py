 #turtle-color-list.py
import turtle
scr=turtle.Screen()
t=turtle.Turtle()
colors=['red','blue','green','orange']
for c in colors:
    t.pencolor(c)
    t.forward(50)
    t.right(90)
turtle.done()