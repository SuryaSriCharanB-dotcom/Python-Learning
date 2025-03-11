import turtle
import colorsys

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")

# Setup turtle
t = turtle.Turtle()
t.speed(0)
t.width(2)
turtle.colormode(255)

# Generate colors
colors = [colorsys.hsv_to_rgb(i/100.0, 1, 1) for i in range(100)]
colors = [(int(r*255), int(g*255), int(b*255)) for r, g, b in colors]

# Draw spiral
for i in range(400):
    t.pencolor(colors[i % 100])
    t.forward(i * 2)
    t.right(59)
    t.forward(i * 2)
    t.right(59)

# Hide turtle and finish
t.hideturtle()
turtle.done()
