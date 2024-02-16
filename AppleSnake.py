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

# Game
running = True
time = 0
score = 0
direction = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}

# Snake
snake_direction = direction["right"]
snake = [[(WINDOW_HEIGHT // 10) / 2, (WINDOW_WIDTH // 10) / 2],
         [(WINDOW_HEIGHT // 10) / 2, (WINDOW_WIDTH // 10) / 2 - 1],
         [(WINDOW_HEIGHT // 10) / 2, (WINDOW_WIDTH // 10) / 2 - 2],
         [(WINDOW_HEIGHT // 10) / 2, (WINDOW_WIDTH // 10) / 2 - 3]]
snake_time = 0
snake_tick = 100
snake_booster = False

# Apple
apple = [random.randrange(1, (WINDOW_HEIGHT // 10)), random.randrange(1, (WINDOW_WIDTH // 10))]

# Main loop
while running:
    # Frame Per Second / Refresh Rate
    delta_time = fps.tick(WINDOW_FPS)
    time += delta_time

    # Key event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if snake_direction != direction["down"]:
                    snake_direction = direction["up"]
            if event.key == pygame.K_DOWN:
                if snake_direction != direction["up"]:
                    snake_direction = direction["down"]
            if event.key == pygame.K_LEFT:
                if snake_direction != direction["right"]:
                    snake_direction = direction["left"]
            if event.key == pygame.K_RIGHT:
                if snake_direction != direction["left"]:
                    snake_direction = direction["right"]
            if event.key == pygame.K_SPACE:
                snake_booster = True
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                snake_booster = False

    # Snake, Apple
    if time - snake_time >= snake_tick or snake_booster:
        snake.insert(0, [snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1]])
        if apple in snake:
            score += 500
            snake_tick += -1
            apple = [random.randrange(1, (WINDOW_HEIGHT // 10)), random.randrange(1, (WINDOW_WIDTH // 10))]
        else:
            snake.pop()
        snake_time = time

    # Game over
    if snake[0][0] < 0 or WINDOW_HEIGHT // 10 <= snake[0][0] or snake[0][1] < 0 or WINDOW_WIDTH // 10 <= snake[0][1]:
        running = False
    if snake[0] in snake[1:]:
        running = False

    # Refresh game screen
    window.fill(BLACK)
    pygame.draw.rect(window, DARK_GREEN, [snake[0][1] * 10, snake[0][0] * 10, 10, 10])
    for snake_element in snake[1:]:
        pygame.draw.rect(window, GREEN, [snake_element[1] * 10, snake_element[0] * 10, 10, 10])
    pygame.draw.rect(window, RED, [apple[1] * 10, apple[0] * 10, 10, 10])
    window.blit(pygame.font.SysFont(None, 25).render(str(score), True, WHITE), (10, 10))
    pygame.display.update()

# Quit
print("Your score is : " + str(score))
pygame.quit()
quit()
