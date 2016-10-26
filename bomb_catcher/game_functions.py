import pygame, sys
from pygame.locals import *

def print_text(screen, font, x, y, text, color=(0, 0, 0)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x, y))

def check_events():
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()