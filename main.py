import pygame

pygame.init()
# Creating a screen
screen = pygame.display.set_mode((800,600))

# title, icon
pygame.display.set_caption("Road Fighter")
icon = pygame.image.load("images\icon.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("images\player.png")
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0


def player(x,y):
    screen.blit(playerImg, (x,y))




running = True
while running:
    #Clear the screen
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
                print("LEFT")
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
                print("RIGHT")
            if event.key == pygame.K_UP:
                playerY_change = -0.3
                print("UP")
            if event.key == pygame.K_DOWN:
                playerY_change = 0.3
                print("DOWN")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0


    playerX += playerX_change
    playerY += playerY_change
    player(playerX, playerY)

    #Update the display
    pygame.display.update()




