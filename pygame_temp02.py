# -*- coding: utf-8 -*-
"""
My First Game
"""
import pygame

''' 定義物件 define class --------------------------------------------------'''
class Missile:
    def __init__(self, pos):
        self.pos = [pos[0], pos[1]]
        
    def get_pos(self):
        return self.pos
    
    def set_pos(self, pos):
        self.pos = [pos[0], pos[1]]

''' 定義函數 define function -----------------------------------------------'''
def process_missile_group(m_group):
    remove_mg = set([])
    for m in m_group:
        m_pos = m.get_pos()
        if m_pos[1] <=0:
            remove_mg.add(m)
    if len(remove_mg) > 0:
        m_group.symmetric_difference_update(remove_mg)
def update_missile(m_group):
     if len(m_group) > 0:
         for m in m_group:
             m_pos = m.get_pos()
             screen.blit(missile_png, (m_pos[0], m_pos[1]))
             new_pos = [m_pos[0], m_pos[1] - 10]
             m.set_pos(new_pos)

''' 變數宣告 ---------------------------------------------------------------'''
screen_w, screen_h = 400, 640
mouseX, mouseY = 0, 0
missileX, missileY = 0, 0
score = 0
life = 3
missile_grp = set([]) #set

''' 遊戲設定 ---------------------------------------------------------------'''
pygame.init() #initial 初始化
clock = pygame.time.Clock()
''' 場景設定 ---------------------------------------------------------------'''
screen = pygame.display.set_mode((screen_w, screen_h))
title = pygame.display.set_caption("My First Game")
hide_cusor = pygame.mouse.set_visible(1) #隱藏鼠標
clock = pygame.time.Clock() 
''' 載入圖片和聲音檔案-------------------------------------------------------'''
ship = pygame.image.load('tship.png')
ship_icon = pygame.transform.scale(ship, (30, 30))
missile_png = pygame.image.load('missile.png')
''' 文字設定----------------------------------------------------------------'''
font = pygame.font.SysFont("consolas", 20)
''' text = font.render("要顯示的文字", 減少鋸齒, (R, G, B)) '''
text1 = font.render("Anti-Corona", True, (80, 80, 150))
text2 = font.render("Defeat COVID-19", True, (150, 200, 150))
text_score = font.render("Socre:", True, (10, 20, 30))
text_score_pt = font.render(str(score), True, (10, 20, 30))
''' Sprites ---------------------------------------------------------------'''
run =  True
while run:
    '''---------------------------------------------------------------------'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            #buttons = pygame.mouse.get_pressed()
            if event.button == 1:
                print('滑鼠左鍵')
                missile = Missile([mouseX-10, mouseY-60])
                missile_grp.add(missile)
                score = score + 10
                text_score_pt = font.render(str(score), True, (10, 20, 30))
                print(score)
            if event.button == 2:
                print('滑鼠中鍵')
            if event.button == 3:
                print('滑鼠右鍵')
            if event.button == 4:
                print('滾輪向上')
            if event.button == 5:
                print('滾輪向下')
        if event.type == pygame.MOUSEMOTION:
            mouseX, mouseY = pygame.mouse.get_pos()
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_z]:
                pass
            if keys[pygame.K_x]:
                pass
            if keys[pygame.K_c]:
                pass
            if keys[pygame.K_v]:
                pass
                
        #print(event)
    ''' 程式運算、計算-------------------------------------------------------'''
    #mouseX, mouseY = pygame.mouse.get_pos() #取得鼠標x,y座標值
    '''buttons = pygame.mouse.get_pressed()
    if buttons[0] == 1:
        print('滑鼠左鍵')
    if buttons[1] == 1:
        print('滑鼠中鍵')
    if buttons[2] == 1:
        print('滑鼠右鍵')
    '''

    '''把所有文字、圖片依序畫在場景內-----------------------------------------'''
    screen.fill((255,255,255)) #背景顏色
    screen.blit(text1, (120, 80))
    screen.blit(text2, (120, 120))
    screen.blit(text_score, (10, 10))
    screen.blit(text_score_pt, (180, 10))
    for i in range(0, life):
        screen.blit(ship_icon, (5 + i*33, screen_h - 33))
    process_missile_group(missile_grp)
    update_missile(missile_grp)
    #screen.blit(missile, (missileX, missileY))
    screen.blit(ship, (mouseX - 45, mouseY - 45))
    clock.tick(60)
    '''---------------------------------------------------------------------'''
    pygame.display.flip() #刷新畫面
'''--while loop end---------------------------------------------------------'''
pygame.quit() #quit 結束pygame















