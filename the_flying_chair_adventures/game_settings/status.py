import pygame
from pygame.locals import *
import random

pygame.init()


class Points:

    # Creating a global variable in the class
    points = 0

    def __init__(self, screen):
        self.screen = screen

    # This function is responsible for checking the points
    def draw_points(self):
        font = pygame.font.Font(None, 40)
        text = font.render(f"Points: {self.points}", 1, (255, 255, 255))

        # Here so I'm defining the position of the points
        points_place = text.get_rect(topleft=(3, 50/2))
        self.screen.blit(text, points_place)

    # This function is responsible for increasing the points
    def update_points(self):
        self.points += 1

    # This one is responsible for removing the poinits
    def remove_points(self):
        self.points -= 1

    def reset_points(self):
        self.points = 0


class Health:

    def __init__(self, screen, position_x, position_y):
        self.screen = screen
        self.position_x = position_x
        self.position_y = position_y
        self.health_length = 399

    def draw_health(self):
        height = 30
        width = 400
        green = 25, 128, 82
        red = 186, 29, 11

        # Here we are creating the navigating bar that gonna be shown when you are dead
        pygame.draw.rect(
            self.screen, red, (self.position_x, self.position_y, width, height))

        # This bar is you health baar
        pygame.draw.rect(
            self.screen, green, (self.position_x, self.position_y, self.health_length, height))

    def update_bar(self):
        if self.health_length >= 0:
            self.health_length -= 50

    def reset_bar(self):
        self.health_length = 400
