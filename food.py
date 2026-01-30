from turtle import *
import random
import time



class Food():
    def __init__(self,screen_w,screen_h):
        self.food = Turtle()
        self.food.shape("circle")
        self.food.shapesize(0.5,0.5,0.5)
        self.screen_w = screen_w
        self.screen_h = screen_h
        self.change_position()
        
    def change_position(self):
        random_x = random.randint(int(-0.45 * self.screen_w), int(0.45 * self.screen_w))
        random_y = random.randint(int(-0.35 * self.screen_h), int(0.35 * self.screen_h))
        self.food.teleport(random_x, random_y)
        
    def current_position(self):
        return self.food.position()
        
        
        
if __name__ == "__main__":
    food = Food()
    mainloop()