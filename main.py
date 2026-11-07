# Example file showing a basic pygame "game loop"
import pygame

# setup variables
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
PLAYER_SIZE = 25

# game variables
player_y = 100
player_y_speed = 0

# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            player_y_speed = -5

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("#a4d3fd")

    pygame.draw.circle(screen, "yellow", (100, player_y), PLAYER_SIZE)

    player_y = player_y + player_y_speed
    player_y_speed = player_y_speed + 0.2

    if player_y > SCREEN_HEIGHT - PLAYER_SIZE:
        player_y = SCREEN_HEIGHT - PLAYER_SIZE
    if player_y < PLAYER_SIZE:
        player_y = PLAYER_SIZE
        player_y_speed = 0
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()