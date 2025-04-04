import pygame
pygame.init()
w, h = 800, 600
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Paint Shapes with Color")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
screen.fill(WHITE)
drawing = False
start_pos = None
shape_type = "square"
current_color = BLACK
font = pygame.font.SysFont(None, 24)
colors = [
    (255, 0, 0),  
    (0, 255, 0),   
    (0, 0, 255),  
    (0, 0, 0),     
    (255, 255, 0), 
    (255, 165, 0), 
    (128, 0, 128) 
]
color_buttons = []
for i, color in enumerate(colors):
    rect = pygame.Rect(10 + i * 40, 40, 30, 30)
    color_buttons.append((rect, color))
    pygame.draw.rect(screen, color, rect)
    pygame.draw.rect(screen, BLACK, rect, 2)
def draw_shape(start, end, shape, color):
    x1, y1 = start
    x2, y2 = end
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    left = min(x1, x2)
    top = min(y1, y2)
    if shape == "square":
        side = min(width, height)
        pygame.draw.rect(screen, color, (left, top, side, side), 2)
    elif shape == "right_triangle":
        pygame.draw.polygon(screen, color, [(x1, y1), (x2, y2), (x1, y2)], 2)
    elif shape == "equilateral_triangle":
        side = min(width, height)
        height_eq = (3 ** 0.5 / 2) * side
        pygame.draw.polygon(screen, color, [
            (x1, y1),
            (x1 + side, y1),
            (x1 + side / 2, y1 - height_eq)
        ], 2)
    elif shape == "rhombus":
        cx = (x1 + x2) // 2
        cy = (y1 + y2) // 2
        dx = abs(x2 - x1) // 2
        dy = abs(y2 - y1) // 2
        pygame.draw.polygon(screen, color, [
            (cx, cy - dy),
            (cx + dx, cy),
            (cx, cy + dy),
            (cx - dx, cy)
        ], 2)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                shape_type = "square"
            elif event.key == pygame.K_2:
                shape_type = "right_triangle"
            elif event.key == pygame.K_3:
                shape_type = "equilateral_triangle"
            elif event.key == pygame.K_4:
                shape_type = "rhombus"
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for rect, color in color_buttons:
                if rect.collidepoint(pos):
                    current_color = color
                    break
            else:
                drawing = True
                start_pos = pos
        elif event.type == pygame.MOUSEBUTTONUP:
            if drawing:
                end_pos = pygame.mouse.get_pos()
                draw_shape(start_pos, end_pos, shape_type, current_color)
                drawing = False
    for rect, color in color_buttons:
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, BLACK, rect, 2)
    info_text = font.render("1: Square  2: Right Triangle  3: Equilateral Triangle  4: Rhombus", True, BLACK)
    screen.blit(info_text, (10, 10))
    pygame.display.flip()
pygame.quit()
