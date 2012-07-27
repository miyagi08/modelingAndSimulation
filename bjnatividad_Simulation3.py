import pygame
import sys
import math
import random

pygame.init()
pygame.mouse.set_visible(True)
font = pygame.font.Font("freesansbold.ttf", 32)


clock = pygame.time.Clock()
window = pygame.display.set_mode([800,600])
background_color = pygame.Color(240,25,255)

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity_x = 0
        self.velocity_y = 0
        self.size = 10
        self.color = pygame.Color(0,0,0)

    def update(self):
        
        self.x += self.velocity_x
        self.y += self.velocity_y

        self.velocity_x *= 0.99
        self.velocity_y *= 0.99

        self.x = int(self.x)
        self.y = int(self.y)

        if (self.x > 800):
            self.velocity_x *=-1
        if (self.x < 0):
            self.velocity_x = self.velocity_x * -1

        if (self.y < 0):
            self.velocity_y *=-1
        if (self.y > 600):
            self.velocity_y *=-1
        
    def draw(self, window):
        pygame.draw.circle(window, self.color, [self.x, self.y], self.size)

list_of_balls = [Ball(random.randint(50,300), random.randint(50,300)),
                 Ball(random.randint(115,300), random.randint(115,300)),
                Ball(random.randint(115,300), random.randint(115,300)),
                Ball(random.randint(115,300), random.randint(115,300)),]



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill(background_color)

    mouse_pos = pygame.mouse.get_pos()
    msg = "%i %i" %(mouse_pos[0],mouse_pos[1])
    text = font .render(msg, False, pygame.Color(0,0,0))
    window.blit(text,[0,0])

    if (pygame.mouse.get_pressed()[0] == True):
        for ball in list_of_balls:
            #move to origin
            origin_mouse_x = mouse_pos[0] - ball.x
            origin_mouse_y = mouse_pos[1] - ball.y
            #find distance to origin (pythagorean)
            distance = math.sqrt(origin_mouse_x * origin_mouse_x + origin_mouse_y * origin_mouse_y)

            #normalize
            normal_mouse_x = origin_mouse_x / distance
            normal_mouse_y = origin_mouse_y / distance

            #invert normal
            #normal_mouse_x *=-1
            #normal_mouse_y *=-1

            #move ball away from cursor, using the inverted normal
            ball.velocity_x += normal_mouse_x * 2.5
            ball.velocity_y += normal_mouse_y * 2.5

    for ball in list_of_balls:    
        ball.update()
        ball.draw(window)

    pygame.display.update()
    clock.tick(30)
