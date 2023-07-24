import turtle
from PIL import Image
import os

axiom = "X"
rules = {
    "X": "F-[[X]+X]+F[+FX]-X",
    "F": "FF"
}
iterations = 5
delta = 22.5
fileName = "l_system_tree_2d_f"

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
    color = [0.0, 0.0, 0.0]
    thickness = 2
    step = 16

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
    screen.getcanvas().postscript(file=f"{fileName}.eps")
    img = Image.open(f"{fileName}.eps")
    img.save(f"{fileName}.png", "png")
    os.remove(f"{fileName}.eps")

    turtle.done()

if __name__ == "__main__":
    lsystem = generate_lsystem(axiom, rules, iterations)
    draw_lsystem(lsystem)
