import pygame, sys, time, random
from pygame.locals import *
def print_text(font, x, y, text, color = (0, 0, 0)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x, y))

pygame.init()
screen = pygame.display.set_mode((600, 500))
font1 = pygame.font.Font(None, 24)
font2 = pygame.font.Font(None, 200)
game_over = True
key_flag = False
clock_start = 0
correct_answer = 97
seconds = 10
score = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            key_flag = True
        elif event.type == pygame.KEYUP:
            key_flag = False
    
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()
    if keys[K_RETURN]:
        if game_over:
            game_over = False
            score = 0
            seconds = 11
            clock_start = time.clock()
    
    current = time.clock() - clock_start
    speed = score * 6
    if seconds - current < 0:
        game_over = True
    elif current <= 10:
        if keys[correct_answer]:
            correct_answer = random.randint(97, 122)
            score += 1

    screen.fill((255, 255, 255))

    print_text(font1, 0, 0, "Let's see how fast you can type!")
    print_text(font1, 0, 20, "Try to keep up for 10 seconds...")

    if key_flag:
        print_text(font1, 500, 0, "<key>")

    if not game_over:
        print_text(font1, 0, 80, "Time: " + str(int(seconds-current)))

    print_text(font1, 0, 100, "Speed: " + str(speed) + " letters/min")

    if game_over:
        print_text(font1, 0, 160, "Press Enter to start...")

    print_text(font2, 0, 240, chr(correct_answer-32))

    
    #update the display
    pygame.display.update()
    '''
    screen.fill((255, 255, 255))
    print_text(font1, 0, 0, "Hello")
    keys = pygame.key.get_pressed()
    clock_start = time.clock()
    last_time = int(11 - clock_start)
    if (last_time >= 0):
        count_time = True
    else:
        count_time = False
    if count_time:
        print_text(font1, 200, 200, str(last_time))
    if (clock_start <= 5):
        show_text = True
    else:
        show_text = False
    if show_text:
        if keys[pygame.K_1]:
            count += 1
    if not show_text:
        print_text(font1, 100, 100, str(count))
    pygame.display.update()
    '''