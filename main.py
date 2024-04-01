import random

import pygame
import os
import math

pygame.init()
# Creating a screen
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width,screen_width))
FPS = 60

# title, icon and background
pygame.display.set_caption("Road Fighter")
icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)
background = pygame.image.load("images/background.png")
clock = pygame.time.Clock()
bg_height = background.get_height()

# define game variables. +1 is a buffer, kad nesitemptu is 2 bg, nes trecias tuscias
scroll = 0
tiles = math.ceil(screen_height / bg_height) + 1

# Player
playerImg = pygame.image.load("images/player.png")
playerX = 370
playerY = 680
playerX_change = 0
playerY_change = 0

# Other cars
#carImg = pygame.image.load("images/car.png")
#carX = random.randint()
#carY

def player(x,y):
    screen.blit(playerImg, (x,y))

running = True
while running:
    clock.tick(FPS)
    #Clear the screen
    for i in range(-1, tiles): # Start with -1 to ensure seamless transition
        screen.blit(background, (0, i * bg_height + scroll))
    # scroll background speed
    scroll += 10
    # reset scroll
    if abs(scroll) > bg_height:
        scroll = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -3.5
                print("LEFT")
            if event.key == pygame.K_RIGHT:
                playerX_change = 3.5
                print("RIGHT")
            if event.key == pygame.K_UP:
                playerY_change = -3.5
                print("UP")
            if event.key == pygame.K_DOWN:
                playerY_change = 3.5
                print("DOWN")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0

    # Boundaries of player
    playerX += playerX_change
    if playerX <= 70:
        playerX = 70
    elif playerX >= 600:
        playerX = 600
    playerY += playerY_change
    if playerY <= 0:
        playerY =0
    elif playerY >=680:
        playerY = 680
    player(playerX, playerY)

    #Update the display
    pygame.display.update()




