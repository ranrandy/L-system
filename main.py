from lsystem import LSystem2D, LSystem3D, LSystem3DParametric
from parameters import *
import os

if __name__ == "__main__":
    if dimension == 2:
        lsystem = LSystem2D(
            axiom, rules, iterations, delta, fileName, 
            initX, initY, imageWidth, imageHeight, 
            penColor, penColorIncrementStep, 
            penThickness, penThicknessDecrementStep, 
            penStep, hasLeaf)
    else: # dimension == 3:
        if parametric:
            lsystem = LSystem3DParametric(
                axiom, rules, iterations, delta, fileName, 
                initX, initY, imageWidth, imageHeight, 
                penColor, penColorIncrementStep, 
                penThickness, penThicknessDecrementStep, 
                penStep, hasLeaf)
        else:
            lsystem = LSystem3D(
                axiom, rules, iterations, delta, fileName, 
                initX, initY, imageWidth, imageHeight, 
                penColor, penColorIncrementStep, 
                penThickness, penThicknessDecrementStep, 
                penStep, hasLeaf)
        lsystem.init3D(initX, initY, initZ)

    lsystem.generate_lsystem()
    # print(lsystem.result)

    if dimension == 3:
        lsystem.generate_nodes_edges()

    lsystem.draw()
    lsystem.save()

    if hasLeaf:
        os.remove(f"{fileName}.png")
        print("Please save the screenshot by yourself." 
              + "Otherwise there exists some artifact when exporting from the Turtle library," 
              + "which I did not try to fix")