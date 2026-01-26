from turtle import *
import time

class Score():
    def __init__(self):
        self.score = 0
        self.pen = Turtle()
        self.pen.teleport(0, 350)
        self.pen.hideturtle()
        self.update_score()
        

    def update_score(self):
        self.pen.clear()
        self.pen.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()
        
    def reset_score(self):
        self.score = 0
        self.update_score()
        
        
        
if __name__ == "__main__":
    score = Score()
    mainloop()