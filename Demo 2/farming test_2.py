# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 14:22:15 2019

@author: Monkey2
"""

import pygame
pygame.init()


backgroundColor = 0,255,0
running = True
margin = 2  
num_rows_columns = 8
soil_1 = pygame.image.load('Dirt.jpeg')
soil_1_rect = soil_1.get_rect()
soil_1_width = soil_1.get_width()
soil_1_height = soil_1.get_height()
soil_tiles = pygame.sprite.Group()
x = 0
y = 0

class soil(pygame.sprite.Sprite, x, y):
    def __init__(self, screen):
        self.x = x
        self.y = y
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load('Dirt.jpeg')
        self.rect = self.img.get_rect()
        self.rect.centerx = self.x
        self.rect.centery = self.y

width, height = ((soil_1_width + margin)*num_rows_columns)+margin,((soil_1_height + margin)*num_rows_columns) + margin
screen = pygame.display.set_mode((width,height))
while running:
    screen.fill(backgroundColor)
    key_in = pygame.key.get_pressed()
    
    if key_in[pygame.K_ESCAPE]:
        print("Quitting!")
        pygame.quit()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Quitting!")
            pygame.quit()
            
    for row in range(num_rows_columns):
        y = y + (soil_1_height/2) + margin
        for column in range(num_rows_columns):
            x = x + (soil_1_width/2) + margin
            soil_tiles.add(soil(screen))
            soil_tiles.update()
            soil_tiles.draw(screen)
        
    pygame.display.update()
    