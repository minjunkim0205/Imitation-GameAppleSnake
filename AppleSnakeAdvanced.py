# Import library
import pygame
import random

# Game option
WINDOW_HEIGHT = 360
WINDOW_WIDTH = 640
WINDOW_FPS = 60

# Color
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)
BLUE = pygame.Color(0, 0, 255)
DARK_GREEN = pygame.Color(1, 50, 32)

# Initialising pygame
pygame.init()

# Initialise game window
pygame.display.set_caption("AppleSnake Game")
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# FPS
fps = pygame.time.Clock()

# Game c
runtime = 0
running = [True, True, False, False] # 0:Runtime, 1:Menu, 2:InGame, 3:GameOver

# Management loop
while running[0]:
    # Main menu management
    
    # Main menu loop
    while running[1]:
        # Frame Per Second / Refresh Rate
        delta_time = fps.tick(WINDOW_FPS)
        runtime += delta_time
        # Key event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = [False, False, False, False]
        # Use legacy input
        pressed = pygame.key.get_pressed()
        key = [
            pressed[pygame.K_RETURN],
            pressed[pygame.K_UP],
            pressed[pygame.K_DOWN],
            pressed[pygame.K_LEFT],
            pressed[pygame.K_RIGHT],
            pressed[pygame.K_SPACE]
        ]
        # Refresh game screen
        window.fill(BLACK)
        window.blit(pygame.font.SysFont(None, 25).render(str(key), True, WHITE), (10, 10))
        pygame.display.update()
# Exit pygame
pygame.quit()
quit()
 