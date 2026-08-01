import pygame
import random
import math

FLOAT_HEIGHT = 14
FLOAT_BOB_RANGE = 4
FLOAT_BOB_SPEED = 4

pygame.init()
pygame.mixer.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 750, 500
tracks = {
    "background": "background.mp3",
    "level_up": "level up.mp3",
    "evolve": "evolve.mp3",
    "win": "win.mp3"
}

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
next_crystal = True
crystal_collected = False
gengar_state = False

SPEED = 5
WHITE = (255, 255, 255)
font = pygame.font.Font(None, 30)
exp = 0
count = 0
count_two = 0


pygame.mixer.music.load(tracks["background"])
level_up_sound = pygame.mixer.Sound(tracks["level_up"])
evolve_sound = pygame.mixer.Sound(tracks["evolve"])
level_up_sound.set_volume(0.1)
evolve_sound.set_volume(0.3)
pygame.mixer.music.set_volume(0.6)
pygame.mixer.music.play(-1)

instructions = pygame.image.load("Images/instructions.png")
instructions = pygame.transform.scale(instructions, (750, 490))

deco = pygame.image.load("Images/Mossy Tileset/Hanging Plants 3.png")
deco = pygame.transform.scale(deco, (240, 160))

platform1 = pygame.image.load("Images/Mossy Tileset/Platform Long.png")
platform1 = platform1.convert_alpha()
platform1 = pygame.transform.scale(platform1, (350, 60))
platformrect = pygame.Rect((330, 310, 340, 45))
platformrect2 = pygame.Rect((-10, 200, 340, 45))

sparkly = pygame.image.load("sparkly.png.png")
sparkly = pygame.transform.scale(sparkly, (35, 35))

platform1 = pygame.image.load("Images/Mossy Tileset/Platform Long.png")
platform1 = platform1.convert_alpha()
platform1 = pygame.transform.scale(platform1, (350, 60))
platformrect = pygame.Rect((330, 310, 340, 45))
platformrect2 = pygame.Rect((-10, 200, 340, 45))

platform2 = pygame.image.load("Images/Mossy Tileset/Platform XS.png")
platform2 = platform2.convert_alpha()
platform2 = pygame.transform.scale(platform2, (60, 50))
platformrect3 = pygame.Rect((450, 150, 60, 40))


platform3 = pygame.image.load("Images/Mossy Tileset/Platform Medium.png")
platform3 = platform3.convert_alpha()
platform3 = pygame.transform.scale(platform3, (210, 60))
platformrect4 = pygame.Rect((570, 70, 210, 60))


platformrect3_y_min = 90
platformrect3_y_max = 200
platformrect3_speed = 2


expcandyxs = pygame.image.load("Images/expcandyxs.webp")
expcandyxs= pygame.transform.scale(expcandyxs, (30, 30))


expcandym = pygame.image.load("Images/exp.candym.png")
expcandym= pygame.transform.scale(expcandym, (18, 18))


expcandyl = pygame.image.load("Images/exp.candyl.png")
expcandyl= pygame.transform.scale(expcandyl, (20, 20))


expcandy_spawn_points = ((400, 285), (550, 285), (60, 175), (250, 175), (600, 45), (650, 45), (700, 45))
# expcandy1.center = random.choice(expcandy_spawn_points)


linkingcord = pygame.image.load("Images/linkingcord.png")
linkingcord = pygame.transform.scale(linkingcord, (30, 30))
linkincord = linkingcord.get_rect()
linkincord.center = (random.choice(expcandy_spawn_points))

moonstone = pygame.image.load("Images/moonstone.png")
moonstone = pygame.transform.scale(moonstone, (20, 20))
moonstone_rect = moonstone.get_rect()
moonstone_rect.center = (random.choice(expcandy_spawn_points))

gastly1_left = pygame.image.load("Images/cleffa.png")
gastly1_left = pygame.transform.scale(gastly1_left, (30, 30))
gastly1_right = pygame.transform.flip(gastly1_left, True, False)


haunter1_left = pygame.image.load("Images/clefairy.png")
haunter1_left = pygame.transform.scale(haunter1_left, (45, 45))
haunter1_right = pygame.transform.flip(haunter1_left, True, False)


gengar1_left = pygame.image.load("Images/clefable.png")
gengar1_left = pygame.transform.scale(gengar1_left, (70, 70))
gengar1_right = pygame.transform.flip(gengar1_left, True, False)


pkm1_state = gastly1_left
background = pygame.image.load("Images/background.png")
background = pygame.transform.scale(background, (750, 500))


pkm1_rect = pkm1_state.get_rect(center = (700, 395))
pkm1_rect.bottom = 395


gastly2_left = pygame.image.load("Images/gastly.png")
gastly2_left = pygame.transform.scale(gastly2_left, (35, 40))
gastly2_right = pygame.transform.flip(gastly2_left, True, False)


haunter2_left = pygame.image.load("Images/haunter.png")
haunter2_left = pygame.transform.scale(haunter2_left, (60, 60))
haunter2_right = pygame.transform.flip(haunter2_left, True, False)


gengar2_left = pygame.image.load("Images/genger.png")
gengar2_left = pygame.transform.scale(gengar2_left, (70, 70))
gengar2_right = pygame.transform.flip(gengar2_left, True, False)


pkm2_state = gastly2_right
pkm2_rect = pkm2_state.get_rect(center = (50, 395))
pkm2_rect.bottom = 395
running = True


is_jumping1 = False
is_jumping2 = False
jump_velocity1 = 0
jump_velocity2 = 0
gravity = 1.5
spawnpoint = random.choice(expcandy_spawn_points)
type_of_candy = [expcandyxs, expcandym, expcandyl]


def spawn_candy():
    crystal_regions = random.randint(1, 5)
    candy_type = random.choice(type_of_candy)
    if crystal_regions == 1:
        candy_location_x = random.randint(40, 280)
        candy_location_y = random.randint(315, 330)
    if crystal_regions == 2:
        candy_location_x = random.randint(30, 440)
        candy_location_y = random.randint(100, 190)
    if crystal_regions == 3:
        candy_location_x = random.randint(345, 705)
        candy_location_y = random.randint(260, 310)
    if crystal_regions == 4:
        candy_location_x = random.randint(520, 600)
        candy_location_y = random.randint(140, 200)
    if crystal_regions == 5:
        candy_location_x = random.randint(530, 700)
        candy_location_y = random.randint(30, 70)

    candy_rect = candy_type.get_rect(center=(candy_location_x, candy_location_y))
    return candy_type, candy_rect

platforms = [platformrect, platformrect2, platformrect3, platformrect4]
GROUND_Y = 395


clock = pygame.time.Clock()
score = 0
gameover = False


SPAWN_EVENT = pygame.USEREVENT + 1


exp_clef = 0
exp_gen = 0
obstacle = []
gotcord1 = False
gotcord2 = False
evolved1 = False
evolved2 = False
enter = False
BLACK = (0, 0, 0)

candy_type, candy_rect = spawn_candy()[0], spawn_candy()[1]

while not enter:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            enter = True
    screen.blit(background, (0, 0))
    screen.blit(instructions, (0, 0))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        print("enter")
        enter = True
    pygame.display.flip()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # if event.type == SPAWN_EVENT:
       
    #     candy = False


    keys = pygame.key.get_pressed()


    if keys[pygame.K_LEFT]:
        pkm1_rect.x -= SPEED
        if exp_clef < 8000:
            pkm1_state = gastly1_left
        elif exp_clef >= 8000 and gotcord1 == False:
            print("now evolved!")
            pkm1_state = haunter1_left
        else:
            win = "Player 1"


    if keys[pygame.K_a]:
        pkm2_rect.x -= SPEED
        if exp_gen < 8000:
            pkm2_state = gastly2_left
        elif exp_gen >= 8000 and gotcord2 == False:
            pkm2_state = haunter2_left
        else:
            win = "Player 2 "



    if keys[pygame.K_RIGHT]:
        pkm1_rect.x += SPEED
        if exp_clef < 8000:
            pkm1_state = gastly1_right
        elif exp_clef >= 8000 and gotcord1 == False:
            pkm1_state = haunter1_right
        else:
            win = "Player 1 "


    if keys[pygame.K_d]:
        pkm2_rect.x += SPEED
        if exp_gen < 8000:
            pkm2_state = gastly2_right
        elif exp_gen >= 8000 and gotcord2 == False:
            pkm2_state = haunter2_right
        else:
            win = "Player 2"

    if (keys[pygame.K_UP]) and not is_jumping1 and on_ground1:
        is_jumping1 = True
        jump_velocity1 = 13


    if (keys[pygame.K_w]) and not is_jumping2 and on_ground2:
        is_jumping2 = True
        jump_velocity2 = 13


    if pkm1_state.get_size() != pkm1_rect.size:
        old_bottom, old_centerx = pkm1_rect.bottom, pkm1_rect.centerx
        pkm1_rect.size = pkm1_state.get_size()
        pkm1_rect.bottom = old_bottom
        pkm1_rect.centerx = old_centerx

    if pkm2_state.get_size() != pkm2_rect.size:
        old_bottom, old_centerx = pkm2_rect.bottom, pkm2_rect.centerx
        pkm2_rect.size = pkm2_state.get_size()
        pkm2_rect.bottom = old_bottom
        pkm2_rect.centerx = old_centerx


    prev_platformrect3_top = platformrect3.top

    platformrect3.y += platformrect3_speed
    if platformrect3.y <= platformrect3_y_min or platformrect3.y >= platformrect3_y_max:
        platformrect3_speed *= -1

    prev1_bottom = pkm1_rect.bottom
    prev2_bottom = pkm2_rect.bottom


    if is_jumping1:
        pkm1_rect.y -= jump_velocity1
        jump_velocity1 -= 0.5 * gravity
        if jump_velocity1 < -13:
           is_jumping1 = False
    else:
        pkm1_rect.y += 5 * gravity


    if is_jumping2:
        pkm2_rect.y -= jump_velocity2
        jump_velocity2 -= 0.5 * gravity
        if jump_velocity2 < -13:
            is_jumping2 = False
    else:
        pkm2_rect.y += 5 * gravity


    on_ground1 = False
    on_ground2 = False


    for plat in platforms:
        plat_prev_top = prev_platformrect3_top if plat is platformrect3 else plat.top
        if pkm1_rect.colliderect(plat):
            falling_onto_top1 = prev1_bottom <= plat_prev_top and pkm1_rect.bottom >= plat.top
            if falling_onto_top1:
                pkm1_rect.bottom = plat.top
                is_jumping1 = False
                jump_velocity1 = 13
                on_ground1 = True
            elif pkm1_rect.top < plat.bottom and prev1_bottom - pkm1_rect.height <= plat.bottom and jump_velocity1 > 0:
                pkm1_rect.top = plat.bottom
                jump_velocity1 = 0
        if pkm2_rect.colliderect(plat):
            falling_onto_top2 = prev2_bottom <= plat_prev_top and pkm2_rect.bottom >= plat.top
            if falling_onto_top2:
                pkm2_rect.bottom = plat.top
                is_jumping2 = False
                jump_velocity2 = 13
                on_ground2 = True
            elif pkm2_rect.top < plat.bottom and prev2_bottom - pkm2_rect.height <= plat.bottom and jump_velocity2 > 0:
                pkm2_rect.top = plat.bottom
                jump_velocity2 = 0
    if pkm2_rect.colliderect(pkm1_rect):


        landing_on_1 = prev2_bottom <= pkm1_rect.top and pkm2_rect.bottom >= pkm1_rect.top
        landing_on_2 = prev1_bottom <= pkm2_rect.top and pkm1_rect.bottom >= pkm2_rect.top


        if landing_on_1:
            pkm2_rect.bottom = pkm1_rect.top
            is_jumping2 = False
            jump_velocity2 = 13
            on_ground2 = True
        elif landing_on_2:
            pkm1_rect.bottom = pkm2_rect.top
            is_jumping1 = False
            jump_velocity1 = 13
            on_ground1 = True
        else:
            overlap_left = pkm1_rect.right - pkm2_rect.left
            overlap_right = pkm2_rect.right - pkm1_rect.left
            if overlap_left < overlap_right:
                push_amount = overlap_left / 2
                pkm1_rect.x -= push_amount
                pkm2_rect.x += push_amount
            else:
                push_amount = overlap_right / 2
                pkm1_rect.x += push_amount
                pkm2_rect.x -= push_amount


    if pkm1_rect.bottom >= GROUND_Y:
        pkm1_rect.bottom = GROUND_Y
        is_jumping1 = False
        jump_velocity1 = 13
        on_ground1 = True


    if pkm2_rect.bottom >= GROUND_Y:
        pkm2_rect.bottom = GROUND_Y
        is_jumping2 = False
        jump_velocity2 = 13
        on_ground2 = True

    if pkm1_rect.left < 0:
        pkm1_rect.left = 0
    if pkm1_rect.right > SCREEN_WIDTH:
        pkm1_rect.right = SCREEN_WIDTH
    if pkm1_rect.top < 0:
        pkm1_rect.top = 0
    if pkm1_rect.bottom > SCREEN_HEIGHT:
        pkm1_rect.bottom = SCREEN_HEIGHT


    if pkm2_rect.left < 0:
        pkm2_rect.left = 0
    if pkm2_rect.right > SCREEN_WIDTH:
        pkm2_rect.right = SCREEN_WIDTH
    if pkm2_rect.top < 0:
        pkm2_rect.top = 0
    if pkm2_rect.bottom > SCREEN_HEIGHT:
        pkm2_rect.bottom = SCREEN_HEIGHT


    if pkm1_rect.colliderect(candy_rect):
        if candy_type == expcandyxs:
            exp_clef += 500
        elif candy_type == expcandym:
            exp_clef += 1000
        elif candy_type == expcandyl:
            exp_clef += 1300
        crystal_collected = True
        next_crystal == False
        print("collide")
        if exp_clef >= 8000 and evolved1 == False:
            print("Player 1 evolved!")
            evolve_sound.play()
            evolved1 = True
        else:
            level_up_sound.play()


    if pkm2_rect.colliderect(candy_rect):
        if candy_type == expcandyxs:
            exp_gen += 500
        elif candy_type == expcandym:
            exp_gen += 1000
        elif candy_type == expcandyl:
            exp_gen += 1300
        crystal_collected = True
        next_crystal == False
        print("collide")
        if exp_gen >= 8000 and evolved2 == False:
            print("Player 2 evolved!")
            evolve_sound.play()
            evolved2 = True
        else:
            level_up_sound.play()


    if pkm1_rect.colliderect(moonstone_rect):
        if exp_clef >= 17000:
            count_two += 1
            gotcord1 = True
            print("stone")
            print("Player 1 evolved!")
            pygame.mixer.music.load(tracks["win"])
            pygame.mixer.music.play(1)
            if count_two > 55:
                gameover = True
            elif count_two > 50:
                pkm1_state = gengar1_left
            elif count_two > 45:
                pkm1_state = haunter1_left
            elif count_two > 40:
                pkm1_state = gengar1_left
            elif count_two > 35:
                pkm1_state = haunter1_right
            elif count_two > 30:
                pkm1_state = gengar1_left
            elif count_two > 15:
                pkm1_state = gengar1_left
            elif count_two > 10:
                pkm1_state = haunter1_left
            elif count_two > 15:
                pkm1_state = gengar1_left
            elif count_two > 10:
                pkm1_state = haunter1_right
            elif count_two > 5:
                pkm1_state = gengar1_left
                win = "Player 2"


    if pkm2_rect.colliderect(linkincord):
        if exp_gen >= 17000:
            gotcord2 = True
            print("cord")
            pygame.mixer.music.load(tracks["win"])
            pygame.mixer.music.play(1)
            print("Player 2 evolved!")
            gengar_state = True

    if gengar_state:
        count += 1
        if count > 55:
            gameover = True
        elif count > 50:
            pkm2_state = gengar2_left
        elif count > 45:
            pkm2_state = haunter2_left
        elif count > 40:
            pkm2_state = gengar2_left
        elif count > 35:
            pkm2_state = haunter2_right
        elif count > 30:
            pkm2_state = gengar2_left
        elif count > 25:
            pkm2_state = gengar2_left
        elif count > 20:
            pkm2_state = haunter2_left
        elif count > 25:
            pkm2_state = gengar2_left
        elif count > 20:
            pkm2_state = haunter2_right
        elif count > 5:
            pkm2_state = gengar2_left
            win = "Player 1"

    screen.blit(background, (0, 0))
    screen.blit(platform1, platformrect)
    screen.blit(platform1, platformrect2)
    screen.blit(platform2, platformrect3)
    screen.blit(platform3, platformrect4)
    screen.blit(pkm1_state, pkm1_rect)


    is_floating2 = pkm2_state in (gastly2_left, gastly2_right, haunter2_left, haunter2_right)
    if is_floating2:
        bob = math.sin(pygame.time.get_ticks() / 1000 * FLOAT_BOB_SPEED) * FLOAT_BOB_RANGE
        pkm2_draw_rect = pkm2_rect.copy()
        pkm2_draw_rect.y -= FLOAT_HEIGHT + bob
        screen.blit(pkm2_state, pkm2_draw_rect)
    else:
        screen.blit(pkm2_state, pkm2_rect)


    if next_crystal == True:
        if candy_type == expcandyxs:
            screen.blit(sparkly, (candy_rect.x - 4, candy_rect.y - 2))
        elif candy_type == expcandym:
                screen.blit(sparkly, (candy_rect.x - 9, candy_rect.y - 9))
        elif candy_type == expcandyl:
                screen.blit(sparkly, (candy_rect.x - 9, candy_rect.y - 8))
        screen.blit(candy_type, candy_rect)
    if crystal_collected == True:
        candy_type, candy_rect = spawn_candy()[0], spawn_candy()[1]
        next_crystal = True
        crystal_collected = False
    screen.blit(deco, (-25, -20))
    if exp_clef >= 17000:
        screen.blit(sparkly, (moonstone_rect.x - 8, moonstone_rect.y - 8))
        screen.blit(moonstone, moonstone_rect)

    if exp_gen >= 17000:
        screen.blit(sparkly, (linkincord.x - 2, linkincord.y - 3))
        screen.blit(linkingcord, linkincord)

    score1 = font.render("Player 1: " + str(exp_gen), True, WHITE)
    screen.blit(score1, (30, 420))
    score2 = font.render("Player 2: " + str(exp_clef), True, WHITE)
    screen.blit(score2, (570, 420))
    pygame.display.flip()
    clock.tick(60)


    if gameover == True:
        waiting_for_restart = True
        while waiting_for_restart:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    waiting_for_restart = False
            pygame.font.Font(None, 150)
            text = font.render(win + " wins!", True, WHITE)
            screen.blit(text, (375 - text.get_width()//2, 250 - text.get_height()//2))
            pygame.mixer.music.load(tracks["win"])
            pygame.mixer.music.play(1)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                waiting_for_restart = False
                running = False


            pygame.display.flip()
            clock.tick(60)



pygame.quit()



