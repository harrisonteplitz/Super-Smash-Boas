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
score = 0 #initial score

pressed = 0
grid = []


# Clock initialization
clock = pygame.time.Clock()
font = pygame.font.Font(None, 25)
frame_count = 0
frame_rate = 60
start_time = 90

for row in range(num):
    grid.append([])
    for column in range(num):
        grid[row].append(0)


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
            
    if key_in[pygame.K_RIGHT] and sum(key_in) == 1 and pressed == 0:
        pressed = 1
        #print(left_count)
        main_char_rect.centerx = main_char_rect.centerx + margin + rect_width
        
        if main_char_rect.right > width:
            main_char_rect.centerx = main_char_rect.centerx - margin - rect_width
            
    if key_in[pygame.K_LEFT] and sum(key_in) == 1 and pressed == 0:
        pressed = 1
        #print(left_count)
        main_char_rect.centerx = main_char_rect.centerx - margin - rect_width
        
        if main_char_rect.left < margin:
            main_char_rect.centerx = main_char_rect.centerx + margin + rect_width
    
    if key_in[pygame.K_DOWN] and sum(key_in) == 1 and pressed == 0:
        pressed = 1
        #print(left_count)
        main_char_rect.centery = main_char_rect.centery + margin + rect_height
        
        if main_char_rect.bottom >height - margin:
            main_char_rect.centery = main_char_rect.centery - margin - rect_height
        
    if key_in[pygame.K_UP] and sum(key_in) == 1 and pressed == 0:
        pressed = 1
        #print(left_count)
        main_char_rect.centery = main_char_rect.centery - margin - rect_height
        
        if main_char_rect.top < margin:
            main_char_rect.centery = main_char_rect.centery + margin + rect_height
    if key_in[pygame.K_SPACE]:
        column = main_char_rect.centerx // (margin + rect_width)
        row = main_char_rect.centery // (margin + rect_height)
        grid[row][column] = 1
    if event.type == pygame.KEYUP:
        pressed = 0   
        
    for row in range(num):
        for column in range(num):
            color = 139,69,19 #"saddlebrown
            if grid[row][column] == 1:
                color = 0,255,100
            pygame.draw.rect(screen, color, [(margin + rect_width) * column + margin,
                              (margin + rect_height) * row + margin,
                              rect_width,
                              rect_height])
            tile_coords.update({(row,column):((margin + rect_width) * column + margin,
                              (margin + rect_height) * row + margin)})#update dictionary of tile positions
    screen.blit(main_char, main_char_rect)
#Clock printed to screen
    total_seconds = start_time - (frame_count // frame_rate)
    if total_seconds < 0:
        total_seconds = 0
 
    # Divide by 60 to get total minutes
    minutes = total_seconds // 60
 
    # Use modulus (remainder) to get seconds
    seconds = total_seconds % 60
 
    # Use python string formatting to format in leading zeros
    output_string = "Time left: {0:02}:{1:02} | Score: ".format(minutes, seconds) #need to add score variable in this string
 
    # Blit to the screen
    text = font.render(output_string, True, (0,0,0))
 
    screen.blit(text, [150, 380])
 
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    frame_count += 1
 
    # Limit frames per second
    clock.tick(frame_rate)

    pygame.display.update()
    
