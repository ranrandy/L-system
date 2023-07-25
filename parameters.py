import numpy as np

###### Figure 1.24
# axiom = "X"
# rules = {
#     "X": "F-[[X]+X]+F[+FX]-X",
#     "F": "FF"
# }
# iterations = 5
# delta = 22.5
# fileName = "outputs/l_system_tree_2d_f"

# initX = -50
# initY = -490

# imageWidth = 800
# imageHeight = 1000

# penColor = [0.0, 0.0, 0.0]
# penColorIncrementStep = 0.04

# penThickness = 2
# penThicknessDecrementStep = 0.2
# penStep = 16

# dimension = 2



###### Figure 1.25
axiom = "A"
rules = {
    "A": "[&&FL!A]/////'[&FL!A]///////'[&FL!A]",
    "F": "S/////F",
    "S": "FL",
    "L": "['''^^{-f+f+f-|-f+f+f}]"
}
iterations = 7
delta = 22.5
fileName = "outputs/l_system_tree_3d_Figure_1_25"

initX = -20
initY = -370
initZ = 0

imageWidth = 1000
imageHeight = 800

penColor = np.array([0.2, 0.1, 0.03])
penColorIncrementStep = 0.03

penThickness = 10
penThicknessDecrementStep = 1.2
penStep = 23

dimension = 3
parametric = False
hasLeaf = True




###### Chapter 2 Modeling of Trees
# axiom = [("!", 1), ("F", 200), ("A")] 
# d1 = 94.97
# d2 = 132.63
# a = 18.95
# lr = 1.109
# vr = 1.732
# rules = {
#     "A": lambda : [("!", vr), ("F", 50), 
#                    ("["), ("&", a), ("F", 50), ("A"), ("]"),
#                    ("/", d1),
#                    ("["), ("&", a), ("F", 50), ("A"), ("]"),
#                    ("/", d2),
#                    ("["), ("&", a), ("F", 50), ("A"), ("]"),
#                    ("A")], 
#     "F": lambda step : ("F", step * lr),
#     "!": lambda width : ("!", width * vr)
# }
# iterations = 4
# delta = 22.5
# fileName = "outputs/l_system_tree_3d_a"

# initX = -50
# initY = -490
# initZ = 0

# imageWidth = 1000
# imageHeight = 1000

# penColor = [0.01, 0.1, 0.01]
# penColorIncrementStep = 0.04

# penThickness = 2
# penThicknessDecrementStep = 0.2
# penStep = 16

# dimension = 3
# parametric = True
