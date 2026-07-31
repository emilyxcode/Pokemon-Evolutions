import pygame
import random

pygame.init()
SPEED = 5

WHITE = (255, 255, 255)
font = pygame.font.Font(None, 50)

SCREEN_WIDTH, SCREEN_HEIGHT = 750, 500

pkm2 = pygame.image.load("Images/pokemon.png")
pkm2 = pygame.transform.scale(pkm2, (80, 101))

pkm = pygame.image.load("Images/pokemon - Copy.png")
pkm = pygame.transform.scale(pkm, (80, 101))

current_pkm = pkm

leppa = pygame.image.load("Images/Berries/leppa.png")
leppa_img = pygame.transform.scale(leppa, (40, 40))

aspear = pygame.image.load("Images/Berries/aspear.png")
aspear_img = pygame.transform.scale(aspear, (40, 40))

cheri = pygame.image.load("Images/Berries/cheri.png")
cheri_img = pygame.transform.scale(cheri, (40, 40))

chesto = pygame.image.load("Images/Berries/chesto.png")
chesto_img = pygame.transform.scale(chesto, (40, 40))

hopo = pygame.image.load("Images/Berries/hopo.png")
hopo_img = pygame.transform.scale(hopo, (40, 40))

lum = pygame.image.load("Images/Berries/lum.png")
lum_img = pygame.transform.scale(lum, (40, 40))

oran = pygame.image.load("Images/Berries/oran.png")
oran_img  = pygame.transform.scale(oran, (40, 40))

pecha = pygame.image.load("Images/Berries/pecha.png")
pecha_img = pygame.transform.scale(pecha, (40, 40))

persim = pygame.image.load("Images/Berries/persim.png")
persim_img = pygame.transform.scale(persim, (40, 40))

rawst = pygame.image.load("Images/Berries/rawst.png")
rawst_img = pygame.transform.scale(rawst, (40, 40))

salac = pygame.image.load("Images/Berries/salac.png")
salac_img = pygame.transform.scale(salac, (40, 40))

sitrus = pygame.image.load("Images/Berries/sitrus.png")
sitrus_img = pygame.transform.scale(sitrus, (40, 40))

background = pygame.image.load("Images/background.png")
background = pygame.transform.scale(background, (750, 500))

base = pygame.image.load("Images/base.png")
base = pygame.transform.scale(base, (750, 80))

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = True

pkm_rect = pkm.get_rect(center=(50, 380))
base_rect = base.get_rect(center=(375, 470))

leppa_rect = leppa.get_rect(center=(15, 0))
aspear_rect = aspear.get_rect(center=(15, 0))
cheri_rect = cheri.get_rect(center=(15, 0))
chesto_rect = chesto.get_rect(center=(15, 0))
oran_rect = oran.get_rect(center=(15, 0))
pecha_rect = pecha.get_rect(center=(15, 0))
persim_rect = persim.get_rect(center=(15, 0))
rawst_rect = rawst.get_rect(center=(15, 0))
sitrus_rect = sitrus.get_rect(center=(15, 0))

is_jumping = False
jump_velocity = 15
gravity = 1

clock = pygame.time.Clock()

berries = []       
BERRY_SPEED = 4     
SPAWN_EVENT = pygame.USEREVENT + 1
WAIT_EVENT = pygame.USEREVENT + 1

pygame.time.set_timer(SPAWN_EVENT, random.randint(1000, 2500)) 

score = 0

gameover = False

berrylist = [leppa_img, aspear_img, cheri_img, chesto_img, hopo_img, lum_img, oran_img, pecha_img, persim_img, rawst_img, salac_img, sitrus_img]
whichberry = random.choice(berrylist)

newspeed = 5
speedx = 1000
speedy = 2500

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    if event.type == SPAWN_EVENT:
        while len(berries) < 1:
            x_pos = random.randint(10, 710)
            whichberry = random.choice(berrylist)
            new_berry = whichberry.get_rect(topleft=(x_pos, -30))
            berries.append(new_berry)
            speedx -= 1
            speedy -= 1
        
        pygame.time.set_timer(SPAWN_EVENT, random.randint(speedx, speedy))

    screen.fill((0, 0, 0))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        current_pkm = pkm2  
        pkm_rect.x -= SPEED
        
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        current_pkm = pkm 
        pkm_rect.x += SPEED
        
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        is_jumping = True

    if is_jumping:
        pkm_rect.y -= jump_velocity
        jump_velocity -= gravity
        
        if pkm_rect.bottom >= 443:
            pkm_rect.bottom = 443
            is_jumping = False
            jump_velocity = 15

    if pkm_rect.left < 0:
        pkm_rect.left = 0
    if pkm_rect.right > SCREEN_WIDTH:
        pkm_rect.right = SCREEN_WIDTH
    if pkm_rect.top < 0:
        pkm_rect.top = 0
    if pkm_rect.bottom > SCREEN_HEIGHT:
        pkm_rect.bottom = SCREEN_HEIGHT

    x = random.randint(10, 740)
    time = random.randint(100, 1000)

    text_surface = font.render("SCORE: " + str(score), True, WHITE)

    screen.blit(whichberry, (x, 0))
    screen.blit(background, (0, 0))
    screen.blit(base, base_rect)
    screen.blit(current_pkm, pkm_rect)
    screen.blit(text_surface, (10, 10))

    for berry in berries[:]:
        berry.y += BERRY_SPEED
        screen.blit(whichberry, berry)
        
        if pkm_rect.colliderect(berry):
            if whichberry == hopo_img:
                berries.remove(berry)
                SPEED -= 1
            elif whichberry == cheri_img or whichberry == lum_img:
                berries.remove(berry)
                score += 1
                SPEED = newspeed
            elif whichberry == salac_img:
                berries.remove(berry)
                score += 1
                newspeed += 1
                SPEED += 1
            else:
                berries.remove(berry)
                score += 1

        if berry.colliderect(base_rect):
            berries.remove(berry)
            if whichberry != hopo_img:
                gameover = True
            else:
                pass
            
        elif berry.top > SCREEN_HEIGHT:
            berries.remove(berry)

    if gameover == True:
        text = font.render("GAME OVER!", True, WHITE)    
        screen.blit(text, (375 - text.get_width()//2, 250 - text.get_height()//2))
        running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()