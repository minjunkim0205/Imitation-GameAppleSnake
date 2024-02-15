# Import library
import pygame

# Game option
WINDOW_HEIGHT = 360
WINDOW_WIDTH = 640

# Initialising pygame
pygame.init()

# Initialise game window
pygame.display.set_caption("AppleSnake Game")
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Game
running = True

# Main loop
while running:
    # Refresh game screen
    pygame.display.update()

# Quit
pygame.quit()
quit()
