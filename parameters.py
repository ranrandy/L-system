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
# axiom = "A"
# rules = {
#     "A": "[&&FL!A]/////'[&FL!A]///////'[&FL!A]",
#     "F": "S/////F",
#     "S": "FL",
#     "L": "['''^^{-f+f+f-|-f+f+f}]"
# }
# iterations = 7
# delta = 22.5
# fileName = "outputs/l_system_tree_3d_Figure_1_25"

# initX = -20
# initY = -370
# initZ = 0

# imageWidth = 1000
# imageHeight = 800

# penColor = np.array([0.2, 0.1, 0.03])
# penColorIncrementStep = 0.03

# penThickness = 10
# penThicknessDecrementStep = 1.2
# penStep = 23

# dimension = 3
# parametric = False
# hasLeaf = True




###### Chapter 2 Modeling of Trees
# ###### Figure 2.6
# axiom = [("A", 80, 20)]
# r1 = 0.9
# r2 = 0.7
# a0 = 30
# a2 = -30
# d = 137.5
# wr = 0.707
# rules = {
#     "A": lambda l, w: [("!", w), ("F", l), 
#                        ("["), ("&", a0), ("B", l * r2, w * wr), ("]"),
#                        ("/", d), ("A", l * r1, w * wr)],
#     "B": lambda l, w: [("!", w), ("F", l), 
#                        ("["), ("-", a2), ("$"), ("C", l * r2, w * wr), ("]"),
#                        ("C", l * r1, w * wr)],
#     "C": lambda l, w: [("!", w), ("F", l), 
#                        ("["), ("+", a2), ("$"), ("B", l * r2, w * wr), ("]"),
#                        ("B", l * r1, w * wr)],
# }
# iterations = 10
# delta = None
# fileName = "outputs/l_system_tree_3d_Figure_2_6_d"

# initX = 0
# initY = -270
# initZ = 0

# imageWidth = 600
# imageHeight = 600

# penColor = [0, 0, 0]
# penColorIncrementStep = None
# penThickness = None
# penThicknessDecrementStep = None
# penStep = None

# dimension = 3
# parametric = True
# hasLeaf = False



###### Figure 2.7
axiom = [("A", 100, 20)]
r1 = 0.9
r2 = 0.8
a1 = 35
a2 = 35
wr = 0.707
rules = {
    "A": lambda l, w: [("!", w), ("F", l), 
                       ("["), ("&", a1), ("B", l * r1, w * wr), ("]"),
                       ("/", 180), 
                       ("["), ("&", a2), ("B", l * r2, w * wr), ("]")],
    "B": lambda l, w: [("!", w), ("F", l), 
                       ("["), ("+", a1), ("$"), ("B", l * r1, w * wr), ("]"),
                       ("["), ("-", a2), ("$"), ("B", l * r2, w * wr), ("]")]
}
iterations = 10
delta = None
fileName = "outputs/l_system_tree_3d_Figure_2_7_d"

initX = 0
initY = -270
initZ = 0

imageWidth = 600
imageHeight = 600

penColor = [0, 0, 0]
penColorIncrementStep = None
penThickness = None
penThicknessDecrementStep = None
penStep = None

dimension = 3
parametric = True
hasLeaf = False



# ###### Figure 2.8
# axiom = [("!", 1/2), ("F", 200/2), ("/", 45/2), ("A")] 
# d1 = 94.97
# d2 = 132.63
# a = 18.95
# lr = 1.109
# vr = 1.732
# rules = {
#     "A": lambda : [("!", vr/2), ("F", 50/2), 
#                    ("["), ("&", a), ("F", 50/2), ("A"), ("]"),
#                    ("/", d1),
#                    ("["), ("&", a), ("F", 50/2), ("A"), ("]"),
#                    ("/", d2),
#                    ("["), ("&", a), ("F", 50/2), ("A"), ("]")], 
#     "F": lambda step : [("F", step * lr)],
#     "!": lambda width : [("!", width * vr)]
# }
# iterations = 6
# delta = None
# fileName = "outputs/l_system_tree_3d_Figure_2_8_a"

# initX = 0
# initY = -280
# initZ = 0

# imageWidth = 550
# imageHeight = 600

# penColor = [0, 0, 0]
# penColorIncrementStep = None
# penThickness = None
# penThicknessDecrementStep = None
# penStep = None

# dimension = 3
# parametric = True
# hasLeaf = False
