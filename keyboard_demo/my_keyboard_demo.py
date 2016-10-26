import pygame, sys, time, random
from pygame.locals import *

def print_text(font, x, y, text, color=(0, 0, 0)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x, y))

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Keyboard Demo")
font1 = pygame.font.Font(None, 24)
font2 = pygame.font.Font(None, 200)
score = 0
correct_answer = 97
game_start = False
time_start = 0
current = 0
time_last = 0
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    
    keys = pygame.key.get_pressed()
    if keys[K_RETURN]:
        score = 0
        time_start = time.clock()
    
    
    if time_start != 0:
        current = time.clock() - time_start

    if current > 10:
        game_start = False
        time_last = 0
    else:
        game_start = True
        time_last = int(10 - current)
    if game_start:
        if keys[correct_answer]:
            correct_answer = random.randint(97, 122)
            score += 1

    screen.fill((255, 255, 255))
    print_text(font1, 0, 0, "Let's see how fast you can type!")
    print_text(font1, 0, 20, "Try to keep up for 10 seconds...")

    print_text(font1, 0, 80, "time:" + str(time_last))
    print_text(font1, 0, 100, "Speed:" + str(score) + " letters/min")

    print_text(font1, 0, 160, "Press Enter to start...")

    print_text(font2, 0, 220, chr(correct_answer-32))

    pygame.display.update()
