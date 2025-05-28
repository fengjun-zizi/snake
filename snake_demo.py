import os 
import sys
import time
import pygame
from mygame.setting import * 

os.environ["SDL_VIDEO_CENTERED"] = "1"

GAME_NAME = "My Game"
SCREEN_SIZE = 640, 480
DISPLAY_MODE = pygame.HWSURFACE | pygame.DOUBLEBUF
LOOP_SPEED = 60
FONT_NAME = "resources/Minecraft.ttf"
FONT_SIZE = 16
KEY_PAUSE = pygame.K_p

class MyGame():
    """pygame模版类"""

    def __init__(self , **kwargs) :
        """初始化"""
        pygame.init()
        self.game_name = kwargs.get("game_name") or GAME_NAME
        pygame.display.set_caption(self.game_name)
        self.screen_size = kwargs.get("screen_size") or SCREEN_SIZE
        self.screen_width , self.screen_height = self.screen_size
        self.display_mode = kwargs.get("display_mode") or DISPLAY_MODE
        self.images = {}
        self.souds = {}
        self.musics = {}
        self.icon = kwargs.get("icon") or None
        self.icon and pygame.display.set_icon(pygame.image)