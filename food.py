from turtle import *
import random
import time



class Food():
    def __init__(self):
        self.food = Turtle()
        self.food.shape("circle")
        self.food.shapesize(0.5,0.5,0.5)
        # self.food.shapesize(10,10,10)

        
    def change_position(self):
        random_x = random.randint(-380, 380)
        random_y = random.randint(-380, 380)
        self.food.teleport(random_x, random_y)
        
    def current_position(self):
        return self.food.position()
        
        
        
if __name__ == "__main__":
    food = Food()
    mainloop()