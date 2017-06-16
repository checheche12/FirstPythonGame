import pygame
from pygame.locals import *
import sys

pygame.init()
screen = pygame.display.set_mode((1024,768),DOUBLEBUF)
pygame.display.set_caption('Pracitce')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255,255,255))
    imageFile = pygame.image.load('Image/1.png')
    screen.blit(imageFile, (50,100))
    pygame.display.flip()
