import pygame, sys
from pygame.locals import *

def print_text(font, x, y, text, color=(0, 0, 0)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x, y))

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Mouse Demo")
font = pygame.font.Font(None, 24)
pos_x = pos_y = 0
rel_x = rel_y = 0
mouse_down = mouse_up = 0
mouse_down_x = mouse_down_y = 0
mouse_up_x = mouse_up_y = 0
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == MOUSEMOTION:
            pos_x, pos_y = event.pos
            rel_x, rel_y = event.rel
        elif event.type == MOUSEBUTTONDOWN:
            mouse_down = event.button
            mouse_down_x, mouse_down_y = event.pos
        elif event.type == MOUSEBUTTONUP:
            mouse_up = event.button
            mouse_up_x, mouse_up_y = event.pos

    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()

    screen.fill((255, 255, 255))

    print_text(font, 0, 0, "Mouse Event")
    print_text(font, 0, 20, "Mouse Position:" + str(pos_x) + "," + str(pos_y))
    print_text(font, 0, 40, "Mouse relative:" + str(rel_x) + "," + str(rel_x))
    print_text(font, 0, 60, "Mouse button down:" + str(mouse_down) + " at " + str(mouse_down_x) + "," + str(mouse_down_y))
    print_text(font, 0, 80, "Mouse button up:" + str(mouse_up) + " at " + str(mouse_up_x) + "," + str(mouse_up_y))

    print_text(font, 0, 160, "Mouse Polling")
    x, y = pygame.mouse.get_pos()
    print_text(font, 0, 180, "Mouse position:" + str(x) + "," + str(y))
    b1, b2, b3 = pygame.mouse.get_pressed()
    print_text(font, 0, 200, "Mouse buttons:" + str(b1) + "," + str(b2) + "," + str(b3))
    pygame.display.update()
