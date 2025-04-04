import pygame
import sys
import time
pygame.init()
clock_img = pygame.image.load("image.jpeg") 
clock_rect = clock_img.get_rect()
w, h = clock_rect.width, clock_rect.height
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Clock")
center = (w// 2, h // 2)
minute = pygame.image.load("hand1.png")
second = pygame.image.load("hand2.png")
while True:
    screen.fill((255, 255, 255)) 
    screen.blit(clock_img, (0, 0)) 
    t = time.localtime()
    seconds = t.tm_sec
    minutes = t.tm_min
    second_angle = -seconds * 6
    minute_angle = -minutes * 6 
    sminute = pygame.transform.scale(minute, (int(minute.get_width() * 0.1), int(minute.get_height() * 0.1)))
    ssecond = pygame.transform.scale(second, (int(second.get_width() * 0.7), int(second.get_height() * 0.7)))
    rotated_second = pygame.transform.rotate(ssecond, second_angle)
    rotated_minute = pygame.transform.rotate(sminute, minute_angle)
    second_rect = rotated_second.get_rect(center=center)
    minute_rect = rotated_minute.get_rect(center=center)
    screen.blit(rotated_second, second_rect.topleft)
    screen.blit(rotated_minute, minute_rect.topleft)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.time.delay(1000)
