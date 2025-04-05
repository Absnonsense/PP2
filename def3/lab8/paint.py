import pygame, sys
pygame.init()
w, h = 800, 600
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Paint")
clock = pygame.time.Clock()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
colors = [BLACK, (255,0,0), (0,255,0), (0,0,255), (255,255,0)]
color_idx =0
brush_color = colors[color_idx]
canvas = pygame.Surface((w, h))
canvas.fill(WHITE)
drawing = False
shape = "free"
start_pos = None
def draw_ui():
    for i, c in enumerate(colors):
        pygame.draw.rect(screen, c, (10 + i*40, 10, 30, 30))
        if i == color_idx:
            pygame.draw.rect(screen, (100, 100, 100), (10 + i*40, 10, 30, 30), 3)
    pygame.draw.rect(screen, (200, 200, 200), (220, 10, 60, 30))
    screen.blit(font.render("Rect", 1, BLACK), (225, 15))
    pygame.draw.rect(screen, (200, 200, 200), (290, 10, 60, 30))
    screen.blit(font.render("Circ", 1, BLACK), (295, 15))
    pygame.draw.rect(screen, (200, 200, 200), (360, 10, 60, 30))
    screen.blit(font.render("Erase", 1, BLACK), (365, 15))
font = pygame.font.SysFont("Arial", 20)
while True:
    clock.tick(60)
    screen.fill((220, 220, 220))
    screen.blit(canvas, (0, 0))
    draw_ui()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if y < 50:
                # Color buttons
                for i in range(len(colors)):
                    if 10 + i*40 < x < 40 + i*40 and 10 < y < 40:
                        color_idx = i
                        brush_color = colors[color_idx]
                # Rect tool
                if 220 < x < 280 and 10 < y < 40:
                    shape = "rect"
                elif 290 < x < 350 and 10 < y < 40:
                    shape = "circ"
                elif 360 < x < 420 and 10 < y < 40:
                    shape = "erase"
                continue
            drawing = True
            start_pos = event.pos
            if shape == "free" or shape == "erase":
                pygame.draw.circle(canvas, WHITE if shape == "erase" else brush_color, event.pos, 5)
        elif event.type == pygame.MOUSEBUTTONUP:
            if drawing and shape in ["rect", "circ"]:
                end_pos = event.pos
                x0, y0 = start_pos
                x1, y1 = end_pos
                rect = pygame.Rect(min(x0, x1), min(y0, y1), abs(x1 - x0), abs(y1 - y0))
                if shape == "rect":
                    pygame.draw.rect(canvas, brush_color, rect, 2)
                elif shape == "circ":
                    center = rect.center
                    radius = max(rect.width // 2, rect.height // 2)
                    pygame.draw.circle(canvas, brush_color, center, radius, 2)
            drawing = False
            start_pos = None
        elif event.type == pygame.MOUSEMOTION:
            if drawing and shape in ["free", "erase"]:
                pygame.draw.circle(canvas, WHITE if shape == "erase" else brush_color, event.pos, 5)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                shape = "free"
    pygame.display.flip()
