# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 20:21:45 2022

@author: rogel
"""

#####################
import json
def write_data(data, file_obj):
    with open(file_obj, 'w') as f:
        json.dump(data, f, indent=4)

def load_data(ai_set, player, map_1, map_2, file_obj):
    try:
        with open(file_obj, 'r') as read_file:
            data = json.load(read_file)
            file_obj = open(file_obj)
            ai_set.world = data['world_bool']
            ai_set.house = data['house_bool']
            player.rect.x = data['player.rect.x']
            player.rect.y = data['player.rect.y']
            player.grid_x = data['player.grid_x']
            player.grid_y = data['player.grid_y']
            player.house_grid_x = data['player.house_grid_x']
            player.house_grid_y = data['player.house_grid_y']
            map_1.rect.x = data['map_1.rect.x']
            map_1.rect.y = data['map_1.rect.y']
            map_2.rect.x = data['map_2.rect.x']
            map_2.rect.y = data['map_2.rect.y']
            ai_set.grid = data['ai_set.grid']
            ai_set.house_grid = data['ai_set.house_grid']

    except:
        data = {
        'world_bool':ai_set.world,
        'house_bool':ai_set.house,
        'player.rect.x':player.rect.x,
        'player.rect.y':player.rect.y,
        'player.grid_x':player.grid_x,
        'player.grid_y':player.grid_y,
        'player.house_grid_x':player.house_grid_x,
        'player.house_grid_y':player.house_grid_y,
        'map_1.rect.x':map_1.rect.x,
        'map_1.rect.y':map_1.rect.y,
        'map_2.rect.x':map_2.rect.x,
        'map_2.rect.y':map_2.rect.y,
        'ai_set.grid':ai_set.grid,
        'ai_set.house_grid':ai_set.house_grid
        }
        write_data(data, 'explorer_data.json')
        
def save_data(ai_set, player, map_1, map_2, file_obj):
        data = {
        'world_bool':ai_set.world,
        'house_bool':ai_set.house,
        'player.rect.x':player.rect.x,
        'player.rect.y':player.rect.y,
        'player.grid_x':player.grid_x,
        'player.grid_y':player.grid_y,
        'player.house_grid_x':player.house_grid_x,
        'player.house_grid_y':player.house_grid_y,
        'map_1.rect.x':map_1.rect.x,
        'map_1.rect.y':map_1.rect.y,
        'map_2.rect.x':map_2.rect.x,
        'map_2.rect.y':map_2.rect.y,
        'ai_set.grid':ai_set.grid,
        'ai_set.house_grid':ai_set.house_grid
        }
        write_data(data, file_obj)
        