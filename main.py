import pygame
import sys
from random import randint

FIGHTER_STEP = 0.5
ROCKET_STEP = 0.4
ALIEN_STEP = 0.1

screen_width = 800
screen_height = 600
screen_fill_colour = (32, 52, 71)
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.init()
pygame.display.set_caption('Shooter')

fighter_image = pygame.image.load('images/fighter.png')
fighter_width, fighter_height = fighter_image.get_size()
fighter_x = int(screen_width / 2 - fighter_width / 2)
fighter_y = int(screen_height - fighter_height)
fighter_is_moving_left = False
fighter_is_moving_right = False

rocket_image = pygame.image.load('images/rocket.png')
rocket_width, rocket_height = rocket_image.get_size()
rocket_x = int(fighter_x + fighter_width / 2 - rocket_width / 2)
rocket_y = int(fighter_y - rocket_height)
rocked_was_fired = False

alien_image = pygame.image.load('images/alien.png')
alien_width, alien_height = alien_image.get_size()
alien_x = randint(0, screen_width - alien_width)
alien_y = 0
alien_speed = ALIEN_STEP

rect_height = fighter_height + 1
rect_width = screen_width
rect_colour = (42, 62, 81)

game_font = pygame.font.SysFont('JetBrains Mono', 30)
game_is_running = True
game_score = 0

while game_is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                fighter_is_moving_left = True
            if event.key == pygame.K_RIGHT:
                fighter_is_moving_right = True
            if event.key == pygame.K_SPACE:
                rocket_x = int(fighter_x + fighter_width / 2 - rocket_width / 2)
                rocket_y = int(fighter_y - rocket_height)
                rocked_was_fired = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                fighter_is_moving_left = False
            if event.key == pygame.K_RIGHT:
                fighter_is_moving_right = False

    if fighter_is_moving_left and fighter_x >= FIGHTER_STEP:
        fighter_x -= FIGHTER_STEP
    if fighter_is_moving_right and fighter_x <= screen_width - FIGHTER_STEP - fighter_width:
        fighter_x += FIGHTER_STEP

    alien_y += alien_speed

    if alien_y + alien_height >= fighter_y:
        game_is_running = False

    if rocked_was_fired:
        rocket_y -= ROCKET_STEP
    if rocked_was_fired and rocket_y + rocket_height <= 0:
        rocked_was_fired = False

    screen.fill(screen_fill_colour)
    pygame.draw.rect(screen, (22, 42, 61), (0, screen_height - fighter_height - 1, rect_width, 1))
    pygame.draw.rect(screen, rect_colour, (0, screen_height - fighter_height, rect_width, rect_height))
    screen.blit(fighter_image, (fighter_x, fighter_y))
    screen.blit(alien_image, (alien_x, alien_y))
    if rocked_was_fired:
        screen.blit(rocket_image, (rocket_x, rocket_y))
    if rocked_was_fired and \
            alien_x - 2 * rocket_height / 3 < rocket_x < alien_x + alien_width - 2 * rocket_width / 3 and \
            alien_y < rocket_y < alien_y + alien_height - rocket_height:
        rocked_was_fired = False
        alien_x = randint(0, screen_width - alien_width)
        alien_y = 0
        alien_speed += ALIEN_STEP/10
        game_score += 1

    game_score_text = game_font.render(f"Your score is: {game_score}", True, rect_colour)
    screen.blit(game_score_text, (20, 20))
    pygame.display.update()

game_over_text = game_font.render('GAME OVER', True, (255, 255, 255))
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (screen_width / 2, screen_height / 2)
screen.blit(game_over_text, game_over_rect)
pygame.display.update()
pygame.time.wait(3000)
pygame.quit()
