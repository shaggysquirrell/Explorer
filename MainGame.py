   # -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 21:22:41 2021

@author: rogel
"""

import pygame

from Game_Settings import Settings
import Game_Functions as gf

class maps():
    def __init__(self, screen, ai_set, image):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        
        self.rect.x = self.screen_rect.centerx
        self.rect.y = self.screen_rect.centery
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)

class Player():
    def __init__(self, screen, ai_set):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        
        self.ai_set = ai_set
        
        self.image = ai_set.player_frames[0]
        self.rect = self.image.get_rect()
        
        self.rect.x = self.screen_rect.centerx
        self.rect.y = self.screen_rect.centery-8
        
        self.grid_x = 0
        self.grid_y = 0
        self.house_grid_x = 0
        self.house_grid_y = 0
        
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False
        
    def check_events(self):
        if self.moving_left:
            print('True')
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)


def main_game():
    pygame.init()
    ai_set = Settings()
    clock = pygame.time.Clock()
    
    screen = pygame.display.set_mode(ai_set.screen_size)
    screen_rect = screen.get_rect()
    pygame.display.set_caption('Explorer RPG3 ' + str(clock.get_fps()))
    
    gf.init(screen, ai_set)
    player = Player(screen, ai_set)
    map_1 = maps(screen, ai_set, ai_set.map_sheet[0])
    map_2 = maps(screen, ai_set, ai_set.map_sheet[1])
    
    ######## Music ##########
    pygame.mixer.music.load('Hit_01.mp3')
    
    run = True
    while run:
        clock.tick(ai_set.frame_rate)
        gf.check_external_events(ai_set, player, map_1)
        
        screen.fill((0,0,0))
        
        if ai_set.world:
            gf.init_movement(ai_set, player, map_1)
            map_1.blitme()
            player.blitme()
            for i in range(len(ai_set.chests)):
                ai_set.chests[i].update()
                ai_set.chests[i].animate()
                ai_set.chests[i].blitme()
        
        elif ai_set.house:
            gf.init_movement(ai_set, player, map_2)
            map_2.blitme()
            player.blitme()
    
        pygame.display.flip()
        
main_game()