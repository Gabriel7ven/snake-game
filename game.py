from food import Food
from turtle import *
from snake import Snake
from score import Score
import time



class Game():
    def __init__(self):
        self.screen = Screen()
        self.screen.title("Snake Game")
        self.screen.setup(width=900, height=800)
        self.is_on = True 
        self.score = Score()
        self.snake = Snake()
        self.food = Food()
        self.screen.onkeypress(self.snake.go_up, "Up")
        self.screen.onkeypress(self.snake.go_down, "Down")
        self.screen.onkeypress(self.snake.go_left, "Left")
        self.screen.onkeypress(self.snake.go_right, "Right")


        
if __name__ == "__main__":
    game = Game()
    while game.is_on:
        game.screen.tracer(8)
        time.sleep(0.1)
        game.screen.listen()
        game.snake.move()
        
        # detecting collision
        if game.snake.detect_colision_with_food(game.food.current_position()) < 15:
            game.food.change_position()
            game.score.increase_score()
            game.snake.add_segment()
        
        
    