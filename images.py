import pygame 

pygame.init() 
pygame.mixer.init()

WIDTH = 800 
HEIGHT = 600 
BACKGROUND = (0, 0, 0) 

screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
clock = pygame.time.Clock() 

pkm = pygame.image.load("Images/Charjabug.png") 
pkm = pygame.transform.scale(pkm, (50, 50)) 
pkm_rect = pkm.get_rect(center=(WIDTH // 2, HEIGHT // 2)) 

pkmx = WIDTH // 2 
pkmy = HEIGHT // 2 

tracks = {
    
}
pygame.mixer.music.load("tvBackground.mp3")
pygame.mixer.music.set_volume(0.6)
pygame.mixer.music.play(-1)

SPEED = 3
dx = SPEED 
dy = SPEED 

running = True 

while running: 
    screen.fill(BACKGROUND) 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 

    pkmx += dx 
    pkmy += dy 

    if pkmx - 50 <= 0 or pkmx + 50 >= WIDTH: 
        dx = -dx 
        pygame.mixer.sound.play()

    if pkmy - 61 <= 0 or pkmy + 61 >= HEIGHT: 
        dy = -dy 

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        screen.blit(pkm, (pkmx - 50, pkmy - 61)) 
        x = 10
        pygame.display.flip()
    else:
        pygame.display.flip()

    clock.tick(60) 

pygame.quit()