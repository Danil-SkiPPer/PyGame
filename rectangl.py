import pygame
import sys

clock = pygame.time.Clock()
pygame.init()

screen_width = 800
screen_height = 600
STEP = 10


screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('Pygame Shooter')

rect_width = 50
rect_height = 50

x = screen_width / 2 - rect_width / 2
y = screen_height / 2 - rect_height / 2

rect_colour = pygame.Color('lightyellow')

while True:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and y >=STEP:
                y -= STEP
            if event.key == pygame.K_DOWN and y <= screen_height - STEP - rect_height:
                y += STEP
            if event.key == pygame.K_LEFT and x >=STEP:
                x -= STEP
            if event.key == pygame.K_RIGHT and x <= screen_width - STEP - rect_width:
                x += STEP
    screen.fill((32, 52, 71))
    pygame.draw.rect(screen, rect_colour, (x, y, rect_width, rect_height))
    pygame.display.update()
    clock.tick(60)
