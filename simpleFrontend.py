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
need_update=True
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


#
# Init fonts
#
LABEL_COLOR = (255,131,0)
FOCUS_COLOR = (255,255,255)
FONT = pygame.font.Font("assets/fonts/fff_spacedust.ttf",8)


def update_rom_list_data(dirPath):

    result = []
    for file in os.listdir(dirPath):
        
        file_path = os.path.join(dirPath,file)
        
        if(os.path.isfile(file_path)):
            parts = os.path.splitext(os.path.basename(file_path))
            file_name = parts[0]
            result.append(file_name)

    return result

#
# Rom list control
#
class ListBox(pygame.Surface):
    
    def __init__(self,(width,height)):
        pygame.Surface.__init__(self,(width,height))
        self.set_colorkey((0,0,0))

        self.sell_h=25
        self.page_size = int(self.get_height()/self.sell_h)+1;
        
    def select_index(self,ind):
        
        self.selected_index=ind;
        focus_delta=int(self.page_size/2)
        start_index=0
        
        if ind>focus_delta:
            if (len(self.data_source)-1-ind) < focus_delta :
                start_index=(len(self.data_source)-self.page_size)
            else:
                start_index = ind-focus_delta
            
        
        end_index = start_index+self.page_size if len(self.data_source)>self.page_size else len(self.data_source)
       
        y=0
        self.fill((0,0,0))
        
        for i in range(start_index,end_index):
            color = FOCUS_COLOR if i==ind else LABEL_COLOR
            
            label = FONT.render(str(self.data_source[i]),False,color)
            self.blit(label,[0,y])
            y+=self.sell_h
            
    def set_data(self,list_data):
        self.data_source=list_data
        self.select_index(0)

    def next_item(self):
        
        if self.data_source == None or len(self.data_source)==0:
            return

        new_index=self.selected_index+1

        if new_index>len(self.data_source)-1:
            new_index=0

        self.select_index(new_index)
    
    def prev_item(self):
        if self.data_source == None or len(self.data_source)==0:
            return
        
        new_index=self.selected_index-1

        if new_index<0:
            new_index=len(self.data_source)-1
            
        self.select_index(new_index)

    def page_up(self):
        if self.data_source == None or len(self.data_source)==0:
            return

        new_index=self.selected_index-self.page_size
        if new_index<0:
            new_index=len(self.data_source)-1
            
        self.select_index(new_index)
        
    def page_down(self):
        if self.data_source == None or len(self.data_source)==0:
            return
        
        new_index=self.selected_index+self.page_size
       
        if new_index>len(self.data_source)-1:
            new_index=0
            
        self.select_index(new_index)

    def get_selected(self):
        if self.data_source == None or len(self.data_source)==0:
            return None
        else:
            return self.data_source[self.selected_index]

#
# Image viewer
#
class ImageBox:
    def __init__(self,(width,height)):
        self.surface=pygame.Surface((width,height))
        
    def set_source(self,src):
        self.surface.fill((0,0,0))
        if(os.path.isfile(src)):
            img = pygame.image.load(src).convert()

            if(img.get_width()>img.get_height()):
                scale=float(self.surface.get_width())/img.get_width()
            else:
                scale=float(self.surface.get_height())/img.get_height() 
            
            img_w = int(img.get_width()*scale)
            img_h = int(img.get_height()*scale)
            
            img_surface=pygame.transform.scale(img,(img_w,img_h))
            self.surface.blit(img_surface,[.5*(self.surface.get_width()-img_w),.5*(self.surface.get_height()-img_h)])

rom_list_data = update_rom_list_data(ROM_PATH)

rom_list= ListBox((300,270))
rom_list.set_data(rom_list_data)

img_box=ImageBox((222,165))



while running:
    
    for event in pygame.event.get():

        ### temp
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_DOWN:
                rom_list.next_item()
                need_update=True
                
            if event.key == pygame.K_UP:
                rom_list.prev_item()
                need_update=True

            if event.key == pygame.K_LEFT:
                rom_list.page_up()
                need_update=True
                
            if event.key == pygame.K_RIGHT:
                rom_list.page_down()
                need_update=True
                
        ### end of temp
        
        if event.type == QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

        if need_update:
            need_update=False

            #update data
            img_box.set_source(os.path.join(SNAPS_PATH,rom_list.get_selected()+'.png'))
            
            #update graphics
            screen.blit(BACKDROP_IMG,[0,0])
            screen.blit(LOGO_LINE_IMG,[0,0])
            screen.blit(img_box.surface,[85,65])
            screen.blit(CABINET_IMG,[107,201])
            screen.blit(rom_list,[325,100])
            pygame.display.update();
            
pygame.quit()
sys.exit()
