# Example file showing a basic pygame "game loop"
import pygame
import random

# setup variables
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
PLAYER_SIZE = 25
PIPE_WIDTH = 70
PIPE_SPACING = 135

# game variables
player_y = 100
player_y_speed = 0

# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

# classes
class Pipe:
    def __init__(self, x_coordinate):
        self.x = x_coordinate
        self.y = random.randint(100, SCREEN_HEIGHT - 100)
    
    def draw(self):
        # top rectangle
        pygame.draw.rect(screen, "green", (
            self.x - PIPE_WIDTH / 2,
            0,
            PIPE_WIDTH,
            self.y - PIPE_SPACING / 2
        ))

        # bottom rectangle
        pygame.draw.rect(screen, "green", (
            self.x - PIPE_WIDTH / 2,
            self.y + PIPE_SPACING / 2,
            PIPE_WIDTH,
            SCREEN_HEIGHT - (self.y + PIPE_SPACING / 2)
        ))

pipe_list = [Pipe(SCREEN_WIDTH)]

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

    # RENDER YOUR GAME HERE
    for i in range(len(pipe_list)):
        pipe_list[i].draw()

    pygame.draw.circle(screen, "yellow", (100, player_y), PLAYER_SIZE)

    # moving the bird
    player_y += player_y_speed
    player_y_speed += 0.2

    if player_y > SCREEN_HEIGHT - PLAYER_SIZE:
        player_y = SCREEN_HEIGHT - PLAYER_SIZE
    if player_y < PLAYER_SIZE:
        player_y = PLAYER_SIZE
        player_y_speed = 0

    # moving the pipe
    for i in range(len(pipe_list) - 1, -1, -1):
        pipe_list[i].x -= 2
        if pipe_list[i].x == 100:
            pipe_list.append(Pipe(SCREEN_WIDTH))
        if pipe_list[i].x == -100:
            pipe_list.remove(pipe_list[i])

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()