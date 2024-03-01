from turtle import Turtle, colormode
import random

colormode(255)

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        # Generating a random color each time the food is refreshed
        rand_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.color(rand_color) # Set the turtle to random color
        # moving the food to a random location
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
