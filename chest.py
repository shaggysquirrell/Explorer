# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 21:12:48 2022

@author: rogel
"""

class Chest():
    def __init__(self, screen, ai_set, row, col):
        self.ai_set = ai_set
        self.screen = screen
        
        self.chest_1 = True
        self.chest_2 = False
        self.chest_3 = False
        
        self.row =  row
        self.col = col
        
        self.open = False
        self.animation_time = 15
        
        self.screen_rect = self.screen.get_rect()
        
        ###  Chest_1  ###
        self.chest1_image_one = self.ai_set.object_frames[ai_set.chest_frames[0]]
        self.chest1_rect_one = self.chest1_image_one.get_rect()
        
        self.chest1_rect_one.x = 50
        self.chest1_rect_one.y = 50
        
        ###  Chest_2  ###
        self.chest2_image_one = self.ai_set.object_frames[ai_set.chest_frames[1]]
        self.chest2_image_two = self.ai_set.object_frames[ai_set.chest_frames[2]]
        self.chest2_image_three = self.ai_set.object_frames[ai_set.chest_frames[3]]
        self.chest2_image_four = self.ai_set.object_frames[ai_set.chest_frames[4]]
        
        self.chest2_rect_one = self.chest2_image_one.get_rect()
        self.chest2_rect_two = self.chest2_image_two.get_rect()
        self.chest2_rect_three = self.chest2_image_three.get_rect()
        self.chest2_rect_four = self.chest2_image_four.get_rect()
        
        self.chest2_rect_one.x = 50
        self.chest2_rect_one.y = 50
        self.chest2_rect_two.x = 34
        self.chest2_rect_two.y = 50
        self.chest2_rect_three.x = 50
        self.chest2_rect_three.y = 34
        self.chest2_rect_four.x = 34
        self.chest2_rect_four.y = 34
        
        ###  Chest_3  ###
        self.chest3_image_one = self.ai_set.object_frames[ai_set.chest_frames[5]]
        self.chest3_image_two = self.ai_set.object_frames[ai_set.chest_frames[6]]
        self.chest3_image_three = self.ai_set.object_frames[ai_set.chest_frames[7]]
        self.chest3_image_four = self.ai_set.object_frames[ai_set.chest_frames[8]]

        self.chest3_rect_one = self.chest3_image_one.get_rect()
        self.chest3_rect_two = self.chest3_image_two.get_rect()
        self.chest3_rect_three = self.chest3_image_three.get_rect()
        self.chest3_rect_four = self.chest3_image_four.get_rect()
        
        self.chest3_rect_one.x = 50
        self.chest3_rect_one.y = 50
        self.chest3_rect_two.x = 50
        self.chest3_rect_two.y = 50
        self.chest3_rect_three.x = 50
        self.chest3_rect_three.y = 50
        self.chest3_rect_four.x = 50
        self.chest3_rect_four.y = 50
    
    def update(self):
        x,y = self.ai_set.grid[self.col, self.row]['screen_location']
        
        self.chest1_rect_one.x, self.chest1_rect_one.y = x,y
        
        self.chest2_rect_one.x, self.chest2_rect_one.y = x-8,y-8
        self.chest2_rect_two.x, self.chest2_rect_two.y = x+8,y-8
        self.chest2_rect_three.x, self.chest2_rect_three.y = x-8,y+8
        self.chest2_rect_four.x, self.chest2_rect_four.y = x+8,y+8
        
        self.chest3_rect_one.x, self.chest3_rect_one.y = x-8,y-8
        self.chest3_rect_two.x, self.chest3_rect_two.y = x+8,y-8
        self.chest3_rect_three.x, self.chest3_rect_three.y = x-8,y+8
        self.chest3_rect_four.x, self.chest3_rect_four.y = x+8,y+8
        
    def animate(self):
        if self.open:
            if self.chest_1:
                self.animation_time -= 1
                if self.animation_time == 0:
                    self.animation_time = 15
                    self.chest_1 = False
                    self.chest_2 = True
                    
            elif self.chest_2:
                self.animation_time -= 1
                if self.animation_time == 0:
                    self.animation_time = 15
                    self.chest_2 = False
                    self.chest_3 = True
                    
        elif not self.open:
            if self.chest_3:
                self.animation_time -= 1
                if self.animation_time == 0:
                    self.animation_time = 15
                    self.chest_3 = False
                    self.chest_2 = True
                    
            elif self.chest_2:
                self.animation_time -= 1
                if self.animation_time == 0:
                    self.animation_time = 15
                    self.chest_2 = False
                    self.chest_1 = True
            
        
    def blitme(self):
        if self.chest_1:
            self.screen.blit(self.chest1_image_one, self.chest1_rect_one)
            
        elif self.chest_2:
            self.screen.blit(self.chest2_image_one, self.chest2_rect_one)
            self.screen.blit(self.chest2_image_two, self.chest2_rect_two)
            self.screen.blit(self.chest2_image_three, self.chest2_rect_three)
            self.screen.blit(self.chest2_image_four, self.chest2_rect_four)

        elif self.chest_3:
            self.screen.blit(self.chest3_image_one, self.chest3_rect_one)
            self.screen.blit(self.chest3_image_two, self.chest3_rect_two)
            self.screen.blit(self.chest3_image_three, self.chest3_rect_three)
            self.screen.blit(self.chest3_image_four, self.chest3_rect_four)