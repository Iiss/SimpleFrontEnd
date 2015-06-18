import pygame,sys
from pygame.locals import *
import os

SCREEN_W = 640
SCREEN_H = 480
FPS = 30

pygame.init()
        
screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))
pygame.display.set_caption("Simple Frontend")
#pygame.mouse.set_visible(False)

running = True

#
# Constants
#
ROM_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)),'roms')
SNAPS_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)),'snaps')

#
# Init skin graphics
#
BACKDROP_IMG = pygame.image.load("assets/img/hg2.png").convert()

CABINET_IMG = pygame.image.load("assets/img/cab.png").convert()
CABINET_IMG.set_colorkey(CABINET_IMG.get_at((0,0)))

LOGO_LINE_IMG = pygame.image.load("assets/img/invaders.png").convert()
LOGO_LINE_IMG.set_colorkey(LOGO_LINE_IMG.get_at((0,0)))

screen.blit(BACKDROP_IMG,[0,0])
screen.blit(LOGO_LINE_IMG,[0,0])
screen.blit(CABINET_IMG,[107,201])

#
# Init fonts
#
LABEL_COLOR = (255,131,0)
FOCUS_COLOR = (255,255,255)
FONT = pygame.font.Font("assets/fonts/fff_spacedust.ttf",8)


### temp
label = FONT.render('Test Label Incorporated',False,LABEL_COLOR); 
screen.blit(label,[0,0])
pygame.display.update();
### end of temp

while running:

    for event in pygame.event.get():
        if event.type == QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
            
pygame.quit()
sys.exit()
