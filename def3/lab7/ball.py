import pygame
pygame.init()
w, h = 500, 500
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("ball")
r = 25
c = (255,0,0)
s = 20
x, y = w // 2, h // 2
running = True
while running:
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, c, (x, y), r)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and (y - r - s) > 0:
                y -= s
            elif event.key == pygame.K_DOWN and (y + r + s) < h:
                y += s
            elif event.key == pygame.K_LEFT and (x - r - s) > 0:
                x -= s
            elif event.key == pygame.K_RIGHT and (x + r + s) < w:
                x += s
    pygame.display.update()
pygame.quit()
