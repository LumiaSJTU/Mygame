import pygame, sys, random
from pygame.locals import *
import game_functions as gf
pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Bomb Catcher")
font = pygame.font.Font(None, 24)
font1 = pygame.font.Font(None, 100)
white = 255, 255, 255
black = 0, 0, 0
y = 0
game_start = False
x = random.randint(10, 590)
survive = True
fail = False
lives = 3
score = 0
speed = 5
while True:
    gf.check_events()

    screen.fill(white)
    if survive:
        gf.print_text(screen, font, 0, 0, "Lives: " + str(lives))
        gf.print_text(screen, font, 500, 0, "Scores: " + str(score))
    if fail:
        gf.print_text(screen, font, 0, 0, "Lives: " + str(lives))
        gf.print_text(screen, font, 500, 0, "Scores: " + str(score))
    
    keys = pygame.key.get_pressed()
    if keys[K_RETURN]:
        game_start = True
    if game_start:
        if y <= 470:
            pygame.draw.circle(screen, black, (x, y), 10)
            y += speed
            print(y)
    pos_x, pos_y = pygame.mouse.get_pos()
    if pos_x >=550:
        pos = 550, 480, 50, 20
        pygame.draw.rect(screen, black, pos, 0)
    else:
        pos = pos_x, 480, 50, 20
        pygame.draw.rect(screen, black, pos, 0)
    if y == 470 + speed:
        if pos_x <= x and x <= pos_x + 70:
            x = random.randint(10, 590)
            y = 0
            survive = True
            fail = False
            score += 1
            if (score % 10 == 0):
                speed += 5
        else:
            x = random.randint(10, 590)
            y = 0
            survive = False
            fail = True
            lives -= 1
    if lives == 0:
        screen.fill(white)
        gf.print_text(screen, font1, 100, 100, "GAME OVER")
        game_start = False
        gf.print_text(screen, font, 180, 480, "Press Enter for another game!")
        if keys[K_RETURN]:
            lives = 3
            score = 0
            survive = True
            fail = False
            x = random.randint(10, 590)
            y = 0
    pygame.display.update()