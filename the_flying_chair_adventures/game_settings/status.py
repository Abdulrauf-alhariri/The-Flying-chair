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
        self.health_length = 400
        self.percent = 100

    def draw_health(self):
        height = 20
        width = 400
        green = 25, 128, 82
        red = 186, 29, 11

        # Here we are creating the navigating bar that gonna be shown when you are dead
        pygame.draw.rect(
            self.screen, red, (self.position_x, self.position_y, width, height))

        # This bar is you health baar
        pygame.draw.rect(
            self.screen, green, (self.position_x, self.position_y, self.health_length, height))

        font = pygame.font.Font(None, 30)
        text = font.render(f" {self.percent} %", 1, (255, 255, 255))

        # Here so I'm defining the position of the points
        percent_place = text.get_rect(topright=(970, self.position_y))
        self.screen.blit(text, percent_place)

    def update_bar(self, state):
        if self.health_length >= 0 and state == True:
            self.health_length -= 8
            self.percent -= 2

    # This method is used to recover the players health
    def reset_hp(self):
        self.health_length = 400
        self.percent = 100


# A class to check of we should recover the health or not


class Shield:
    def __init__(self, screen, position_x, position_y):
        self.screen = screen
        self.position_x = position_x
        self.position_y = position_y
        self.shield_length = 0
        self.percent = 0

    def draw_bar(self):
        height = 20
        width = 400
        grey = 81, 82, 102
        blue = 0, 14, 217

        # Here we are creating the navigating bar that gonna be shown when you are dead
        pygame.draw.rect(
            self.screen, grey, (self.position_x, self.position_y, width, height))

        # This bar is you health baar
        pygame.draw.rect(
            self.screen, blue, (self.position_x, self.position_y, self.shield_length, height))

        font = pygame.font.Font(None, 30)
        text = font.render(f" {self.percent} %", 1, (255, 255, 255))

        # Here so I'm defining the position of the points
        percent_place = text.get_rect(topright=(970, self.position_y))
        self.screen.blit(text, percent_place)
    # This function is to check whether the bar is full or not

    def check_bar(self):
        if self.shield_length == 400:
            return True

        else:
            return False

    # This function is to increase the length of the bar
    def update_bar(self):
        self.percent += 2

        if self.shield_length < 400:
            self.shield_length += 8

    def reset_bar(self):
        self.shield_length = 0
        self.percent = 0
