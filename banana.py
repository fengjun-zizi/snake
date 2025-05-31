from random import randint
from settings import * 
class Banana (): 
    """香蕉类"""
    def __init__(self, game) :
        self.game = game
        self.x = self.y = 0 
        self.game.add_draw_action(self.draw)
        self.drop()

    def drop (self) : 
        snake = self.game.snake.body + [self.game.snake.head]
        while True : 
            (x , y ) = randint ( 0 , COLUMNS - 3  ) , randint ( 0 , ROWS - 3 )
            if (x , y ) not in snake : 
                self.x , self.y = x , y 
                break 

    def draw (self) :
        self.game.draw_cell( (self.x , self.y) , CELL_SIZE , BANANA_COLOR_SKIN , BANANA_COLOR_BODY)
