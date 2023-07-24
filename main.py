from lsystem import LSystem
from parameters import *

if __name__ == "__main__":
    lsystem = LSystem(axiom, rules, iterations, delta, fileName, initX, initY, penColor, penThickness, penStep)
    lsystem.generate_lsystem()
    lsystem.draw()
    lsystem.save()