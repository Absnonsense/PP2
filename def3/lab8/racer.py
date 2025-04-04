import pygame
import random
import sys
pygame.init()
pygame.mixer.init()
w, h = 600, 800
fps = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Racer Game")
clock = pygame.time.Clock()
pygame.mixer.music.load("inochi.mp3")
pygame.mixer.music.play(-1)
coin_sound = pygame.mixer.Sound("good.mp3")
font = pygame.font.SysFont("Arial", 30)
score = 0
coin_c = 0
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 80))
        self.image.fill((0, 0, 255))  # Blue car
        self.rect = self.image.get_rect(center=(w // 2, h - 100))
        self.speed = 5
    def update(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < w:
            self.rect.x += self.speed
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 80))
        self.image.fill(RED)
        self.rect = self.image.get_rect(x=random.randint(0, w - 50), y=-80)
        self.speed = random.randint(5, 10)
    def update(self):
        self.rect.y += self.speed
        if self.rect.top > h:
            self.rect.y = -80
            self.rect.x = random.randint(0, w - 50)
            global score
            score += 1
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        pygame.draw.circle(self.image, YELLOW, (15, 15), 15)
        self.rect = self.image.get_rect(x=random.randint(0, w - 30), y=random.randint(-800, -30))
        self.speed = 4
    def update(self):
        self.rect.y += self.speed
        if self.rect.top > h:
            self.rect.y = random.randint(-800, -30)
            self.rect.x = random.randint(0, w - 30)
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
coins = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for _ in range(5):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)
for _ in range(3):
    coin = Coin()
    all_sprites.add(coin)
    coins.add(coin)
running = True
while running:
    clock.tick(fps)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    player.update(keys)
    enemies.update()
    coins.update()
    if pygame.sprite.spritecollideany(player, enemies):
        pygame.mixer.music.stop()
        print("crashed")
        running = False
    collected = pygame.sprite.spritecollide(player, coins, False)
    for coin in collected:
        coin_sound.play()
        coin_c += 1
        coin.rect.y = random.randint(-800, -30)
        coin.rect.x = random.randint(0, w - 30)
    screen.fill(BLACK)
    all_sprites.draw(screen)
    score_text = font.render(f"Score: {score}", True, WHITE)
    coin_text = font.render(f"Coins: {coin_c}", True, YELLOW)
    screen.blit(score_text, (10, 10))
    screen.blit(coin_text, (w - 150, 10))
    pygame.display.flip()
pygame.quit()
sys.exit()

