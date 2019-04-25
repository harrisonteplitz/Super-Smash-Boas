# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 14:22:15 2019

@author: Monkey2
"""

import pygame, random
pygame.init()


backgroundColor = 0,255,50
running = True
margin = 2  
rect_width = 50
rect_height = 50
num = 8
width, height = ((rect_width + margin)*num)+margin,((rect_height + margin)*num) + margin
screen = pygame.display.set_mode((width,height))
tile_coords = {}
main_char = pygame.image.load('pryor.jpg')
main_char = pygame.transform.scale(main_char, (50, 50))
main_char_rect = main_char.get_rect()
main_char_rect.centerx = margin + (rect_width/2)
main_char_rect.centery = margin + (rect_height/2)
left_pressed = 0
right_count = 0
up_count = 0
down_count = 0



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
            
    for row in range(num):
        for column in range(num):
            color = 100,42,42
            pygame.draw.rect(screen, color, [(margin + rect_width) * column + margin,
                              (margin + rect_height) * row + margin,
                              rect_width,
                              rect_height])
            tile_coords.update({(row,column):((margin + rect_width) * column + margin,
                              (margin + rect_height) * row + margin)})#update dictionary of tile positions 

    if key_in[pygame.K_LEFT] and left_pressed == 0:
        left_pressed = 1
        main_char_rect.centerx, main_char_rect.centery = ((main_char_rect.centerx + margin + rect_width), main_char_rect.centery)
        
    
    screen.blit(main_char, main_char_rect)
    pygame.display.update()
    