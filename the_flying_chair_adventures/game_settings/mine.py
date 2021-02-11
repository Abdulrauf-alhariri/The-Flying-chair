import pygame
from pygame.locals import *
import random

# En klass för minor


class Mine:

    # Sätter "startvärden"
    def __init__(self, screen, sprite, position_x, position_y, velocity_x, velocity_y):
        self.screen = screen
        self.sprite = sprite
        self.position_x = position_x
        self.position_y = position_y
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y

    # Flyttar minan
    def update(self):
        self.position_x += self.velocity_x
        self.position_y += self.velocity_y

    # Ritar ut minan
    def draw(self):
        self.screen.blit(self.sprite, (self.position_x, self.position_y))

    # Hitbox för minan
    def hitbox(self):
        hitbox = self.sprite.get_rect()
        hitbox.x = self.position_x
        hitbox.y = self.position_y
        return hitbox
