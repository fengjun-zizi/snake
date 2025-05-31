from apple import * 
from banana import * 
from settings import * 
from snake_demo import *
from snake import *
import pygame


class PySnake(MyGame) :
    """贪吃蛇小游戏"""
    
    def __init__(self):
        """初始化"""
        super().__init__(game_name=GAME_NAME, icon=ICON,
                                      screen_size=SCREEN_SIZE,
                                      display_mode=DISPLAY_MODE,
                                      loop_speed=LOOP_SPEED,
                                      font_name=FONT_NAME,
                                      font_size=FONT_SIZE,
                                      background=WHITE)
        
        self.prepare_background()
        self.apple_counter = 0 
        self.banana_counter = 0 
        self.hightest_score = 0 
       
        self.snake = Snake(self)
        self.apple = Apple(self)
        self.banana = Banana(self)

        self.add_key_binding(KEY_UP , self.snake.turn , direction = UP )
        self.add_key_binding(KEY_DOWN, self.snake.turn, direction=DOWN)
        self.add_key_binding(KEY_LEFT, self.snake.turn, direction=LEFT)
        self.add_key_binding(KEY_RIGHT, self.snake.turn, direction=RIGHT)
        self.add_key_binding(KEY_RESTART, self.restart)
        self.add_key_binding(KEY_EXIT, self.quit)

        self.add_draw_action(self.draw_score)

    def prepare_background(self):
        self.background.fill(BACKGROUND_COLOR)
        for _ in range(CELL_SIZE, SCREEN_WIDTH, CELL_SIZE):
            self.draw.line(self.background, GRID_COLOR,
                           (_, 0), (_, SCREEN_HEIGHT))
        for _ in range(CELL_SIZE, SCREEN_HEIGHT, CELL_SIZE):
            self.draw.line(self.background, GRID_COLOR,
                           (0, _), (SCREEN_WIDTH, _))
            
    def restart(self) : 
        if not self.snake.alive :
            self.apple_counter = 0 
            self.banana_counter = 0 
            self.apple.drop()
            self.snake.respawn()
            self.running = True

    def draw_score(self) : 
        text_1 = "Apple %d"  % self.apple_counter # 这行语句的意思是什么？？
        text_2 = "Banana %d" % self.banana_counter 
        self.score = self.apple_counter + ( self.banana_counter * 2 )
        text_3 = "Score : %d " % self.score
        self.hightest_score = max(self.hightest_score, self.score) # 更新最高分
        self.draw_text(text_1, ( 0 , 0 ) , (255 , 255, 33)) # 绘画分数
        self.draw_text(text_2 , (0 , 20 ) , (255 , 255 , 35 ))
        self.draw_text(text_3 , (0 , 40 ) , (255 , 160 , 100))
         
        if not self.snake.alive:  # 如果这个蛇死了
            self.draw_text("GAME OVER", (SCREEN_WIDTH / 2 - 54, SCREEN_HEIGHT / 2 - 10), (255, 33, 33), WHITE)
            self.draw_text(" press R to restart ",
                           (SCREEN_WIDTH / 2 - 85, SCREEN_HEIGHT / 2 + 20),
                           GREY, DARK_GREY)

            self.draw_text("Current highest score : %d" % self.hightest_score,
                           (SCREEN_WIDTH / 2 - 114, SCREEN_HEIGHT / 2 + 50),
                           (255, 33, 33), WHITE)  # 展示最高分

        if not self.running and self.snake.alive: #运行（暂停），但是蛇还活着
            self.draw_text(" GAME PAUSED ",
                           (SCREEN_WIDTH / 2 - 55, SCREEN_HEIGHT / 2 - 10),
                           LIGHT_GREY, DARK_GREY)
            
if __name__ == '__main__' :
    PySnake().run()