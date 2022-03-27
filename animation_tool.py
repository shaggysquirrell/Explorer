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
        self.screen_size = (500,700)#(0,0)
        self.frame_rate = 60
        self.back_ground_color = (225, 220, 180)
        self.r = 0
        self.g = 0
        self.b = 0
        self.button_color = (186, 234, 240)
        
        self.animation_time = 0
        self.reset_time = 0
        
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
        
        self.enter = False
        self.backspace = False
        
        self.letter = ''
        self.start_animation = False
        
        self.resize = False
        
        
import pygame.font



class Button():
    def __init__(self, screen, ai_set, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        self.width, self.height = 200, 50
        self.button_color = ai_set.button_color
        self.text_color = (255, 255, 255)
        
        self.font = pygame.font.SysFont(None, 48)
        
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        self.prep_msg(msg)
        
        
    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        
        self.msg_image_rect.center = self.rect.center
        
    def blitme(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        
        
        
def check_button(screen, ai_set, mouse_x, mouse_y, start_button):
    if start_button.rect.collidepoint(mouse_x, mouse_y):
        ai_set.start_animation = True
        
        
        
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
        
class Text_box:
    def __init__(self, surface, x, y, width, height, state, color=(176, 176,176),
                 active_color=(255, 255, 255), border=True, border_color=(0,0,0), border_width=2,
                 place_text='', text_name='arial', text_size=25, text_color=(0,0,0)):
        self.screen = surface
        self.x = x
        self.y = y
        self.pos = vec(x,y)
        self.width = width
        self.height = height
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos
        self.state = state
        self.color = color
        self.active_color = active_color
        self.border = border
        self.border_color = border_color
        self.border_width = border_width
        self.place_text = place_text
        self.text = []
        self.font_name = text_name
        self.font_size = text_size
        self.text_color = text_color
        self.cursor_pos = 0
        self.active = False
        self.hovered = False
        
        self.input = ''
        
        self.direction_text = state
        
    def update(self, pos):
        if self.is_hovered(pos):
            self.hovered = True
        else:
            self.hovered = False
            
    def draw(self):
        if self.border:
            self.image.fill(self.border_color)
            if self.active:
                pygame.draw.rect(self.image, self.active_color, (self.border_width, self.border_width, 
                                self.width-(self.border_width*2), self.height-(self.border_width*2)))
                
            else:
                pygame.draw.rect(self.image, self.color, (self.border_width, 
                                self.border_width, self.width-(self.border_width*2), self.height-(self.border_width*2)))
                                 
        else:
            if self.active:
                self.image.fill(self.active_color)

            else:
                self.image.fill(self.color)
                
        if len(self.text) > 0:
            self.show_text()
        self.screen.blit(self.image, self.pos)
        
    def is_hovered(self, pos):
        if pos[0] > self.pos.x and pos[0] < self.pos.x + self.width:
            if pos[1] > self.pos.y and pos[1] < self.pos.y + self.height:
                self.click()
                return True
            else:
                self.active = False
                return False
        else:
            self.active = False
            return False
    
    def direction(self):
        text = self.direction_text
        font = pygame.font.SysFont(self.font_name, self.font_size)
        text = font.render(text, False, self.text_color)
        size = text.get_size()
        
        x, y = self.x- 120, self.y+10
        
        pos = vec(x, y)
        self.screen.blit(text, pos)
        
    
    def show_text(self):
        text = ''.join(self.text)
        font = pygame.font.SysFont(self.font_name, self.font_size)
        text = font.render(text, False, self.text_color)
        size = text.get_size()
        if size[0]+10 > self.width+10:
            x, y = self.width-(size[0]+10), (self.height//2)-(size[1]//2)
        else:
            x, y = 10, (self.height//2)-(size[1]//2)
        pos = vec(x, y)
        self.image.blit(text, pos)
        
    def click(self):
        self.active = True
        
    def user_input(self, event):
        if event.key != 13 and event.key != 273 and event.key != 274 and event.key != 275 and event.key != 276:
            self.text.insert(self.cursor_pos, event.unicode)
            self.cursor_pos += 1
        elif event.key == 8 and self.cursor_pos> 0 and len(self.text) > 0:
            del self.text[self.cursor_pos-1]
            self.cursor_pos-=1
        elif event.key == 276 and self.cursor_pos != 0:
            self.cursor_pos -=1
        elif event.key == 275 and self.cursor_pos < len(self.text):
            self.cursor_pos +=1
        elif event.key == 127 and self.cursor_pos < len(self.text):
            del self.text[self.cursor_pos]
            print('delete')
        
        
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
        
        
        
def check_events(ai_set, screen, start_button):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if ai_set.resize:
            ai_set.screen_size = (200, 200)
            screen = pygame.display.set_mode(ai_set.screen_size, pygame.RESIZABLE)
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            for box in ai_set.text_boxes:
                box.update(pygame.mouse.get_pos())
                
            
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_button(screen, ai_set, mouse_x, mouse_y, start_button)
                
        if event.type == pygame.KEYDOWN:
            for box in ai_set.text_boxes:
                if box.active:
                    box.user_input(event)
            
            if event.key == pygame.K_RETURN:
                for i in range(len(ai_set.text_boxes)):
                    box = ai_set.text_boxes[i]

                    if box.active:
                        if i == len(ai_set.text_boxes) - 1:
                            i = -1
                        ai_set.text_boxes[1+i].active = True
                        box.active = False
                        box.input = ''
                        for x in range(len(box.text)):
                            if box.text[x] != '':
                                box.input = box.input + box.text[x]
                        return
                return
                
            if event.key == pygame.K_BACKSPACE:
                for box in ai_set.text_boxes:
                    if box.active:
                        box.text = []
                        box.input = ''
                ai_set.backspace = True
                return
            
            
def check_animation_events(ai_set):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            ai_set.start_animation = False
            pygame.display.set_mode(ai_set.screen_size, pygame.RESIZABLE)
            
ai_set = Settings()

def main_game(ai_set):
    pygame.init()
    clock = pygame.time.Clock()
    
#    check_admin_input(ai_set)
    
    screen = pygame.display.set_mode(ai_set.screen_size, pygame.RESIZABLE)
    pygame.display.set_caption('Animation_Tool')
    
    ai_set.player_frames = strip_sheet(ai_set, ai_set.rows, ai_set.columns, ai_set.player_sheet)
    print(ai_set.player_frames)
    player = Player(screen, ai_set)
    
    ai_set.text_boxes.append(Text_box(screen, 200, 60, 200, 50, 'Image:'))
    ai_set.text_boxes.append(Text_box(screen, 200, 120, 200, 50, 'Rows:'))
    ai_set.text_boxes.append(Text_box(screen, 200, 180, 200, 50, 'Columns:'))
    ai_set.text_boxes.append(Text_box(screen, 200, 240, 200, 50, 'Frame Rate:'))
    ai_set.text_boxes.append(Text_box(screen, 200, 300, 200, 50, 'Red(RGB):'))
    ai_set.text_boxes.append(Text_box(screen, 200, 360, 200, 50, 'Green(RGB):'))
    ai_set.text_boxes.append(Text_box(screen, 200, 420, 200, 50, 'Blue(RGB):'))
    
    start_button = Button(screen, ai_set, 'Start')
    
    run = True
    while run:

        clock.tick(ai_set.frame_rate)
        pygame.draw.rect(screen, (255,0,0), pygame.Rect(screen.get_width() - 5 -(screen.get_width()/5), 50, screen.get_width()/5,50))
        check_events(ai_set, screen, start_button)
        
        try:
            if ai_set.start_animation:
            
                ai_set.player_sheet = ai_set.text_boxes[0].input
                ai_set.rows = ai_set.text_boxes[1].input
                ai_set.columns = ai_set.text_boxes[2].input
                ai_set.frame_rate = int(ai_set.text_boxes[3].input)
                ai_set.r = int(ai_set.text_boxes[4].input)
                ai_set.g = int(ai_set.text_boxes[5].input)
                ai_set.b = int(ai_set.text_boxes[6].input)
                
                rect = pygame.image.load(ai_set.player_sheet).get_rect()
                x = rect.width//int(ai_set.columns)
                y = rect.height//int(ai_set.rows)
                screen = pygame.display.set_mode((x, y))
            
                ai_set.player_frames = strip_sheet(ai_set, ai_set.rows, ai_set.columns, ai_set.player_sheet)
                print(ai_set.player_frames)
                player = Player(screen, ai_set)

            
                while ai_set.start_animation:
                    clock.tick(ai_set.frame_rate)
                    check_animation_events(ai_set)
                    
                    screen.fill((ai_set.r, ai_set.g, ai_set.b))
                    
                    player.frame_update(ai_set)
                    player.blitme()
        
                    pygame.display.update()
        except:
            print('Try again something went wrong')
            ai_set.start_animation = False
                
        screen.fill(ai_set.back_ground_color)
        
        for box in ai_set.text_boxes:
            box.draw()
            box.direction()
        
        start_button.blitme()
        pygame.display.update()
        
#ai_set.screen_size = (x,y)

main_game(ai_set)
