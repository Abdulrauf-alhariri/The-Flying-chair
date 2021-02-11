import pygame as pg
import sys
from pygame.locals import *
import random
import time


# Importing the settings that are responsible for the game
from game_settings.mine_manager import MineManager
from game_settings.status import Points, Health


pg.init()

# Skärmen
height = 800
width = 1200
screen = pg.display.set_mode((width, height))
# KONSTANTER
FRICTION = 0.0005

# We're gonna use this variable to observe the time in the game
Clock = pg.time.Clock()

# The game frames
frames = 1000

# Håller koll på minor!
mine_sprite = pg.image.load(
    'C:\\The-flying-chair-adventures-main\\game_images\\mine_sprite.png').convert_alpha()
mine_manager = MineManager(screen, mine_sprite)

# Blob sprite
blob_sprite = pg.image.load(
    "C:\\The-flying-chair-adventures-main\\game_images\\blob_sprite.png")

# Håll koll på poäng!
poäng = Points(screen)

# Håll koll på hälsan!
player_hp = Health(screen, 750, 25)


# Player/Spelaren
player_sprite = pg.image.load(
    "C:\\The-flying-chair-adventures-main\\game_images\\player_sprite.png").convert_alpha()
player_position_x = 300
player_position_y = 300
player_velocity_x = 0
player_velocity_y = 0
# Avgör vilket spelläge som gäller för tillfället. Spelet ska börja med att visa menyn
gamestate = 'ready!'

# Text
font = pg.font.SysFont("Comic Sans MS", 70)

# draw the player


def draw_player():
    screen.blit(player_sprite, (player_position_x, player_position_y))


# Rita "startmenyn"
def draw_title_screen():
    textobjekt = font.render('The flying chair adventures', 1, (255, 255, 0))
    screen.blit(textobjekt, (50, 300))


# Undersöker om spelaren krockar med ett annat objekt.
# Returnerar True om krock, annars False.
def player_check_hit(other_hitbox):
    hitbox = player_sprite.get_rect()
    hitbox.x = player_position_x
    hitbox.y = player_position_y

    if hitbox.colliderect(other_hitbox):
        return True
    else:
        return False


# Styrning
left_pressed = False
right_pressed = False
up_pressed = False
down_pressed = False
space_down = False
x_down = False

# Reset the game


def reset_game():
    global gamestate, player_velocity_x, player_velocity_y, player_position_x, player_position_y
    global left_pressed, right_pressed, up_pressed, down_pressed
    time.sleep(3)
    player_velocity_x = 0
    player_velocity_y = 0
    player_position_x = 300
    player_position_y = 300
    left_pressed = False
    right_pressed = False
    up_pressed = False
    down_pressed = False
    gamestate = "ready!"


# Game sounds
damage_sound3 = pg.mixer.Sound(
    "C:\\The-flying-chair-adventures-main\\Game_sounds\\hit_mine3.wav")


# Spel-loopen
# Har något hänt? "events"
# Uppdatera game state
# Rita ut på skärmen
while True:

    # if hp == 0:
    #     reset_game()
    #     player_hp.reset_bar()
    #     poäng.reset_points()

    if gamestate == 'ready!':
        for event in pg.event.get():

            # Om en knapp på tangentbordet trycks ned, ändra spelläget till running
            if event.type == KEYDOWN:
                gamestate = 'running'

        # Visa menyn
        screen.fill((0, 0, 0))
        draw_title_screen()
        pg.display.update()

    elif gamestate == "running":

        # Create mine
        if random.randint(1, 50) == 1:
            mine_manager.create_mine()

        # For-loop - den där get() ger alltså en LISTA med händelser. Kolla vilken TYP
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()

            # Om en knapp på tangentbordet trycks ned
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    left_pressed = True

                if event.key == K_RIGHT:
                    right_pressed = True

                if event.key == K_UP:
                    up_pressed = True

                if event.key == K_DOWN:
                    down_pressed = True

                if event.key == K_SPACE:
                    space_down = True

                if event.key == K_x:
                    x_down = True

            # Om en knapp på tangentbordet har släppts
            if event.type == KEYUP:
                if event.key == K_LEFT:
                    left_pressed = False

                if event.key == K_RIGHT:
                    right_pressed = False

                if event.key == K_UP:
                    up_pressed = False

                if event.key == K_DOWN:
                    down_pressed = False

                if event.key == K_SPACE:
                    space_down = False

                if event.key == K_x:
                    x_down = False

        # Vilka knappar är nedtryckta just nu?
        if left_pressed:
            player_velocity_x -= 0.05
            player_velocity_y = 0

        if right_pressed:
            player_velocity_x += 0.05
            player_velocity_y = 0
        if up_pressed:
            player_velocity_y -= 0.05
            player_velocity_x = 0
        if down_pressed:
            player_velocity_y += 0.05
            player_velocity_x = 0

        # Minska hastigheten lite pga FRICTION
        player_velocity_x *= 1 - FRICTION
        player_velocity_y *= 1 - FRICTION

        # Ändra spelarens position - alltså FLYTTA SPELAREN
        player_position_x += player_velocity_x
        player_position_y += player_velocity_y

        # Bromsa om man trycker på space
        if space_down:
            player_velocity_x *= 0.01
            player_velocity_y *= 0.01

        # If the player pass the borders
        if player_position_x >= 1210:
            player_position_x = -3

        if player_position_x <= -4:
            player_position_x = 1205

        if player_position_y <= -10:
            player_position_y = 805

        if player_position_y >= 810:
            player_position_y = -1

        mine_manager.update()

        # RGB
        R = 0
        G = 0
        B = 0
        # Går igenom alla minor och undersöker om de krockar med spelaren
        for mine in mine_manager.mines:
            if player_check_hit(mine.hitbox()):

                # When the player hits a mine so it disappers and a sound plays
                # Also lose some hp and the game stops for 10 milliseconds
                mine_manager.remove_mine(mine)

                player_hp.update_bar()
                damage_sound3.play()
                pg.time.delay(100)

                R = 179
                G = 9
                B = 9
                screen.fill((179, 9, 9))
                screen.fill((0, 0, 0))

        # player hp
        hp = player_hp.health_length

        # Rita på skärmen
        # R   G  B
        if not x_down:
            screen.fill((R, G, B))

        draw_player()
        mine_manager.draw()
        poäng.draw_points()
        player_hp.draw_health()
        Clock.tick(1000)
        print(hp)

        pg.display.update()

        if hp <= 0:
            reset_game()
            player_hp.reset_bar()
            poäng.reset_points()
            mine_manager.reset_minor()
