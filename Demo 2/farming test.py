# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 14:22:15 2019

@author: Monkey2
"""

import pygame, random
pygame.init()


backgroundColor = 255,255,0
running = True
margin = 2  
rect_width = 50
rect_height = 50
num = 8
width, height = ((rect_width + margin)*num)+margin,((rect_height + margin)*num) + margin
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
            
    for row in range(8):
        for column in range(8):
            color = 0,0,0
            pygame.draw.rect(screen, color, [(margin + rect_width) * column + margin,
                              (margin + rect_height) * row + margin,
                              rect_width,
                              rect_height])
    
    pygame.display.update()
    