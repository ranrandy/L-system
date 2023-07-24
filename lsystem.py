import turtle
from PIL import Image
import os


class LSystem:
    def __init__(self, axiom, rules, iterations, delta, FilePath, initX, initY, penColor, penThickness, penStep):
        # For generating the sequence of characters
        self.axiom = axiom
        self.rules = rules
        self.iterations = iterations
        self.delta = delta
        self.saveFilePath = FilePath
        self.result = axiom

        # Screen settings
        self.screen = turtle.Screen()
        self.screen.setup(800, 1000)
        self.screen.delay(0)

        # turtle settings
        self.t = turtle.Turtle()
        self.t.hideturtle()
        turtle.tracer(0)
        self.t.speed(0)
        self.t.penup()
        self.t.setpos(initX, initY)
        self.t.pendown()

        # Pen settings
        self.penColor = penColor
        self.penThickness = penThickness
        self.penStep = penStep
    
    # Generate the sequence of characters
    def apply_rules(self):
        result = ""
        for char in self.result:
            result += self.rules.get(char, char)
        self.result = result
    
    def generate_lsystem(self):
        for _ in range(self.iterations):
            self.apply_rules()
    
    def draw(self):
        # Draw
        stack = []
        self.t.left(90)
        self.t.pensize(self.penThickness)
        for chr in self.result:
            self.t.color(self.penColor)
            if chr == 'F':
                self.t.forward(self.penStep)
            elif chr == '+':
                self.t.left(self.delta)
            elif chr == '-':
                self.t.right(self.delta)
            elif chr == '[':
                angle_, pos_ = self.t.heading(), self.t.pos()
                stack.append((angle_, pos_, self.penThickness, self.penStep, self.penColor))
            elif chr == ']':
                angle_, pos_, self.penThickness, self.penStep, self.penColor = stack.pop()
                self.t.pensize(self.penThickness)
                self.t.setheading(angle_)
                self.t.penup()
                self.t.goto(pos_)
                self.t.pendown()
        
    def save(self):
        # Convert the PostScript file to PNG
        self.screen.getcanvas().postscript(file=f"{self.saveFilePath}.eps")
        img = Image.open(f"{self.saveFilePath}.eps")
        img.save(f"{self.saveFilePath}.png", "png")
        os.remove(f"{self.saveFilePath}.eps")

        turtle.done()