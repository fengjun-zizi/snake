import pygame
from settings import * 

class Snake(object) :
    """贪吃蛇"""

    def __init__(self , game):
        self.game = game 
        self.sound_hit = pygame.mixer.Sound("resources/hit.wav")
        self.sound_eat = pygame.mixer.Sound("resources/eat.wav")
        self.game.add_draw_action(self.draw)
        self.respawn()

    def set_speed(self,speed) : 
        self._speed = speed
        interval = 1000 / self._speed
        self.game.add_game_action("snake.move" , self.move , interval)

    def get_speed(self) : 
        return self._speed 
    
    speed = property(get_speed , set_speed)

    def draw(self) :
        skin_color = SNAKE_COLOR_SKIN if self.alive else SNAKE_COLOR_SKIN_DEAD
        body_color = SNAKE_COLOR_BODY if self.alive else SNAKE_COLOR_BODY_DEAD
        head_color = SNAKE_COLOR_HEAD if self.alive else SNAKE_COLOR_HEAD_DEAD
        for cell in self.body : # 这里的cell是一个临时变量，不需要声明
            self.game.draw_cell(cell, CELL_SIZE , skin_color , body_color)

    def turn(self, **kwargs) : 
        if (self.direction in [LEFT  , RIGHT] and kwargs["direction"] in [UP , DOWN] or self.direction in [UP , DOWN] and kwargs["direction"] in [LEFT , RIGHT]) :
            self.new_direction = kwargs["direction"]
    
    def move(self) : 
        if self.alive : 
            #设定方向
            self.direction = self.new_direction
            x , y = meeting = (self.head[0] + self.direction[0],
                               self.head[1] + self.direction[1])
            
            if (meeting in self.body or x not in range(COLUMNS) or y not in range(ROWS)) : 
                self.die()
                return
            
            if meeting == (self.game.apple.x , self.game.apple.y):
                self.sound_eat.play()
                self.game.apple.drop()
                self.game.apple_counter += 1
            else : 
                self.body.pop()

            self.body = [self.head] + self.body
            self.head = meeting 

    def respawn(self) :
        """重生"""
        self.head = (SNAKE_X , SNAKE_Y) 
        self.body = [(-1,-1)] * SNAKE_BODY_LENGTH
        self.direction = SNAKE_DIRECTION
        self.new_direction = SNAKE_DIRECTION
        self.speed = SNAKE_SPEED
        self.alive = True 

    def die(self) :
        self.sound_hit.play()
        self.alive = False
