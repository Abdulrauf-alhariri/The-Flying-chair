import pygame as pg
from pygame.locals import *
# from PIL import


pg.init()

screen = pg.display.set_mode((1200, 800))
player_sprite = pg.image.load(
    "C:\\The-flying-chair-adventures-main\\game_images\\player_sprite.png").convert_alpha()

player_2 = player_sprite.copy().convert_alpha()
player_2.fill((0, 0, 200, 100), special_flags=pg.BLEND_ADD)

player_sprite.fill((155, 90, 0, 0), special_flags=pg.BLEND_ADD)


def draw_player():
    screen.blit(player_sprite, (300, 300))
    screen.blit(player_2, (500, 300))


repeat = 1
brighten = 1


while True:
    screen.fill((0, 0, 0))
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()

    draw_player()
    pg.display.update()
