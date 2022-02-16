 # -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 21:58:56 2021

@author: rogel
"""


import pygame
import csv
import sys
import os

from chest import Chest

def parse_csv(ai_set, csv_filename):
    number_value = []
    with open(os.path.join(ai_set.csv_filename)) as data:
        data = csv.reader(data, delimiter= ',')
        for i in data:
            number_value.append(list(i))
          
    return number_value

        ###########  Get Map Tiles  ###############
def get_tiles(screen, ai_set, filename, rows, columns):
    sheet = pygame.image.load(filename)
    rect = sheet.get_rect()
    screen_rect = screen.get_rect()
    
    img_width = rect.w/columns
    img_height = rect.h/rows
                   ###################
    ai_set.tile_values = parse_csv(ai_set, ai_set.csv_filename)
                  ####################
    
    tiles = []
    chest_index = -1
    
    for row in range(rows):
        for col in range(columns):
            rect = pygame.Rect(img_width*col, img_height*row, img_width, img_height)
            tiles.append(sheet.subsurface(rect))
            x = screen_rect.centerx + 16 * col
            y = screen_rect.centery + 16 * row
            
            if int(ai_set.tile_values[row][col]) in ai_set.occupied_tiles:
                occupation = 'Occupied'
            else:
                occupation = 'Not Occupied'
                
            if int(ai_set.tile_values[row][col]) in ai_set.chest_tiles:
                
                cst = Chest(screen, ai_set, row, col)
                ai_set.chests.append(cst)
                
                chest = 'Chest'
                chest_index +=1
                
            else:
                chest = 'NONE'
            
            ai_set.grid[col, row] = {'occupation': occupation, 'grid_location':(col, row), 'screen_location':(x,y), 'chest': chest, 'chest_index': chest_index}

    ai_set.map_tiles = tiles
   ##########################################################


       ############  Get Player Frames  ################
def get_frames(screen, ai_set, filename, rows, columns):
    sheet = pygame.image.load(filename)
    rect = sheet.get_rect()
    img_width = rect.w/columns
    img_height = rect.h/rows
    
    
    frames = []

    
    for row in range(rows):
        for col in range(columns):
            rect = pygame.Rect(img_width*col, img_height*row, img_width, img_height)
            frames.append(sheet.subsurface(rect))

    return frames
##########################################################

def init(screen, ai_set):
    ai_set.object_frames = get_frames(screen, ai_set, ai_set.object_sheet, 20, 33)
    ai_set.map_tiles = get_tiles(screen, ai_set, ai_set.map_sheet, 100, 100)
    ai_set.player_frames = get_frames(screen, ai_set, ai_set.player_sheet[0], 3, 4) + get_frames(screen, ai_set, ai_set.player_sheet[1], 3, 4)

def check_chests(ai_set, player, key):
    if key[pygame.K_LEFT] and ai_set.grid[player.grid_x -1, player.grid_y]['chest'] == 'Chest':
        chest = ai_set.chests[ai_set.grid[player.grid_x -1, player.grid_y]['chest_index']]
        chest.open = True
        
        
        
def check_external_events(ai_set, player, map_1):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def check_events(ai_set, player, map_1):
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
     key = pygame.key.get_pressed()
                 ### Open Chests ###
     check_chests(ai_set, player, key)
     
                ###  Moving Left  ###
     if key[pygame.K_LEFT] and ai_set.grid[player.grid_x -1, player.grid_y]['occupation'] != 'Occupied':             
         if ai_set.key_hold_time == 7:    
            player.grid_x -=1
            ai_set.run_animation_left = True
        
         else:
             ai_set.key_hold_time += 1
             player.image = ai_set.player_frames[17]
             

               ###  Moving Right  ###
     elif key[pygame.K_RIGHT] and ai_set.grid[player.grid_x +1, player.grid_y]['occupation'] != 'Occupied':
         if ai_set.key_hold_time == 7:
             player.grid_x +=1
             ai_set.run_animation_right = True
             
         else:
             ai_set.key_hold_time += 1
             player.image = ai_set.player_frames[4]


             ###  Moving Down  ###
     elif key[pygame.K_DOWN] and ai_set.grid[player.grid_x, player.grid_y +1]['occupation'] != 'Occupied':
         if ai_set.key_hold_time == 7:
             player.grid_y +=1
             ai_set.run_animation_down = True
             
         else:
             ai_set.key_hold_time += 1
             player.image = ai_set.player_frames[0]


             ###  Moving Up  ###
     elif key[pygame.K_UP] and ai_set.grid[player.grid_x, player.grid_y -1]['occupation'] != 'Occupied':
         if ai_set.key_hold_time == 7:
             player.grid_y -=1
             ai_set.run_animation_up = True
         
         else:
             ai_set.key_hold_time += 1
             player.image = ai_set.player_frames[8]
         
     elif key[pygame.K_LEFT] and ai_set.grid[player.grid_x -1, player.grid_y]['occupation'] == 'Occupied':
         pygame.mixer.music.play(0, 0, 1)
         player.image = ai_set.player_frames[17]
     elif key[pygame.K_RIGHT] and ai_set.grid[player.grid_x +1, player.grid_y]['occupation'] == 'Occupied':
         pygame.mixer.music.play(0, 0, 1)
         player.image = ai_set.player_frames[4]
     elif key[pygame.K_DOWN] and ai_set.grid[player.grid_x, player.grid_y +1]['occupation'] == 'Occupied':
         pygame.mixer.music.play(0, 0, 1)
         player.image = ai_set.player_frames[0]
     elif key[pygame.K_UP] and ai_set.grid[player.grid_x, player.grid_y -1]['occupation'] == 'Occupied':
         pygame.mixer.music.play(0, 0, 1)
         player.image = ai_set.player_frames[8]
         
         
     elif not key[pygame.K_LEFT]:
         ai_set.key_hold_time = 0
     elif not key[pygame.K_RIGHT]:
         ai_set.key_hold_time = 0
     elif not key[pygame.K_DOWN]:
         ai_set.key_hold_time = 0
     elif not key[pygame.K_UP]:
         ai_set.key_hold_time = 0
    ##############################################################

def animate(ai_set, player, map_1):           
     if ai_set.run_animation_left and ai_set.animation_time%1 == 0:
        map_1.rect.x += 1
        for row in range(100):
            for col in range(100):
                x,y = ai_set.grid[col,row]['screen_location']
                ai_set.grid[col,row]['screen_location'] = x+1, y
        
        if ai_set.animation_time == 16:
            ai_set.index_left = ai_set.index_left + 1
            
            if ai_set.index_left > 19:
                ai_set.index_left = 16
                
            player.image = ai_set.player_frames[ai_set.index_left]
        
      
     elif ai_set.run_animation_right and ai_set.animation_time%1 ==0:
        map_1.rect.x -= 1
        for row in range(100):
            for col in range(100):
                x,y = ai_set.grid[col,row]['screen_location']
                ai_set.grid[col,row]['screen_location'] = x-1, y

        if ai_set.animation_time == 16:
            ai_set.index_right = ai_set.index_right + 1
            
            if ai_set.index_right > 7:
                ai_set.index_right = 4
                
            player.image = ai_set.player_frames[ai_set.index_right]
            
            
     elif ai_set.run_animation_down and ai_set.animation_time%1 ==0:
        map_1.rect.y -= 1
        for row in range(100):
            for col in range(100):
                x,y = ai_set.grid[col,row]['screen_location']
                ai_set.grid[col,row]['screen_location'] = x, y-1

        if ai_set.animation_time == 16:
            ai_set.index_down = ai_set.index_down + 1
            
            if ai_set.index_down > 3:
                ai_set.index_down = 0
                
            player.image = ai_set.player_frames[ai_set.index_down]
        
        
        
     elif ai_set.run_animation_up and ai_set.animation_time%1 ==0:
        map_1.rect.y += 1
        for row in range(100):
            for col in range(100):
                x,y = ai_set.grid[col,row]['screen_location']
                ai_set.grid[col,row]['screen_location'] = x, y+1

        if ai_set.animation_time == 16:
            ai_set.index_up = ai_set.index_up + 1
            
            if ai_set.index_up > 11:
                ai_set.index_up = 8
                
            player.image = ai_set.player_frames[ai_set.index_up]

def init_movement(ai_set, player, map_1):
    ####  Runs Through The Animation And Movement Process  ####
            #### Automated With No Input ####
            
        ################ Animate Left ##################
    if ai_set.run_animation_left:
        animate(ai_set, player, map_1)
        
        ai_set.animation_time -= 1
            
        if ai_set.animation_time <= 0:
            ai_set.animation_time = 16
            ai_set.run_animation_left = False
                
            if ai_set.player_start_left == 19:
                ai_set.player_start_left = 17
                player.image = ai_set.player_frames[ai_set.player_start_left]
                    
            elif ai_set.player_start_left == 17:
                ai_set.player_start_left = 19
                player.image = ai_set.player_frames[ai_set.player_start_left]
                    
                    
    elif ai_set.run_animation_left == False:
        ai_set.index_left = ai_set.player_start_left
            
        ################# Animate Right ##################    
    if ai_set.run_animation_right:
        animate(ai_set, player, map_1)
        
        ai_set.animation_time -= 1
            
        if ai_set.animation_time <= 0:
            ai_set.animation_time = 16
            ai_set.run_animation_right = False
                
            if ai_set.player_start_right == 4:
                ai_set.player_start_right = 6
                player.image = ai_set.player_frames[ai_set.player_start_right]
                    
            elif ai_set.player_start_right == 6:
                ai_set.player_start_right = 4
                player.image = ai_set.player_frames[ai_set.player_start_right]
                    
                    
    elif ai_set.run_animation_right == False:
        ai_set.index_right = ai_set.player_start_right
                
        ################# Animate Down ################
    if ai_set.run_animation_down:
        animate(ai_set, player, map_1)
        
        ai_set.animation_time -= 1
            
        if ai_set.animation_time <= 0:
            ai_set.animation_time = 16
            ai_set.run_animation_down = False
                
            if ai_set.player_start_down == 0:
                ai_set.player_start_down = 2
                player.image = ai_set.player_frames[ai_set.player_start_down]
                    
            elif ai_set.player_start_down == 2:
                ai_set.player_start_down = 0
                player.image = ai_set.player_frames[ai_set.player_start_down]
                    
                    
    elif ai_set.run_animation_up == False:
        ai_set.index_down = ai_set.player_start_down
                        
        ################# Animate Up ################
    if ai_set.run_animation_up:
        animate(ai_set, player, map_1)
        
        ai_set.animation_time -= 1
            
        if ai_set.animation_time <= 0:
            ai_set.animation_time = 16
            ai_set.run_animation_up = False
                
            if ai_set.player_start_up == 8:
                ai_set.player_start_up = 10
                player.image = ai_set.player_frames[ai_set.player_start_up]
                    
            elif ai_set.player_start_up == 10:
                ai_set.player_start_up = 8
                player.image = ai_set.player_frames[ai_set.player_start_up]
                    
                    
    elif ai_set.run_animation_up == False:
        ai_set.index_up = ai_set.player_start_up          
                

        ########################################################### 
      
     
            
