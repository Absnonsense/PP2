import pygame
import os
pygame.init()
pygame.mixer.init()
m1 = "good.mp3"
m2 = "Kick.mp3"
m3 = "Ino.mp3"
pl = [m1, m2, m3]
current = 0
pygame.display.set_mode((300, 300))
def play_music():
    pygame.mixer.music.load(pl[current])
    pygame.mixer.music.play()
    print(f"Now playing: {pl[current]}")
def stop_music():
    pygame.mixer.music.stop()
    print("Music stopped.")
def next_track():
    global current
    current = current +1
    play_music()
def previous_track():
    global current
    current = current -1
    play_music()
running = True
pygame.mixer.music.load(pl[current])
pygame.mixer.music.play()
print(f"Now playing: {pl[current]}")
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                    print("Music paused.")
                else:
                    pygame.mixer.music.unpause()
                    print("Music resumed.")
            elif event.key == pygame.K_s:  
                stop_music()
            elif event.key == pygame.K_n:
                next_track()
            elif event.key == pygame.K_p:
                previous_track()
pygame.mixer.quit()
pygame.mixer.init()
pygame.quit()
