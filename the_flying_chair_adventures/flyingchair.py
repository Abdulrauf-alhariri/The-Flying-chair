import pygame as pg
import sys
from pygame.locals import *
import random
import time
from datetime import datetime, timedelta


# Importing the settings that are responsible for the game
from game_settings.mine_manager import MineManager, BlobManager
from game_settings.status import Points, Health, Shield


pg.init()

# Skärmen
height = 800
width = 1200
screen = pg.display.set_mode((width, height))
# KONSTANTER
FRICTION = 0.0005

# Screen flash
blinka_red = False
blinka_blue = False
repeat_red = 1
repeat_blue = 1

# Här kontrolerar man antal minor som ska ritas
between = 90
change_num = 1

# We're gonna use this variable to observe the time in the game
Clock = pg.time.Clock()

# The power up variable
power_ups = False
repeat = 1

# The game frames
frames = 1000

# The player brightness
transparency = 128

# Håller koll på minor!
mine_sprite = pg.image.load(
    'C:\\The-flying-chair-adventures-main\\game_images\\mine_sprite.png').convert_alpha()
mine_manager = MineManager(screen, mine_sprite)

# Blob sprite
blob_sprite = pg.image.load(
    "C:\\The-flying-chair-adventures-main\\game_images\\blob_sprite.png")
blob_manager = BlobManager(screen, blob_sprite)


# Håll koll på poäng!
poäng = Points(screen)


# Håll koll på hälsan!
player_hp = Health(screen, 750, 25)
player_shield = Shield(screen, 750, 50)
state = True


# Player/Spelaren
player_sprite = pg.image.load(
    "C:\\The-flying-chair-adventures-main\\game_images\\player_sprite.png").convert_alpha()
player_sprite_v2 = player_sprite.copy().convert_alpha()

# Here we are changing the brightness of the image
player_sprite_v2.fill((155, 90, 0, 0), special_flags=pg.BLEND_ADD)


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
    if power_ups == False:
        screen.blit(player_sprite, (player_position_x, player_position_y))

    else:
        screen.blit(player_sprite_v2, (player_position_x, player_position_y))


# Rita "startmenyn"
def draw_title_screen():
    textobjekt = font.render('The flying chair adventures', 1, (255, 255, 0))
    screen.blit(textobjekt, (50, 300))


# Undersöker om spelaren krockar med ett annat objekt.
# Returnerar True om krock, annars False.
def player_check_hit(other_hitbox):
    if power_ups:
        hitbox = player_sprite_v2.get_rect()

    else:
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
    global left_pressed, right_pressed, up_pressed, down_pressed, x_down
    time.sleep(3)
    player_velocity_x = 0
    player_velocity_y = 0
    player_position_x = 300
    player_position_y = 300
    left_pressed = False
    right_pressed = False
    up_pressed = False
    down_pressed = False
    x_down = False
    gamestate = "ready!"


# Game sounds
damage_sound3 = pg.mixer.Sound(
    "C:\\The-flying-chair-adventures-main\\Game_sounds\\hit_mine3.wav")
points_sound3 = pg.mixer.Sound(
    "C:\\The-flying-chair-adventures-main\\Game_sounds\\hit_point3.wav")


# Spel-loopen
# Har något hänt? "events"
# Uppdatera game state
# Rita ut på skärmen
while True:

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
        if random.randint(1, between) == 1:
            mine_manager.create_mine()

        if random.randint(1, 130) == 1:
            blob_manager.create_blob()

        # For-loop - den där get() ger all tså en LISTA med händelser. Kolla vilken TYP
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
        if player_position_x >= 1203:
            player_position_x = -2

        if player_position_x <= -4:
            player_position_x = 1201

        if player_position_y <= -5:
            player_position_y = 802

        if player_position_y >= 804:
            player_position_y = -1

        mine_manager.update()

        # Här så kollar man om poöng är delbar med 100
        if poäng.points > 1 and poäng.points % 100 == 0:
            power_ups = True

        # Om det är sant så blir det ett speciallt läge i tio sekunder
        # Då förlorar man inga hp även om man krockar minor
        if power_ups:
            if repeat == 1:
                power_up = datetime.now() + timedelta(seconds=10)
                repeat -= 1

            # Här kollar man om det har gått tio sekunder
            if datetime.now() < power_up:
                state = False

            else:
                power_ups = False
                state = True
                repeat = 1

        # Här om antal poöng är delbar med 10 så ökar man antal minor som ska dycka up på skärmen
        # Change_num använder jag för att kolla att if statment fungerar bara en gång om poöng är delbar med 10
        if poäng.points > 1 and poäng.points % 10 == 0:
            if between > 4 and change_num == 1:
                between -= 2
                change_num -= 1

        else:
            change_num = 1

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
                player_hp.update_bar(state)

                # Här kollar man om power ups mode fungerar eller inte
                if state:
                    damage_sound3.play()
                    blinka_red = True
                    pg.time.delay(100)

        # Här gör vi samma sak som med minor
        for blob in blob_manager.blobs:
            if player_check_hit(blob.hitbox_blob()):
                blob_manager.remove_blob(blob)
                poäng.update_points()
                player_shield.update_bar()
                points_sound3.play()
                blinka_blue = True

        # om shield baren är full, så fyller man hp fullt och shield baren blir tom
        if player_shield.check_bar():
            player_shield.reset_bar()
            player_hp.reset_hp()

        # player hp
        hp = player_hp.health_length

        # Rita på skärmen
        # R   G  B
        if not x_down:
            screen.fill((R, G, B))

        draw_player()
        mine_manager.draw()
        blob_manager.draw_blob()
        poäng.draw_points()

        player_hp.draw_health()
        player_shield.draw_bar()
        # Clock.tick(1000)
        print(hp)

        pg.display.update()

        # Här återställer man spelet.
        if hp <= 0:
            reset_game()
            player_hp.reset_hp()
            player_shield.reset_bar()
            poäng.reset_points()
            mine_manager.reset_minor()
            blob_manager.reset_blob()

        # Här blinkar skärmen rött om man förlorar hp
        if blinka_red:
            if repeat_red == 1:
                time_left = datetime.now() + timedelta(milliseconds=60)
                repeat_red -= 1

            if datetime.now() < time_left:
                screen.fill((179, 9, 9))
                pg.display.update()
            else:
                blinka_red = False
                repeat_red = 1

        # Här blinkar skärmen med blå om man träffar blob, får poäng
        if blinka_blue:
            if repeat_blue == 1:
                time_left = datetime.now() + timedelta(milliseconds=60)
                repeat_blue -= 1

            # Om det inte har gått 60 milliseconder så fortsätter skärmen att blinka blått
            if datetime.now() < time_left:
                screen.fill((0, 138, 237))
                pg.display.update()
            else:
                blinka_blue = False
                repeat_blue = 1
