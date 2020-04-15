# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 15:16:50 2020

@author: Hubert
"""

import pygame
init = pygame.init()
screen = pygame.display.set_mode((400,300))
title = pygame.display.set_caption('PyGame Demo')
''' -----------------------------------------------------------------------'''
run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        print(event)
    '''--------------------------------------------------------------------'''
    # put your codes here
    '''--------------------------------------------------------------------'''
    update = pygame.display.update()
''' -----------------------------------------------------------------------'''   
close = pygame.quit()
