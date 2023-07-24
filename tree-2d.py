import turtle
from PIL import Image
import os

axiom = "F"
rules = {
    "F": "FF-[-F+F+F]+[+F-F-F]",
}
iterations = 4
delta = 22.5

def generate_lsystem(axiom, rules, iterations):
    def apply_rules(axiom, rules):
        result = ""
        for char in axiom:
            result += rules.get(char, char)
        return result
    for _ in range(iterations):
        axiom = apply_rules(axiom, rules)
    return axiom

def draw_lsystem(axiom):
    # Screen settings
    screen = turtle.Screen()
    screen.setup(800, 1000)
    screen.delay(0)

    # turtle settings
    t = turtle.Turtle()
    t.hideturtle()
    turtle.tracer(0)
    t.speed(0)
    t.penup()
    t.setpos(-50, -490)
    t.pendown()
    t.color('green')

    # Pen settings
    color = [0.35, 0.2, 0.0]
    thickness = 2
    step = 18

    # Draw
    stack = []
    t.left(90)
    t.pensize(thickness)
    for chr in axiom:
        t.color(color)
        if chr == 'F':
            t.forward(step)
        elif chr == '+':
            t.left(delta)
        elif chr == '-':
            t.right(delta)
        elif chr == '[':
            angle_, pos_ = t.heading(), t.pos()
            stack.append((angle_, pos_, thickness, step, color[1]))
        elif chr == ']':
            angle_, pos_, thickness, step, color[1] = stack.pop()
            t.pensize(thickness)
            t.setheading(angle_)
            t.penup()
            t.goto(pos_)
            t.pendown()
    
    # Convert the PostScript file to PNG
    screen.getcanvas().postscript(file="l_system_tree_2d.eps")
    img = Image.open("l_system_tree_2d.eps")
    img.save("l_system_tree_2d.png", "png")
    os.remove("l_system_tree_2d.eps")

    turtle.done()

if __name__ == "__main__":
    lsystem = generate_lsystem(axiom, rules, iterations)
    draw_lsystem(lsystem)
