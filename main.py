import pygame
import numpy as np

#Initialize pygame
pygame.init()

#Create the screen
screen = pygame.display.set_mode((1200,600))

#Title and Icon
pygame.display.set_caption("Bike Race")
icon = pygame.image.load('bike.png')
pygame.display.set_icon(icon)

#Player

class map(object):
    def __init__(self, path = None):
        self.lines = []
        self.shapes = ['line','arc']
    def add_shape(self, shape, params):
        if shape in self.shapes:
            self.lines.append()

    def draw(self, window):
        pixel_array = pygame.PixelArray(window)
        #print(pixel_array.shape)
        #print(self.lines.max)
        #pixel_array[self.lines[0],self.lines[1]] = (0,0,0)
        pixel_array[:,500] = (0,0,0)
        pixel_array.close()

class player(object):
    def __init__(self, x, y):
        self.x = x
        self.vx = 0.0
        self.max_vx = 1.0

        self.rot = 0.0
        self.vrot = 0.0
        self.max_vrot = 1.0

        self.y = y
        self.vy = 0.0
        self.img = pygame.image.load('bike.png')

    def draw(self,window):
        window.blit(self.img, (self.x,self.y))

    def 
        

#Game Loop
biker = player(0,286)
map1 = map()
running = True
keys = pygame.key.get_pressed()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
            biker.vx = min(biker.max_vx, biker.vx + 0.01)
    elif keys[pygame.K_DOWN]:
            biker.vx = max(0, biker.vx-0.1)
    elif keys[pygame.K_RIGHT]:
            biker.vrot = min(biker.max_vrot, biker.vrot + 0.1)
    elif keys[pygame.K_RIGHT] and biker.vrot > -biker.max_vrot:
            biker.vrot = max(-biker.vrot, biker.vrot-0.1)
    #Nothing is pressed, only friction applies
    else:
        biker.vx -= 0.001
        print(biker.vx)
        biker.vrot /= 1.01
    screen.fill((255,255,255))

    biker.y += biker.vy
    biker.x += biker.vx
    biker.draw(screen)
    map1.draw(screen)
    pygame.display.update()
        