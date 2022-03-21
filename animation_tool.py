# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 18:20:06 2022

@author: rogel
"""

import pygame
import sys

vec = pygame.math.Vector2

class Settings():
    def __init__(self):
        self.screen_size = (0,0)
        self.frame_rate = 5
        self.back_ground_color = (225, 220, 180)
        
        self.animation_time = 10
        self.reset_time = 10
        
        self.player_sheet = 'test2.png'
        self.rows = 1
        self.columns = 1
        
        self.player_frames = []
        self.player_frame_index = 0
        
        self.text_boxes = []
        self.text_box_x = 40
        self.text_box_y = 100
        self.text_box_width = 200
        self.text_box_height = 50
        self.text_box_active_color = (124,124,124)
        self.text_box_color = (255,255,255)
        self.text_size = 24
        self.text_color = (50, 20, 243)
        
        
class Player():
    def __init__(self, screen, ai_set):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        
        self.ai_set = ai_set
        
        self.image = ai_set.player_frames[0]
        self.rect = self.image.get_rect()
        
        self.rect.x = self.screen_rect.centerx
        self.rect.y = self.screen_rect.centery
    
    def frame_update(self, ai_set):
        ai_set.animation_time -= 1
        self.rect.x = self.screen_rect.centerx - self.rect.width//2
        self.rect.y = self.screen_rect.centery - self.rect.height//2
        
        if ai_set.animation_time % 10:
            
            if ai_set.player_frame_index == len(ai_set.player_frames) - 1:
                ai_set.player_frame_index = 0
                ai_set.animation_time = ai_set.reset_time
            
            else:
                ai_set.player_frame_index += 1
            self.image = ai_set.player_frames[ai_set.player_frame_index]
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)
        
#class Text_box():
#    def __init__(self, x, y, width, height, bg_color, active_color, text_size, text_color):
#        self.x = x
#        self.y = y
#        self.width = width
#        self.height = height
#        self.pos = vec(x,y)
#        self.size = vec(x, y)
#        self.image = pygame.Surface((width, height))
#        self.image_rect = self.image.get_rect()
  
#        self.active_color = active_color
#        self.bg_color = bg_color
#        self.active = False
#        self.txt_size = text_size
#        self.txt = ''
#        self.font = pygame.font.SysFont('arial', self.txt_size)
#        self.txt_color = text_color
        
#    def update(self):
#        pass
        
#    def draw(self, screen):
#        if not self.active:
#            self.image.fill(self.bg_color)
            
#        else:
#            self.image.fill(self.active_color)
#            # Rendering text to image #
#            text = self.font.render(self.txt,False, self.txt_color)
#            # Getting the size attributes of the text #
#            rect = text.get_rect()
#            rect.x = self.image_rect.centerx
#            rect.y = self.image_rect.centery
#            text_width = text.get_width()
#            self.image.blit(text, (rect.x, rect.y))
            
            
#        screen.blit(self.image, self.pos)
        
#    def check_click(self, pos):
#        if pos[0]>self.x and pos[0] < self.x+self.width:
#            if pos[1] > self.y and pos[1] < self.y+self.height:
#                self.active = True
#            else:
#                self.active = False
#        else:
#            self.active = False
            
#    def add_text(self, key):
#        text = list(self.txt)
#        text.append(chr(key))
#        self.txt = ''.join(text)
        
#        print(self.txt)
        
        
def strip_sheet(ai_set, rows, columns, filename):
    sheet = pygame.image.load(filename)
    rect = sheet.get_rect()
    img_width = rect.w/int(columns)
    img_height = rect.h/int(rows)
    
    
    frames = []
    for row in range(int(rows)):
        for col in range(int(columns)):
            rect = pygame.Rect(img_width*col, img_height*row, img_width, img_height)
            frames.append(sheet.subsurface(rect))

    return frames
        
        
        
def check_events(ai_set):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            for box in ai_set.text_boxes:
                box.check_click(pygame.mouse.get_pos())
                
        if event.type == pygame.KEYDOWN:
            for box in ai_set.text_boxes:
                if box.active:
                    box.add_text(event.key)


def main_game():
    pygame.init()
    clock = pygame.time.Clock()
    
    ai_set = Settings()
    check_admin_input(ai_set)
    
    screen = pygame.display.set_mode(ai_set.screen_size)
    pygame.display.set_caption('Sprite_Animation')
    
    ai_set.player_frames = strip_sheet(ai_set, ai_set.rows, ai_set.columns, ai_set.player_sheet)
    print(ai_set.player_frames)
    player = Player(screen, ai_set)
    
#    ai_set.text_boxes.append(Text_box(ai_set.text_box_x, ai_set.text_box_y, ai_set.text_box_width, ai_set.text_box_height, ai_set.text_box_active_color, ai_set.text_box_color, ai_set.text_size, ai_set.text_color))
    
    run = True
    while run:
        clock.tick(ai_set.frame_rate)
        check_events(ai_set)
                
        screen.fill(ai_set.back_ground_color)
        
#        for box in ai_set.text_boxes:
#            box.draw(screen)
#        
        player.frame_update(ai_set)
        player.blitme()
        
        pygame.display.update()
        

def check_admin_input(ai_set):
    ai_set.player_sheet = input('What is the file name of your sheet?: ')
    ai_set.rows = input('How many rows in your character sheet?:')
    ai_set.columns = input('How many columns in your character sheet?: ')
    image = pygame.image.load(ai_set.player_sheet)
    rect = image.get_rect()
    x = rect.width//int(ai_set.columns)
    y = rect.height//int(ai_set.rows)
    ai_set.screen_size = (x,y)


    

main_game()   
