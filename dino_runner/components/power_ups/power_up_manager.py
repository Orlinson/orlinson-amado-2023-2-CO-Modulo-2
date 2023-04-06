import pygame
import random
from dino_runner.utils.constants import SHIELD_TYPE, HAMMER_TYPE, DEFAULT_TYPE
from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.duration = random.randint(3, 5)
        self.when_appears = random.randint(50, 70)
    
    #creation of power_up random HW
    which_power_up_create = [Shield(), Hammer()]

    def update(self, game):
        types_power_up = [SHIELD_TYPE, HAMMER_TYPE]
        which_type_power_up_create = random.choice(types_power_up)
        if len(self.power_ups) == 0 and self.when_appears == game.score.count:
            self.generate_power_up(which_type_power_up_create)
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                game.player.has_power_up = True
                #verificar cual tipo de power_up es
                if which_type_power_up_create == SHIELD_TYPE:
                    game.player.type = SHIELD_TYPE
                    game.player.power_up_time = power_up.start_time + (self.duration * 1000)
                    self.power_ups.remove(power_up)
                else:
                    game.player.type = HAMMER_TYPE
                    game.player.power_up_time = power_up.start_time + (self.duration * 1000)
                    self.power_ups.remove(power_up)
                return game.player.type    
                    #game.player.type = SHIELD_TYPE
            #game.player.type = SHIELD_TYPE -> class

                

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = random.randint(50, 70)
    
    def generate_power_up(self, which_type_power_up_create):
        self.when_appears += random.randint(200, 300)
        #power_up = Shield() -> class
        #power_up = random.choice(which_power_up_create)
        if which_type_power_up_create == SHIELD_TYPE:
            power_up = Shield()
            self.power_ups.append(power_up)
        else:
            power_up = Hammer()
        self.power_ups.append(power_up)    
        #print(self.power_ups.append(power_up))
        #return power_up
        
        