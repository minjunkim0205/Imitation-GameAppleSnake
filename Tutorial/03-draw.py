# Import library
import pygame

# Game option
WINDOW_HEIGHT = 360
WINDOW_WIDTH = 640

# Color
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)
BLUE = pygame.Color(0, 0, 255)

# Initialising pygame
pygame.init()

# Initialise game window
pygame.display.set_caption("AppleSnake Game")
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Game
running = True

# Main loop
while running:
    # Key event
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Refresh game screen
    window.fill(BLACK)
    pygame.draw.rect(window, RED, [0 * 10, 0 * 10, 10, 10])
    pygame.draw.rect(window, GREEN, [10 * 10, 10 * 10, 10, 10])
    pygame.draw.rect(window, BLUE, [(WINDOW_WIDTH // 10 - 1) * 10, (WINDOW_HEIGHT // 10 - 1) * 10, 10, 10])
    window.blit(pygame.font.SysFont(None, 25).render("Hello", True, WHITE), (10, 10))
    pygame.display.update()

# Quit
pygame.quit()
quit()
