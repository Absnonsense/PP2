import pygame
import random
import time
pygame.init()
w, h = 600, 600
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Snake Game")
GRID_SIZE = 20
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
FOOD_COLORS = {
    1: (255, 0, 0),  
    2: (255, 165, 0), 
    3: (255, 255, 0), 
}
class Food:
    def __init__(self):
        self.respawn()
    def respawn(self):
        self.pos = (random.randint(0, (w // GRID_SIZE) - 1) * GRID_SIZE,
                    random.randint(0, (h // GRID_SIZE) - 1) * GRID_SIZE)
        self.value = random.choice([1, 2, 3])
        self.spawn_time = time.time()
        self.lifespan = random.randint(5, 10)  # seconds
    def is_expired(self):
        return time.time() - self.spawn_time > self.lifespan
    def draw(self, screen):
        pygame.draw.rect(screen, FOOD_COLORS[self.value], (*self.pos, GRID_SIZE, GRID_SIZE))
snake = [(w // 2, h // 2)]
dx, dy = 0, -GRID_SIZE
food = Food()
score = 0
level = 1
speed = 10
running = True
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 20)
while running:
    screen.fill(BLACK)
    food.draw(screen)
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
    if new_head == food.pos:
        score += food.value
        if score % 5 == 0:
            level += 1
            speed += 2
        food.respawn()
    else:
        snake.pop()
    if food.is_expired():
        food.respawn()
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))
    pygame.display.update()
    clock.tick(speed)
pygame.quit()
