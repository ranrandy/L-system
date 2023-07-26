import turtle
from PIL import Image
import os


class LSystem2D:
    def __init__(
            self, axiom, rules, iterations, delta, FilePath, 
            initX, initY, imageWidth, imageHeight, 
            penColor, penColorIncrementStep, 
            penThickness, penThicknessDecrementStep, 
            penStep, hasLeaf):
        # For generating the sequence of characters
        self.axiom = axiom
        self.rules = rules
        self.iterations = iterations
        self.delta = delta
        self.saveFilePath = FilePath
        self.result = axiom

        # Screen settings
        self.screen = turtle.Screen()
        self.screen.setup(imageWidth, imageHeight)
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
        self.penColorIncrementStep = penColorIncrementStep

        self.penThickness = penThickness
        self.penThicknessDecrementStep = penThicknessDecrementStep

        self.penStep = penStep

        self.hasLeaf = hasLeaf
    
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
        stack = []
        self.t.left(90)
        self.t.pensize(self.penThickness)
        for chr in self.result:
            self.t.color(self.penColor)
            if chr == 'F':
                self.t.forward(self.penStep)
            elif chr == 'f':
                self.t.penup()
                self.t.forward(self.penStep)
                self.t.pendown()
            elif chr == '+':
                self.t.left(self.delta)
            elif chr == '-':
                self.t.right(self.delta)
            elif chr == '[':
                angle_, pos_ = self.t.heading(), self.t.pos()
                stack.append((angle_, pos_, self.penThickness, self.penStep, self.penColor[1]))
            elif chr == ']':
                angle_, pos_, self.penThickness, self.penStep, self.penColor[1] = stack.pop()
                self.t.pensize(self.penThickness)
                self.t.setheading(angle_)
                self.t.penup()
                self.t.goto(pos_)
                self.t.pendown()
            elif chr == '\'':
                self.penColor[1] += self.penColorIncrementStep
            elif chr == '!':
                self.penThickness -= self.penThicknessDecrementStep
        
    def save(self):
        self.screen.update()
        # Convert the PostScript file to PNG
        self.screen.getcanvas().postscript(file=f"{self.saveFilePath}.eps")
        img = Image.open(f"{self.saveFilePath}.eps")
        img.save(f"{self.saveFilePath}.png", "png", dpi=(5000, 5000))
        os.remove(f"{self.saveFilePath}.eps")

        turtle.done()


import networkx as nx
import numpy as np

class LSystem3D(LSystem2D):
    def init3D(self, initX, initY, initZ):
        self.G = nx.DiGraph()

        # Initialize heading, left, and up directions
        self.HLU = np.array([
            [0, 1, 0], # H
            [-1, 0, 0], # L
            [0, 0, 1]] # U
            ).T

        self.G.add_node("root", position=np.array([initX, initY, initZ]))
    
    # Set up the roll, pitch, and yaw matrices. 
    # These rotation matrices are relative to the current H, L, U matrices. 
    # So they are NOT fixed!!!!!!!!
    def R(self, axis, angle):
        axis = axis / np.linalg.norm(axis)

        # Compute the skew-symmetric matrix K for the axis
        K = np.array([[0, -axis[2], axis[1]],
                    [axis[2], 0, -axis[0]],
                    [-axis[1], axis[0], 0]])

        # Compute the rotation matrix using Rodrigues' rotation formula
        R = np.identity(3) + np.sin(angle) * K + (1 - np.cos(angle)) * np.dot(K, K)

        return R

    def generate_nodes_edges(self):
        stack = []

        last_node = "root"
        node_i = 0
        curr_node = f"node{node_i}"

        leaves = []
        leaf_colors = []
        curr_leaf_nodes = []

        for chr in self.result:
            if chr == '!':
                self.penThickness -= self.penThicknessDecrementStep
            elif chr == '\'':
                self.penColor += self.penColorIncrementStep
            elif chr == 'F':
                self.G.add_node(curr_node, position=(
                    self.G.nodes[last_node]["position"] + self.penStep * self.HLU[:, 0]
                ))
                self.G.add_edge(last_node, curr_node)
                self.G.edges[(last_node, curr_node)]["diameter"] = self.penThickness
                self.G.edges[(last_node, curr_node)]["color"] = self.penColor
                last_node = curr_node
                node_i += 1
                curr_node = f"node{node_i}"
            elif chr == 'f': # symbol f is used to bound the area of leaves
                if len(curr_leaf_nodes) == 0:
                    curr_leaf_nodes.append(
                        self.G.nodes[last_node]["position"] + self.penStep * self.HLU[:, 0]
                    )
                else:
                    curr_leaf_nodes.append(
                        curr_leaf_nodes[-1] + self.penStep * self.HLU[:, 0]
                    )
            elif chr == '+':
                self.HLU = self.R(self.HLU[:, 2], self.delta * np.pi / 180.0) @ self.HLU
            elif chr == '-':
                self.HLU = self.R(self.HLU[:, 2], -self.delta * np.pi / 180.0) @ self.HLU
            elif chr == '&':
                self.HLU = self.R(self.HLU[:, 1], self.delta * np.pi / 180.0) @ self.HLU
            elif chr == '^':
                self.HLU = self.R(self.HLU[:, 1], -self.delta * np.pi / 180.0) @ self.HLU
            elif chr == '/':
                self.HLU = self.R(self.HLU[:, 0], self.delta * np.pi / 180.0) @ self.HLU
            elif chr == '\\':
                self.HLU = self.R(self.HLU[:, 0], -self.delta * np.pi / 180.0) @ self.HLU
            elif chr == '|':
                self.HLU = self.R(self.HLU[:, 2], np.pi) @ self.HLU
            elif chr == '[':
                stack.append((self.HLU, self.penThickness, self.penStep, self.penColor.copy(), last_node))
            elif chr == ']':
                self.HLU, self.penThickness, self.penStep, self.penColor, last_node = stack.pop()
            elif chr == '}':
                leaves.append(curr_leaf_nodes) 
                curr_leaf_nodes = []
                leaf_colors.append([0.1, self.penColor[1] + 0.1, 0.1])
        self.leaves = leaves
        self.leaf_colors = leaf_colors

    def draw(self):
        # Draw trunk and branches
        for edge in self.G.edges:
            self.t.penup()
            self.t.goto(-self.G.nodes[edge[0]]["position"][2], self.G.nodes[edge[0]]["position"][1])
            self.t.pendown()
            self.t.pensize(self.G.edges[edge]["diameter"])
            self.t.pencolor(self.G.edges[edge]["color"])
            self.t.goto(-self.G.nodes[edge[1]]["position"][2], self.G.nodes[edge[1]]["position"][1])
        
        if self.hasLeaf:
            # Draw leaves
            self.t.penup()
            for leaf_nodes, leaf_color in zip(self.leaves, self.leaf_colors):
                self.t.begin_fill()
                self.t.fillcolor([0.1, leaf_color[1] + 0.1, 0.1])
                self.t.goto(leaf_nodes[0][00], leaf_nodes[0][1])
                for i in range(1, len(leaf_nodes)):
                    self.t.goto(leaf_nodes[i][0], leaf_nodes[i][1])
                self.t.goto(leaf_nodes[0][0], leaf_nodes[0][1])
                self.t.end_fill()


class LSystem3DParametric(LSystem3D):
    # Generate the list of parametric characters
    def apply_rules(self):
        result = []
        for tuple_i in self.result:
            mapping = self.rules.get(tuple_i[0])
            if mapping:
                # if len(tuple_i) == 1:
                #     result += mapping()
                # else:
                result += mapping(*tuple_i[1:])
            else:
                result.append(tuple_i)
        self.result = result

    def generate_lsystem(self):
        for _ in range(self.iterations):
            self.apply_rules()

    def generate_nodes_edges(self):
        stack = []

        last_node = "root"
        node_i = 0
        curr_node = f"node{node_i}"

        for tuple_i in self.result:
            if tuple_i[0] == '!':
                self.penThickness = tuple_i[1]
            elif tuple_i[0] == 'F':
                self.penStep = tuple_i[1]
                self.G.add_node(curr_node, position=(
                    self.G.nodes[last_node]["position"] + self.penStep * self.HLU[:, 0]
                ))
                self.G.add_edge(last_node, curr_node)
                self.G.edges[(last_node, curr_node)]["diameter"] = self.penThickness
                self.G.edges[(last_node, curr_node)]["color"] = self.penColor
                last_node = curr_node
                node_i += 1
                curr_node = f"node{node_i}"
            elif tuple_i[0] == 'f':
                self.penStep = tuple_i[1]
                self.G.add_node(curr_node, position=(
                    self.G.nodes[last_node]["position"] + self.penStep * self.H
                ))
                last_node = curr_node
                node_i += 1
                curr_node = f"node{node_i}"
            elif tuple_i[0] == '+':
                self.HLU = self.R(self.HLU[:, 2], tuple_i[1] * np.pi / 180.0) @ self.HLU
            elif tuple_i[0] == '-':
                self.HLU = self.R(self.HLU[:, 2], -tuple_i[1] * np.pi / 180.0) @ self.HLU
            elif tuple_i[0] == '&':
                self.HLU = self.R(self.HLU[:, 1], tuple_i[1] * np.pi / 180.0) @ self.HLU
            elif tuple_i[0] == '/':
                self.HLU = self.R(self.HLU[:, 0], tuple_i[1] * np.pi / 180.0) @ self.HLU
            elif tuple_i[0] == '$':
                V = np.array([0, 1, 0])
                L = np.cross(V, self.HLU[:, 0])
                L = L / np.linalg.norm(L)
                U = np.cross(self.HLU[:, 0], L)
                self.HLU = np.array([self.HLU[:, 0], L, U]).T
            elif tuple_i[0] == '[':
                stack.append((self.HLU, self.penThickness, self.penStep, self.penColor.copy(), last_node))
            elif tuple_i[0] == ']':
                self.HLU, self.penThickness, self.penStep, self.penColor, last_node = stack.pop()
