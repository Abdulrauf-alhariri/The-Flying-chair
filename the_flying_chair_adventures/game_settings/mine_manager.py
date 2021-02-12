import pygame
from pygame.locals import *
import random
from datetime import datetime, timedelta

from .mine import Mine, Blob

# En klass för att hantera minor


class MineManager:

    # Sätter "startvärden"
    def __init__(self, screen, sprite):
        self.screen = screen
        self.sprite = sprite

        # Skapar en lista där alla minor ska ligga
        self.mines = []

    # Skapar en ny mina och lägger till den i listan

    def create_mine(self):
        # Värden för den nya minan
        position_x = random.randint(0, 1200)
        position_y = random.randint(-100, 1000)
        velocity_x = random.uniform(-1, 1)
        velocity_y = random.uniform(-1, 1)

        # DEN HÄR RADEN SKAPAR MINAN!
        new_mine = Mine(self.screen, self.sprite, position_x,
                        position_y, velocity_x, velocity_y)

        # Lägger till den nya minan i listan
        self.mines.append(new_mine)

    # Tar bort en mina
    def remove_mine(self, mine):
        self.mines.remove(mine)

    # Uppdaterar alla minor i listan
    def update(self):
        for mine in self.mines:
            mine.update()

            if mine.is_alive == False:
                self.remove_mine(mine)

    # Ritar ut alla minor i listan
    def draw(self):
        for mine in self.mines:
            mine.draw()

    def reset_minor(self):
        self.mines.clear()

# This is the class that can give you points
# and here so are we defining the points


class BlobManager:

    def __init__(self, screen, sprite):
        self.screen = screen
        self.sprite = sprite

        self.blobs = []

    def create_blob(self):
        self.position_x = random.randint(10, 1150)
        self.position_y = random.randint(20, 750)

        new_blob = Blob(self.screen, self.sprite,
                        self.position_x, self.position_y)

        # If there is ten points on the screen so we won't draw more points
        # Until one of them disappers
        if len(self.blobs) <= 10:
            self.blobs.append(new_blob)

    def remove_blob(self, point):
        self.blobs.remove(point)

    def draw_blob(self):
        for blob in self.blobs:
            blob.draw_blob()

    def reset_blob(self):
        self.blobs.clear()
