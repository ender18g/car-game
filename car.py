import pygame
from math import sin, cos, pi


class Car(pygame.sprite.Sprite):
    def __init__(self,screen):
        super().__init__()
        self.image = pygame.image.load('assets/PNG/Cars/car_blue_small_3.png')
        self.image = pygame.transform.rotate(self.image, -90)
        self.rect = self.image.get_rect()
        self.theta = 0 # theta is in degrees
        self.velocity = 2 # in pixels per second
        self.x, self.y = [0,0]
        self.rect.center = (self.x, self.y)
        self.og_image = self.image
        self.steer_step = 2
        self.vel_step = 0.1
        self.screen = screen

    def update(self):
        # update your controls based on the keyboard
        self.update_controls()
        self.check_collision()

        # update the image and rectangle based on new theta
        self.image = pygame.transform.rotate(self.og_image, self.theta)
        self.rect = self.image.get_rect()

        deg_rad = pi / 180

        # calculate the new x and y position after being moved
        self.x += self.velocity * cos(self.theta * deg_rad)
        self.y -= self.velocity * sin(self.theta * deg_rad)

        # place the rect at the updated position
        self.rect.center = (self.x, self.y)

    def update_controls(self):
        # get the list of keyboard booleans
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.theta -= self.steer_step
        if keys[pygame.K_LEFT]:
            self.theta += self.steer_step
        if keys[pygame.K_UP]:
            self.velocity += self.vel_step
        if keys[pygame.K_DOWN]:
            self.velocity -= self.vel_step
    def check_collision(self):
        # check if car hits the border. Stop the car
        buffer = 50

        if self.x > self.screen.get_width() - 50:
            self.velocity = -0.2



    def draw(self):
        self.screen.blit(self.image, self.rect)













