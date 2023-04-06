from pygame.sprite import Sprite

import random

from dino_runner.utils.constants import SCREEN_WIDTH


class PowerUp(Sprite):
    #1er parametro: es la imagen
    # segundo parametro el tipo(tipo de dato cadena)
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = random.randint(125,175)
        self.start_time = 0

    def update(self, game_speed, power_ups):
        self.rect.x -= game_speed
        if self.rect.x <- self.rect.width:
            power_ups.pop()


    def draw(self, screen):
        screen.blit(self.image, self.rect)