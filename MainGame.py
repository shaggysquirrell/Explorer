   # -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 21:22:41 2021

@author: rogel
"""

import pygame

from Game_Settings import Settings
import Game_Functions as gf
import Data_Manager as dm

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
    soun_obj = pygame.mixer.Sound('Open_01.mp3')
    overworld_msc = pygame.mixer.Sound('Opening.ogg')
    overworld_msc.play(-1)
    ######### Data ##########
    dm.load_data(ai_set, player, map_1, map_2,'explorer_data.json')
    
    run = True
    while run:
        clock.tick(ai_set.frame_rate)
        gf.check_external_events(ai_set, player, map_1, map_2)
        gf.check_doors(ai_set, player, map_1, map_2, soun_obj)
        screen.fill((0,0,0))
        
        if ai_set.world:
            gf.check_events(ai_set, player, map_1, map_2, ai_set.grid, player.grid_x, player.grid_y)
            gf.init_movement(ai_set, player, map_1, ai_set.grid, 100, 100)
            map_1.blitme()
            player.blitme()
            for i in range(len(ai_set.chests)):
                ai_set.chests[i].update()
                ai_set.chests[i].animate()
                ai_set.chests[i].blitme()
        
        elif ai_set.house:
            gf.check_events(ai_set, player, map_1, map_2, ai_set.house_grid, player.house_grid_x, player.house_grid_y)
            gf.init_movement(ai_set, player, map_2, ai_set.house_grid, 20, 20)
            map_2.blitme()
            player.blitme()

        pygame.display.flip()
        
main_game()
