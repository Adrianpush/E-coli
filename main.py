from turtle import Turtle, Screen
from bacteria import Bacteria
import random
from collections import defaultdict


screen = Screen()
screen.bgcolor("white")
screen.setup(1000, 1000)
screen.title("E-Coli behaviour")

c = ["red", "blue", "green", "yellow"]
bacterias = []

for col in c:
    bacteria = Bacteria(color=col, target=[0,0], xPos=random.randint(-100, 100), yPos=random.randint(-100, 100))
    bacterias.append(bacteria)


paths = defaultdict(list)

gradient_values = [bacteria.current_gradient_strenght for bacteria in bacterias]

while sum(gradient_values) != 0:

    for i, bacteria in enumerate(bacterias):

        if bacteria.current_gradient_strenght != 0:
            bacteria.evaluate_gradient()
            bacteria.move()
            paths[bacteria.shade].append((bacteria.x, bacteria.y))
            

    gradient_values = [bacteria.current_gradient_strenght for bacteria in bacterias]

for path in paths:
    print(f"{path} arrived at target in {len(paths[path])} moves.")






screen.exitonclick()