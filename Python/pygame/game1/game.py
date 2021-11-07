import pygame
import os
 
from pygame import display

pygame.font.init()
pygame.mixer.init()

# init display
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # set display
pygame.display.set_caption("SpaceDefenders")
BORDER = pygame.Rect(WIDTH//2, 0, 10, HEIGHT-5)
SPACE = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'space.jpg')), (WIDTH, HEIGHT))

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0,255,0)

# fonts
HEALTH_FONT = pygame.font.SysFont('comicsans', 20)
WINNER_FONT = pygame.font.SysFont('comicsans', 70)

# Global CONST vars
FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 6
HEALTH_WIDTH = 200
HEALTH_HEIGHT = 20
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

# Sounds
BUTTLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('assets', 'hit.wav'))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('assets', 'fire.wav'))

# Animations
EXPLODE1 = pygame.image.load(os.path.join('assets', '1.png'))
EXPLODE_SCALE_1 = pygame.transform.scale((EXPLODE1), (50,50))
EXPLODE2 = pygame.image.load(os.path.join('assets', '2.png'))
EXPLODE_SCALE_2 = pygame.transform.scale((EXPLODE2), (50, 50))
EXPLODE3 = pygame.image.load(os.path.join('assets', '3.png'))
EXPLODE_SCALE_3= pygame.transform.scale((EXPLODE3), (50,50))
EXPLODE4 = pygame.image.load(os.path.join('assets', '4.png'))
EXPLODE_SCALE_4= pygame.transform.scale((EXPLODE4), (50,50))
EXPLODE5 = pygame.image.load(os.path.join('assets', '5.png'))
EXPLODE_SCALE_5 = pygame.transform.scale((EXPLODE5), (50, 50))
EXPLODE6 = pygame.image.load(os.path.join('assets', '6.png'))
EXPLODE_SCALE_6 = pygame.transform.scale((EXPLODE6), (50, 50))
EXPLODE7 = pygame.image.load(os.path.join('assets', '7.png'))
EXPLODE_SCALE_7 = pygame.transform.scale((EXPLODE7), (50, 50))

annimate_list = [EXPLODE_SCALE_1, EXPLODE_SCALE_2, EXPLODE_SCALE_3,EXPLODE_SCALE_4, EXPLODE_SCALE_5, EXPLODE_SCALE_6, EXPLODE_SCALE_7]

# HITS
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2


# yellow spaceship data
Y_SPACESHIP_X, Y_SPACESHIP_Y = 150, 100
YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

# red spaceship data
R_SPACESHIP_X, R_SPACESHIP_Y = 700, 100
RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)


def draw_health(red_health, yellow_health, red_health_text, yellow_health_text):
    YELLOW_HEALTH_BAR = pygame.Rect(yellow_health_text.get_width() + 10, 10, yellow_health, 25)
    RED_HEALTH_BAR = pygame.Rect(WIDTH-110, 10, red_health, 25)
    pygame.draw.rect(WIN, GREEN, YELLOW_HEALTH_BAR)
    pygame.draw.rect(WIN, GREEN, RED_HEALTH_BAR)

def draw_window(yellow, yellow_bullets, yellow_health, red, red_bullets, red_health):
    WIN.blit(SPACE, (0, 0))
    pygame.draw.rect(WIN, BLACK, BORDER)

    # red health
    red_health_text = HEALTH_FONT.render(
        "Health: ", 1, WHITE)
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 110, 10))

    # yellow health
    yellow_health_text = HEALTH_FONT.render(
        "Health: ", 1, WHITE)
    WIN.blit(yellow_health_text, (10, 10))

    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))

    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)

    draw_health(red_health, yellow_health, red_health_text, yellow_health_text)

    pygame.display.update()


def handle_yellow_movement(keys_pressed, yellow):
    # LEFT
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:
        yellow.x -= VEL
    # RIGHT
    if keys_pressed[pygame.K_d] and yellow.x + VEL + (yellow.width - 15) < BORDER.x:
        yellow.x += VEL
    # UP
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:
        yellow.y -= VEL
    # DOWN
    if keys_pressed[pygame.K_s] and yellow.y + VEL + (yellow.height + 15) < HEIGHT:
        yellow.y += VEL


def handle_red_movement(keys_pressed, red):
    # LEFT
    if keys_pressed[pygame.K_LEFT] and red.x - VEL - (red.width - 45) > BORDER.x:
        red.x -= VEL
    # RIGHT
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + (red.width - 15) < WIDTH:
        red.x += VEL
    # UP
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:  
        red.y -= VEL
    # DOWN
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + (red.height + 15) < HEIGHT:
        red.y += VEL


def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)
        for redbull in red_bullets:
            if bullet.colliderect(redbull):
                yellow_bullets.remove(bullet)
                red_bullets.remove(redbull)

                for sprite in annimate_list:
                    WIN.blit(sprite, (bullet.x-30, bullet.y-20))
                    display.update()
                BUTTLET_HIT_SOUND.play()

    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)


def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH//2 - draw_text.get_width() //
             2, HEIGHT//2 - draw_text.get_height()//2))
    pygame.display.update()
    pygame.time.delay(5000)


def main():
    red = pygame.Rect(R_SPACESHIP_X, R_SPACESHIP_Y,
                      SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(Y_SPACESHIP_X, Y_SPACESHIP_Y,
                         SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    yellow_bullets = []
    yellow_bullets.clear()
    red_bullets = []
    red_bullets.clear()

    red_health, yellow_health = 100, 100

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

                if event.key == pygame.K_SLASH and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        red.x, red.y + red.height//2 - 2, 10, 5)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
            

            if event.type == RED_HIT:
                red_health -= 5
                BUTTLET_HIT_SOUND.play()

            if event.type == YELLOW_HIT:
                yellow_health -= 5
                BUTTLET_HIT_SOUND.play()

            winner_text = ''
            if red_health <= 0:
                winner_text = 'Yellow Wins!'
                for sprite in annimate_list:
                    WIN.blit(sprite, (red.x, red.y))

            if yellow_health <= 0:
                winner_text = 'Red Wins!'
                for sprite in annimate_list:
                    WIN.blit(sprite, (yellow.x, yellow.y))

            if winner_text != '':
                draw_winner(winner_text)
                run = False

        # move spaceships
        keys_pressed = pygame.key.get_pressed()
        handle_yellow_movement(keys_pressed, yellow)
        handle_red_movement(keys_pressed, red)

        handle_bullets(yellow_bullets, red_bullets, yellow, red)

        draw_window(yellow, yellow_bullets, yellow_health,
                    red, red_bullets, red_health)

    main()


if __name__ == "__main__":
    main()
