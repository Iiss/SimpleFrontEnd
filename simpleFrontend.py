import pygame
from pygame.locals import *

SCREEN_W = 640
SCREEN_H = 480
FPS = 30

pygame.init()
        
screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))
pygame.display.set_caption("Simple Frontend")
#pygame.mouse.set_visible(False)

running = True

BACKDROP_IMG = pygame.image.load("assets/img/hg2.png").convert()

CABINET_IMG = pygame.image.load("assets/img/cab.png").convert()
CABINET_IMG.set_colorkey(CABINET_IMG.get_at((0,0)))

LOGO_LINE_IMG = pygame.image.load("assets/img/invaders.png").convert()
LOGO_LINE_IMG.set_colorkey(LOGO_LINE_IMG.get_at((0,0)))

screen.blit(BACKDROP_IMG,[0,0])
screen.blit(LOGO_LINE_IMG,[0,0])
screen.blit(CABINET_IMG,[107,201])

pygame.display.update();

while running:

    for event in pygame.event.get():
        if event.type == QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
            
pygame.quit()
sys.exit()
