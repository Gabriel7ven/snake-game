from turtle import *
import time
import random

class Snake():
    def __init__(self):
        self.body = []
        self.speed = 20
        self.length = 2
        self.create_snake()
        self.head = self.body[0]
        
    def get_positions(self):
        return [segment.position() for segment in self.body]

    def move(self):
        positions = self.get_positions()
        self.head.fd(20)
        for i in range(1, len(self.body)):
            self.body[i].goto(positions[i-1])  
    
    def accelerate(self):
        self.speed += 5
    def create_snake(self):
        # colors = ["blue","yellow","black","gray","red","green","brown","pink"]
        for i in range(self.length):
            segment = Turtle()
            segment.shape("square")
            segment.penup()
            segment.teleport(-i * 20, 0)
            # segment.color(colors[random.randint(0, len(colors)-1)])
            self.body.append(segment)
    
    def detect_colision_with_food(self, food_position):
        return self.head.distance(food_position)
    
    def detect_colision_with_wall(self,screen_h,screen_w):
        if self.head.xcor() > screen_w / 2 or self.head.xcor() < -1 * (screen_w / 2):
            self.head.setx(-1 * self.head.xcor())
        elif self.head.ycor() > screen_h / 2 or self.head.ycor() < -1 * (screen_h / 2):
            self.head.sety(-1 * self.head.ycor())

    def detect_colision_with_self(self):
        for i in range(1,len(self.body)):
            if self.head.distance(self.body[i].position()) < 1:
                return False
        return True
    
    def add_segment(self):
        segment = Turtle()
        segment.shape("square")
        segment.penup()
        segment.goto(self.get_positions()[len(self.body)-1])
        self.body.append(segment)
        
    def go_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
                    
    def go_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
        
    def go_left(self):      
        if self.head.heading() != 0:
            self.head.setheading(180)
        
    def go_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
    
    
        
if __name__ == "__main__":
    snake = Snake()

    while True:
        time.sleep(0.1)
        snake.move()

    