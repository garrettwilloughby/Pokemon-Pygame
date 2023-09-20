import pygame
import os
from sys import exit

pygame.init()
window = pygame.display.set_mode((800,400))
pygame.display.set_caption("Garry's first game")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
height, width = 50, 50
FPS = 60

speed_snor = 2
speed_typh = 5
speed_gen = 5
speed_blast = 3
speed_tryan = 3
speed_sep = 5

hydropump = 7
leafblade = 3
shadowball = 3
hyperbeam = 8
flamethrower = 5
tackle = 1

player1_snorlax = pygame.image.load(os.path.join('characters','p1snor.png'))
snorlax1 = pygame.transform.scale(player1_snorlax, (height, width))
player2_snorlax = pygame.image.load(os.path.join('characters','p2snor.png'))
snorlax2 = pygame.transform.scale(player2_snorlax,(height, width))

player1_blast = pygame.image.load(os.path.join('characters','p1blas.png'))
blast1 = pygame.transform.scale(player1_blast,(height, width))
player2_blast = pygame.image.load(os.path.join('characters','p2blas.png'))
blast2 = pygame.transform.scale(player2_blast,(height, width))

player1_sep = pygame.image.load(os.path.join('characters','p1sep.png'))
sep1 = pygame.transform.scale(player1_sep,(height, width))
player2_sep = pygame.image.load(os.path.join('characters','p2sep.png'))
sep2 = pygame.transform.scale(player2_sep,(height, width))

player1_typh = pygame.image.load(os.path.join('characters','p1ty.png'))
typh1 = pygame.transform.scale(player1_typh,(height, width))
player2_typh = pygame.image.load(os.path.join('characters','p2ty.png'))
typh2 = pygame.transform.scale(player2_typh,(height, width))

player1_lat = pygame.image.load(os.path.join('characters','p1lat.png'))
lat1 = pygame.transform.scale(player1_lat,(height, width))
player2_lat = pygame.image.load(os.path.join('characters','p2lat.png'))
lat2 = pygame.transform.scale(player2_lat,(height, width))

player1_gen = pygame.image.load(os.path.join('characters','p1gen.png'))
gen1 = pygame.transform.scale(player1_gen,(height, width))
player2_gen = pygame.image.load(os.path.join('characters','p2gen.png'))
gen2 = pygame.transform.scale(player2_gen, (height, width))

player1_tyran = pygame.image.load(os.path.join('characters','p1tyran.png'))
tyran1 = pygame.transform.scale(player1_tyran,(height, width))
player2_tyran = pygame.image.load(os.path.join('characters','p2tyran.png'))
tyran2 = pygame.transform.scale(player2_tyran,(height, width))

def draw_window(player1, player2, player1_bullets, player2_bullets):
    window.fill(WHITE)
    window.blit(snorlax1, (player1.x, player1.y))
    window.blit(typh2, (player2.x, player2.y))
    
    # Draw player1 bullets
    for bullet in player1_bullets:
        pygame.draw.rect(window, BLACK, bullet)
    
    # Draw player2 bullets
    for bullet in player2_bullets:
        pygame.draw.rect(window, BLACK, bullet)

    pygame.display.update()

def player1_movement(keys_pressed, player1):
    if keys_pressed[pygame.K_a] and player1.x - 1 > 0: #left
        player1.x -= 2
    if keys_pressed[pygame.K_w] and player1.y - 1 > 0: #up
        player1.y -= 2
    if keys_pressed[pygame.K_s] and player1.y + 1 < 350: #down
        player1.y += 2
    if keys_pressed[pygame.K_d] and player1.x + 1 < 750: #right
        player1.x += 2

def player2_movement(keys_pressed, player2):
    if keys_pressed[pygame.K_LEFT] and player2.x - 1 > 0: #left
        player2.x -= 5
    if keys_pressed[pygame.K_UP] and player2.y - 1 > 0: #up
        player2.y -= 5
    if keys_pressed[pygame.K_DOWN] and player2.y + 1 < 350: #down
        player2.y += 5
    if keys_pressed[pygame.K_RIGHT] and player2.x + 1 < 750: #right
        player2.x += 5

def move_bullets(bullets, bullet_speed, opposing_player):
    for bullet in bullets:
        bullet.x += bullet_speed  # Update bullet position

        # Check if bullet hits the window boundaries
        if bullet.x > 800:
            bullets.remove(bullet)

        # Check for collision with the opposing player
        if bullet.colliderect(opposing_player):
            # Handle collision (e.g., decrease opposing player's health)
            bullets.remove(bullet)

        # Draw the bullet on the window
        pygame.draw.rect(window, BLACK, bullet)

def main():
    player1 = pygame.Rect(100, 300, height, width)
    player2 = pygame.Rect(100, 300, height, width)
    clock = pygame.time.Clock()

    player1_bullets = []
    player2_bullets = []

    bullet_speed = 5

    while True:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    # Create a new bullet for player1
                    bullet = pygame.Rect(
                        player1.x + width, player1.y + player1.height / 2 - 2, 10, 5
                    )
                    player1_bullets.append(bullet)

                if event.key == pygame.K_SPACE:
                    # Create a new bullet for player2
                    bullet = pygame.Rect(
                        player2.x, player2.y + player2.height / 2 - 2, 10, 5
                    )
                    player2_bullets.append(bullet)

        keys_pressed = pygame.key.get_pressed()
        player1_movement(keys_pressed, player1)
        player2_movement(keys_pressed, player2)

        # Move and handle collisions for player1 bullets
        move_bullets(player1_bullets, bullet_speed, player2)

        # Move and handle collisions for player2 bullets
        move_bullets(player2_bullets, -bullet_speed, player1)

        draw_window(player1, player2, player1_bullets, player2_bullets)

if __name__ == "__main__":
    main()
