# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 21:44:44 2021

@author: rogel
"""

class Settings():
    def __init__(self):
        self.screen_size = (480, 320) #(960, 640)
        self.frame_rate = 60
        self.set_width = 30
        self.set_height= 20
        
        self.key_hold_time = 0
        
        self.grid = {}
        self.house_grid = {}
        self.map_tiles = ()
        
        self.index_left = 16
        self.index_right = 4
        self.index_down = 0
        self.index_up = 8
        
        self.animation_time = 16
        
        self.run_animation = False
        
        self.run_animation_left = False
        self.run_animation_right = False
        self.run_animation_down = False
        self.run_animation_up = False
        
        self.player_frames = []
        self.object_frames = []
        self.hud_frames = []
        
        self.player_sheet = ('character_right.png', 'character_left.png')
        self.map_sheet = ('map.png', 'house_layer1.png')
        self.house_sheet = ('house_layer1.png', 'house_layer2.png')
        self.object_sheet = ('o.png')
        
        self.csv_filename = ('map_new_layer2.csv', 'map_new_layer3.csv', 'house_layer_2.csv', 'house_layer_3.csv')
        
        self.layer1_tile_values = []
        self.layer2_tile_values = []
        self.layer1_house_tile_values = []
        self.layer2_house_tile_values = []
        self.object_tile_values = []
        
        self.player_start_left = 19
        self.player_start_right = 4
        self.player_start_down = 0
        self.player_start_up = 8
        
        self.x = False
        
        self.chests = []
        
        self.occupied_tiles = [603,602,2,733,731, 682, 684, 761, 760, 683, 722, 723,151,724,191, 152, 192, 203, 204, 205, 605, 604]
        self.house_occupied_tiles = [1,2,3]
        self.door_tiles = [48,88]
        
        self.chest_tiles = [2]
        
        self.hud_tiles = [462,463,495,496,528,529,530,531,532,561,562]
        self.chest_frames = [0,33,34,66,67,35,36,68,69]#[45, 46, 78, 79]
        
        self.world = True
        self.house = False
