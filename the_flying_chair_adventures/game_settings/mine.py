import pygame
from pygame.locals import *
import random
from datetime import datetime, timedelta

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
        self.time_left = datetime.now() + timedelta(seconds=5)
        self.is_alive = True

    # Flyttar minan
    def update(self):
        self.position_x += self.velocity_x
        self.position_y += self.velocity_y

        if datetime.now() > self.time_left:
            self.is_alive = False

    # Ritar ut minan

    def draw(self):
        self.screen.blit(self.sprite, (self.position_x, self.position_y))

    # Hitbox för minan
    def hitbox(self):
        hitbox = self.sprite.get_rect()
        hitbox.x = self.position_x
        hitbox.y = self.position_y
        return hitbox


class Blob:
    def __init__(self, screen, sprite, position_x, position_y):
        self.screen = screen
        self.sprite = sprite
        self.position_x = position_x
        self.position_y = position_y

    # Drawing the blob sprite on the screen
    def draw_blob(self):
        self.screen.blit(self.sprite, (self.position_x, self.position_y))

    # Getting the size and the position of the blob sprite
    def hitbox_blob(self):
        hitbox_blob = self.sprite.get_rect()
        hitbox_blob.x = self.position_x
        hitbox_blob.y = self.position_y
        return hitbox_blob
