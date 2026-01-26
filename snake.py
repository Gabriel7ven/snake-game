from turtle import *
import time
import random


class Snake():
    def __init__(self):
        self.body = []
        self.speed = 20
        self.length = 3
        self.create_snake()
        
        
     
    def get_positions(self):
        return [segment.position() for segment in self.body]

    def move(self):
        positions = self.get_positions()
        self.body[0].fd(20)
        for i in range(1, len(self.body)):
            self.body[i].goto(positions[i-1])  
    
    def accelerate(self):
        self.speed += 5
       
    def create_snake(self):
        colors = ["blue","yellow","black","gray","red","green","brown","pink"]
        for i in range(self.length):
            segment = Turtle()
            segment.shape("square")
            segment.penup()
            segment.teleport(-i * 20, 0)
            segment.color(colors[random.randint(0, len(colors))])
            self.body.append(segment)
    
    def detect_colision_with_food(self, food_position):
        return self.body[0].distance(food_position)
            
    def go_up(self):
        print('up')
        self.body[0].setheading(90)
                    
    def go_down(self):
        print('down')
        self.body[0].setheading(270)
        
    def go_left(self):      
        print('left')
        self.body[0].setheading(180)
        
    def go_right(self):
        print('right')
        self.body[0].setheading(0)
    
    
        
if __name__ == "__main__":
    snake = Snake()

    while True:
        time.sleep(0.5)
        snake.move()
   

    