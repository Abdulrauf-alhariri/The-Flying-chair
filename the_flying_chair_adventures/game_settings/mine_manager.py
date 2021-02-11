import pygame
from pygame.locals import *
import random

from .mine import Mine

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
        position_x = random.randint(200, 1200)
        position_y = random.randint(-100, 1200)
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

    # Ritar ut alla minor i listan
    def draw(self):
        for mine in self.mines:
            mine.draw()

    def reset_minor(self):
        self.mines.clear()
