# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 21:22:44 2019

@author: kaust
"""

import pygame, random
pygame.init()


width, height = 800,600
backgroundColor = 0, 0, 0
background_img = pygame.image.load('bckgrnd.jpg')
loss_img = pygame.image.load('game_over.jpg')
screen = pygame.display.set_mode((width,height))


main_char = pygame.image.load('pryor.jpg')
main_char_rect = main_char.get_rect()
main_char_rect.centerx = width/2
main_char_rect.centery = height/2

enemy_char = pygame.image.load('error.jpg')
enemy_char_rect = enemy_char.get_rect()
enemy_char_speed = [5,5]

running = True

def game_over():
    screen.fill(backgroundColor)
    screen.blit(loss_img, (0,0))
    pygame.display.update()
    pygame.time.delay(1000)

while running:
    
    key_in = pygame.key.get_pressed()
    
    if key_in[pygame.K_ESCAPE]:
        print("Quitting!")
        pygame.quit()
        #raise SystemExit
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Quitting!")
            pygame.quit()
            #raise SystemExit
    enemy_char_rect = enemy_char_rect.move(enemy_char_speed)
    if enemy_char_rect.left < 0 or enemy_char_rect.right > width:
        enemy_char_speed[0] = -enemy_char_speed[0]
    if enemy_char_rect.top < 0 or enemy_char_rect.bottom > height:
        enemy_char_speed[1] = -enemy_char_speed[1]

        
    if key_in[pygame.K_LEFT]:
        main_char_rect.centerx -= 10
        if main_char_rect.left < 0:
            main_char_rect.centerx += 2
    if key_in[pygame.K_RIGHT]:
        main_char_rect.centerx += 10
        if main_char_rect.right > width:
            main_char_rect.centerx -= 2
    if key_in[pygame.K_DOWN]:
        main_char_rect.centery += 10
        if main_char_rect.bottom > height:
            main_char_rect.centery -= 2
    if key_in[pygame.K_UP]:
        main_char_rect.centery -= 10
        if main_char_rect.top < 0:
            main_char_rect.centery += 2
    
    if main_char_rect.colliderect(enemy_char_rect):
        running = False
        game_over()
        pygame.display.quit()
        
        
        
    screen.fill(backgroundColor)
    screen.blit(background_img, (0,0))
    screen.blit(main_char, main_char_rect)
    screen.blit(enemy_char, enemy_char_rect)

    pygame.display.update()

    

    
