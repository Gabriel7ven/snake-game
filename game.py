from food import Food
from turtle import *
from snake import Snake
from score import Score
import time



class Game():
    def __init__(self):
        self.screen = Screen()
        self.screen.title("Snake Game")
        self.screen.setup(width=900, height=700)
        self.is_on = True 
        self.score = Score(self.screen.window_height())
        self.snake = Snake()
        self.food  = Food(self.screen.window_width(),self.screen.window_height())
        self.screen.onkeypress(self.snake.go_up, "Up")
        self.screen.onkeypress(self.snake.go_down, "Down")
        self.screen.onkeypress(self.snake.go_left, "Left")
        self.screen.onkeypress(self.snake.go_right, "Right")

    def game_over(self):
        self.pen = Turtle()
        self.pen.hideturtle()
        self.pen.write(f"GAME OVER", align="center", font=("courier", 34, "bold"))








if __name__ == "__main__":
    game = Game()
    window_h = game.screen.window_height()
    window_w = game.screen.window_width()
    
    while game.is_on:
        game.screen.tracer(8,25)
        time.sleep(0.1)
        game.screen.listen()
        game.snake.move()

        if game.snake.detect_colision_with_food(game.food.current_position()) < 15:
            game.food.change_position()
            game.score.increase_score()
            game.snake.add_segment()
        
        game.snake.detect_colision_with_wall(window_h,window_w)
        game.is_on = game.snake.detect_colision_with_self()
        
    game.game_over()
    mainloop()