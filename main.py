import random
from pygame import mixer
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

# Background sound
mixer.music.load("Sounds/car_moving.wav")
mixer.music.play(-1) #-1 on loop
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
carImg = pygame.image.load("images/car.png")
carX = random.randint(70,600)
carY = 100
carY_change = 10
#timer variables
collision_timer = 0
collision_duration = 200 # delay for 3 sec

def player(x,y):
    screen.blit(playerImg, (x,y))
def car(x,y):
    screen.blit(carImg, (x,y))
def isCollision(carX, carY, playerX, playerY):
    distance = math.sqrt((math.pow(carX - playerX,2)) +(math.pow(carY - playerY,2)))
    if distance < 20:
        return True
    else:
        return False

#Game loop
running = True
while running:
    clock.tick(FPS)
    # Handle collision timer
    if collision_timer > 0:
        collision_timer -=1

    #Clear the screen
    for i in range(-1, tiles): # Start with -1 to ensure seamless transition
        screen.blit(background, (0, i * bg_height + scroll))

    # Scroll background speed if collision timer is 0
    if collision_timer == 0:
        scroll += 10

    # scroll background speed after collision
    scroll += 5
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

    # Movement of car
    carY += carY_change
    if carY >= 800:
        carY = -50
        carX = random.randint(70,600)
    # Collision
    collision = isCollision(carX, carY, playerX, playerY)
    if collision and collision_timer == 0 :
        print("Collision!")#TODO: something is wrong
        collision_timer = collision_duration # Start the collision timer

    player(playerX, playerY)
    car(carX, carY)

    #Update the display
    pygame.display.update()




