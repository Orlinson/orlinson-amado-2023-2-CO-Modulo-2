import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import DUCKING, RUNNING, JUMPING, DUCKING_SHIELD, RUNNING_SHIELD, DUCKING_HAMMER, JUMPING_SHIELD,DEFAULT_TYPE, SHIELD_TYPE

RUN_IMAGE = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD}
DUCK_IMAGE = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD}
JUMP_IMAGE = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD}


class Dinosour(Sprite):
  X_POS = 80
  Y_POS = 310
  Y_POS_DUCK = 340
  JUMP_SPEED = 8.5

  def __init__(self):
    #self.image = RUNNING[0]
    self.type = DEFAULT_TYPE
    self.image = RUN_IMAGE[self.type][0]
    self.dino_rect = self.image.get_rect()
    self.dino_rect.x = self.X_POS
    self.dino_rect.y = self.Y_POS
    self.dino_run = True
    self.step_index = 0
    self.dino_jump = False
    self.jump_speed = self.JUMP_SPEED
    self.dino_duck = False
    self.has_power_up = False
    self.power_up_time = 0

  def update(self, user_input):
    if self.dino_run:
      self.run()
    elif self.dino_jump:
      self.jump()
    elif self.dino_duck:
      self.duck()

    if user_input[pygame.K_UP] and not self.dino_jump:
      self.dino_jump = True
      self.dino_run = False
    elif user_input[pygame.K_DOWN] and not self.dino_jump:
      self.dino_jump = False
      self.dino_run = False
      self.dino_duck = True
    elif not self.dino_jump:
      self.dino_jump = False
      self.dino_run = True
      self.dino_duck = False

    if self.step_index > 9:
      self.step_index = 0

  def draw(self, screen):
    screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

  def run(self):
    self.image = RUN_IMAGE[self.type][self.step_index // 5]
    self.dino_rect = self.image.get_rect()
    self.dino_rect.x = self.X_POS
    self.dino_rect.y = self.Y_POS
    self.step_index += 1

  def jump(self):
    #self.image = JUMPING
    self.image = JUMP_IMAGE[self.type]
    self.dino_rect.y -= self.jump_speed*4
    self.jump_speed -= 0.8
    if self.jump_speed < -self.JUMP_SPEED:
      self.dino_rect.y = self.Y_POS
      self.dino_jump = False
      self.jump_speed = self.JUMP_SPEED

  def duck(self):
    #self.image = DUCKING[0] if self.step_index < 5 else DUCKING[1]
    self.image = DUCK_IMAGE[self.type][self.step_index // 5]
    self.dino_rect = self.image.get_rect()
    self.dino_rect.y = self.Y_POS_DUCK
    self.dino_rect.x = self.X_POS
    self.step_index += 1

  def reset(self):
    self.dino_rect.x = self.X_POS
    self.dino_rect.y = self.Y_POS
    self.step_index = 0
    self.dino_run = True
    self.dino_jump = False
    self.dino_duck = False

    self.jump_speed = self.JUMP_SPEED