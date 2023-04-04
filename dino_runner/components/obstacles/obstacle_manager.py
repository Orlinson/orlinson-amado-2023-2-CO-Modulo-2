import pygame
import random
from dino_runner.components import obstacles
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD



class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            show_obstacle = [SMALL_CACTUS, LARGE_CACTUS, BIRD]
            obstacles_any = Cactus(show_obstacle[random.randint(0,2)])

            #which_cactus = [SMALL_CACTUS, LARGE_CACTUS]
            #cactus = Cactus(which_cactus[random.randint(0,1)])
            #bird = Bird
            #obstacles = [cactus, Bird]
            #how_obstacles = obstacles[random.randint(0,1)]
            #which_obstacle = [obstacles_any, Bird]
            self.obstacles.append(obstacles_any)


        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)   
            if game.player.dino_rect.colliderect(obstacle.rect):
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

