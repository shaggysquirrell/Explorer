# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 20:21:45 2022

@author: rogel
"""
import math
#####################
import json
def write_data(data, file_obj):
    with open(file_obj, 'w') as f:
        json.dump(data, f, indent=4)

        
def load_grid_dictionary(ai_set, screen, file_obj):
    try:
        with open(file_obj, 'r') as read_file:
            data = json.load(read_file)
            file_obj = open(file_obj)
            ai_set.grid = decrypt_map_data(ai_set.grid, data['ai_set.grid'], 100, 100)
            ai_set.house_grid = decrypt_map_data(ai_set.house_grid, data['ai_set.house_grid'], 20, 20)
            print('okay')
    except:
        data = {
        'ai_set.grid':encrypt_map_data(ai_set.grid, 100, 100),
        'ai_set.house_grid':encrypt_map_data(ai_set.house_grid, 20, 20)
        }
        write_data(data, 'dictionary_data.json')

def save_grid_dictionary(ai_set, screen, file_obj):
    data = {
        'ai_set.grid':encrypt_map_data(ai_set.grid, 100, 100),
        'ai_set.house_grid':encrypt_map_data(ai_set.house_grid, 20, 20)
    }
    write_data(data, file_obj)




def load_data(ai_set, screen, player, map_1, map_2, file_obj):
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
        }
        write_data(data, file_obj)
        
        
        
def encrypt_map_data(map_data, rows, columns):
    save_index = 0
    dictionary = {}
    rows = math.sqrt(len(map_data))
    columns = math.sqrt(len(map_data))
    for row in range(int(rows)):
        for col in range(int(columns)):
            dictionary[save_index] = map_data[row,col]
            save_index+=1
    return dictionary

def decrypt_map_data(map_data, dictionary, rows, columns):
    reload_index = 0
    rows = math.sqrt(len(map_data))
    columns = math.sqrt(len(map_data))
    for row in range(int(rows)):
        for col in range(int(columns)):
            map_data[row, col] = dictionary[str(reload_index)]
            reload_index+=1
    return map_data
