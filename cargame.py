import pygame
from helpers import build_background
from car import Car

# pygame setup
pygame.init()

# make a clock
clock = pygame.time.Clock()
# set the resolution of our game window
WIDTH = 1080
HEIGHT = 720
display = pygame.display.set_mode((WIDTH, HEIGHT))

# get my background
background = build_background(display)

# make a car instance
my_car = Car(display)

# steer authority
steer_step = 5

# GAME LOOP
running = True
while running:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw the background on the display
    display.blit(background, (0, 0))

    # update and draw car
    my_car.update()
    my_car.draw()

    clock.tick(60) # run at 60 FPS

    pygame.display.set_caption(f"CHOMP {clock.get_fps():.0}")

    # flip() the display to put your work on display
    pygame.display.flip()

pygame.quit()