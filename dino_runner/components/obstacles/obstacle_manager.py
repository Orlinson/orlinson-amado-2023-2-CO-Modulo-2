import pygame
from dino_runner.components import obstacles

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS



class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            Cactus = Cactus(SMALL_CACTUS)
            self.obstacles.append(cactus)

        for obstacles in self.obstacles:
            obstacles.update(game.game_speed, self.obstacles)   
            if game.player.dino_rect.colliderect(obstacle.rect):
                game.playing = False
                break

    def draw(self):
        for obstacle in obstacles:
            obstacle.draw(screen)

