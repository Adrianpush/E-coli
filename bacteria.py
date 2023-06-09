from turtle import Turtle
import random
import math

class Bacteria(Turtle):

    def __init__(self, color,target, xPos, yPos, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible, )

        self.x = xPos
        self.y = yPos
        self.target = target
        self.shade = color
        self.head_mods = {0: (1,0), 45: (1,1), 90: (0,1), 135:(-1,1), 180:(-1,0), 225:(-1,-1), 270:(0,-1), 315:(1,-1)}
        

        self.previous_gradient_strenght = math.sqrt(abs(self.target[0] - self.x) ** 2 + abs(self.target[1] - self.y) ** 2)
        self.current_gradient_strenght = self.previous_gradient_strenght

        self.penup()
        self.hideturtle()
        self.goto(x=self.x * 4, y= self.y * 4)
        self.color(self.shade, self.shade)
        self.showturtle()
        self.pendown()

    def rotate(self):
        self.setheading(random.choice((0,45,90, 135, 180, 225, 270, 315)))

    def _move_b_forword(self):

        h = self.heading()
        if h == 0:
            self.x += 1
        
        elif h == 45:
            self.x += 1
            self.y += 1

        elif h == 90:
            self.y += 1

        elif h == 135:
            self.y += 1
            self.x -= 1

        elif h == 180:
            self.x -= 1
            
        elif h == 225:
            self.x -= 1
            self.y -= 1

        elif h == 270:
            self.y -= 1

        elif h == 315:
            self.x += 1
            self.y -= 1
        
        self.goto(self.x * 4, self.y * 4)

    def move(self):
    
        rand_num = random.randint(0, 9)
        if self.current_gradient_strenght == self.previous_gradient_strenght:

            if rand_num < 5:
                self._move_b_forword()
            else:
                self.rotate()
        
        elif self.current_gradient_strenght <= self.previous_gradient_strenght:

            if rand_num < 8:
                self._move_b_forword()
            else:
                self.rotate()
                
        else:
            if rand_num < 8:
                self.rotate()
            else:
                self._move_b_forword()

    def evaluate_gradient(self):

        gradient_strenght_in_front = math.sqrt(abs(self.target[0] - (self.x + self.head_mods[self.heading()][0])) ** 2 + abs(self.target[1] - (self.y + self.head_mods[self.heading()][1])) ** 2)
        self.previous_gradient_strenght = math.sqrt(abs(self.target[0] - self.x) ** 2 + abs(self.target[1] - self.y) ** 2)
        self.current_gradient_strenght = gradient_strenght_in_front



