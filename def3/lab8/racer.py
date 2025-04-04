import pygame, random
pygame.init()
pygame.mixer.init()
w, h = 600, 800
s = pygame.display.set_mode((w, h))
pygame.display.set_caption("racer")
clock = pygame.time.Clock()
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YEL = (255,255,0)
score = 0
coins = 0
pygame.mixer.music.load("inochi.mp3")
pygame.mixer.music.play(-1)
coin_snd = pygame.mixer.Sound("good.mp3")
f = pygame.font.SysFont("Arial", 30)
class P(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img = pygame.Surface((50, 80))
        self.img.fill((0,0,255))
        self.rect = self.img.get_rect(center=(w//2, h-100))
        self.spd = 5
    def update(self, k):
        if k[pygame.K_LEFT] and self.rect.left > 0: self.rect.x -= self.spd
        if k[pygame.K_RIGHT] and self.rect.right < w: self.rect.x += self.spd
    def draw(self): s.blit(self.img, self.rect)
class E(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img = pygame.Surface((50, 80))
        self.img.fill(RED)
        self.rect = self.img.get_rect(x=random.randint(0, w-50), y=-80)
        self.spd = random.randint(5,10)
    def update(self):
        global score
        self.rect.y += self.spd
        if self.rect.top > h:
            self.rect.y = -80
            self.rect.x = random.randint(0, w-50)
            score += 1
    def draw(self): s.blit(self.img, self.rect)
class C(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img = pygame.Surface((30, 30), pygame.SRCALPHA)
        pygame.draw.circle(self.img, YEL, (15,15), 15)
        self.rect = self.img.get_rect(x=random.randint(0, w-30), y=random.randint(-800, -30))
        self.spd = 4
    def update(self):
        self.rect.y += self.spd
        if self.rect.top > h:
            self.rect.y = random.randint(-800, -30)
            self.rect.x = random.randint(0, w-30)
    def draw(self): s.blit(self.img, self.rect)
p = P()
es = [E() for _ in range(5)]
cs = [C() for _ in range(3)]
run = True
while run:
    clock.tick(60)
    k = pygame.key.get_pressed()
    for e in pygame.event.get():
        if e.type == pygame.QUIT: run = False
    p.update(k)
    for e in es: e.update()
    for c in cs: c.update()
    if any(p.rect.colliderect(e.rect) for e in es):
        pygame.mixer.music.stop()
        print("crashed")
        run = False
    for c in cs:
        if p.rect.colliderect(c.rect):
            coin_snd.play()
            coins += 1
            c.rect.y = random.randint(-800, -30)
            c.rect.x = random.randint(0, w-30)
    s.fill(BLACK)
    p.draw()
    for e in es: e.draw()
    for c in cs: c.draw()
    s.blit(f.render(f"Score: {score}", 1, WHITE), (10,10))
    s.blit(f.render(f"Coins: {coins}", 1, YEL), (w-150,10))
    pygame.display.update()
pygame.quit()
