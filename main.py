import pygame
import random
from pygame import mixer

pygame.init()

screen_size = [360, 600]
screen = pygame.display.set_mode(screen_size)
pygame.font.init()

mixer.music.load("Off Limits.wav")
mixer.music.play(-1)


background = pygame.image.load('background.png')
user = pygame.image.load('user.png')
chicken = pygame.image.load('chicken.png')


def display_score(score):
    font = pygame.font.SysFont('Comic Sans MS', 40, bool)
    score_text = 'Score:' + str(score)
    text_img = font.render(score_text, True, (0, 255, 0))
    screen.blit(text_img, [20, 10])

def display_lives(lives):
    font = pygame.font.SysFont('Comic Sans MS', 40, bool)
    score_text = 'Lives:' + str(lives)
    text_img = font.render(score_text, True, (0, 255, 0))
    screen.blit(text_img, [20, 50])

def Game_Over(lives):
    font = pygame.font.SysFont('Comic Sans MS', 50, bool)
    score_text = 'Game Over'
    text_img = font.render(score_text, True, (0, 255, 0))
    if lives == 0:
        screen.blit(text_img, [30, 200])

def random_offset():
    return -1 * random.randint(100, 1500)


ch_y = [random_offset(), random_offset(), random_offset()]
user_X = 150

score = 0
lives = 5

def crashed(idx):
    global score
    score += 10
    print('+10')
    ch_y[idx] = random_offset()


def update_chicken_pos(idx):
    global lives
    if ch_y[idx] > 610 and score > 0:
        ch_y[idx] = random_offset()
        lives -= 0.5
        print('Lives:',lives)
        gameoverSound = mixer.Sound("game_over.wav")
        gameoverSound.play()
    else:
        ch_y[idx] += 5


keep_alive = True
clock = pygame.time.Clock()
while keep_alive:
    if lives == -0.5:
        print('Score:', score)
        break
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_alive = False
    pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and user_X < 280:
        user_X += 6
    elif keys[pygame.K_LEFT] and user_X > 0:
        user_X -= 6

    update_chicken_pos(0)
    update_chicken_pos(1)
    update_chicken_pos(2)

    screen.blit(background, [0, 0])
    screen.blit(user, [user_X, 520])
    screen.blit(chicken, [0, ch_y[0]])
    screen.blit(chicken, [150, ch_y[1]])
    screen.blit(chicken, [280, ch_y[2]])

    if ch_y[0] > 500 and user_X < 70:
        crashed(0)
    if ch_y[1] > 500 and 80 < user_X < 200:
        crashed(1)
    if ch_y[2] > 500 and user_X > 220:
        crashed(2)

    display_score(score)
    display_lives(lives)
    Game_Over(lives)

    pygame.display.update()
    clock.tick(60)
