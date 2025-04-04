import pygame
import random
pygame.init()
w, h = 600, 600
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Snake Game")
GRID_SIZE = 20
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
snake = [(w // 2, h // 2)]
dx, dy = 0, -GRID_SIZE
food = (random.randint(0, (w // GRID_SIZE) - 1) * GRID_SIZE, random.randint(0, (h // GRID_SIZE) - 1) * GRID_SIZE)
speed = 10
score = 0
level = 1
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, (*food, GRID_SIZE, GRID_SIZE))
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, GRID_SIZE, GRID_SIZE))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dy == 0:
                dx, dy = 0, -GRID_SIZE
            elif event.key == pygame.K_DOWN and dy == 0:
                dx, dy = 0, GRID_SIZE
            elif event.key == pygame.K_LEFT and dx == 0:
                dx, dy = -GRID_SIZE, 0
            elif event.key == pygame.K_RIGHT and dx == 0:
                dx, dy = GRID_SIZE, 0
    new_head = (snake[0][0] + dx, snake[0][1] + dy)
    if new_head[0] < 0 or new_head[0] >= w or new_head[1] < 0 or new_head[1] >= h or new_head in snake:
        running = False
    snake.insert(0, new_head)
    if new_head == food:
        score += 1
        if score % 3 == 0:
            level += 1
            speed += 2
        food = (random.randint(0, (w // GRID_SIZE) - 1) * GRID_SIZE, random.randint(0, (h // GRID_SIZE) - 1) * GRID_SIZE)
    else:
        snake.pop()
    pygame.display.update()
    clock.tick(speed)
pygame.quit()
