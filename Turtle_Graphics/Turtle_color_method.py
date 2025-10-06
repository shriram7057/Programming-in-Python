#turtle-color1.py
import turtle
pen = turtle.Turtle()
pen.color("red")   # Set pen and fill color to red
    
pen.begin_fill()    # Draw a square with red lines and fill

for _ in range(4):
 pen.forward(100)
 pen.left(90)
 pen.end_fill()
 pen.color("blue", "green") # Draw a square with red lines and fill

 # Move the turtle and draw a circle with blue outline and green fill
 pen.penup()
 pen.goto(150, 0)
 pen.pendown()
 pen.begin_fill()
 pen.circle(50)
 pen.end_fill()
 current_colors= pen.color() # Get the current colors
 print(current_colors)  
# Output: ('blue', 'green')
 turtle.done()