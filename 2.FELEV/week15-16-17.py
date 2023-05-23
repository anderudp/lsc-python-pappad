import pygame
import math
import random
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 500
WINDOW = pygame.display.set_mode(size=(WIDTH, HEIGHT))
pygame.display.set_caption("Space Flight")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

BORDER = pygame.Rect(WIDTH // 2 - 5, 0, 10, HEIGHT)

BULLET_HIT_SOUND = pygame.mixer.Sound("explosion.wav")
BULLET_FIRE_SOUND = pygame.mixer.Sound("laser.wav")

HEALTH_FONT = pygame.font.SysFont('arial', 40)
WINNER_FONT = pygame.font.SysFont('arial', 100)

FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3
SPACESHIP_WIDTH = 80
SPACESHIP_HEIGHT = 60

METEOR_WIDTH = METEOR_HEIGHT = 50

METEOR_VEL = 2
METEOR_1_DIR = random.randrange(0, 360)
METEOR_2_DIR = random.randrange(0, 360)
METEOR_3_DIR = random.randrange(0, 360)

METEOR_1_X_VEL = math.cos(METEOR_1_DIR) * METEOR_VEL
METEOR_1_Y_VEL = math.sin(METEOR_1_DIR) * METEOR_VEL

METEOR_2_X_VEL = math.cos(METEOR_2_DIR) * METEOR_VEL
METEOR_2_Y_VEL = math.sin(METEOR_2_DIR) * METEOR_VEL

METEOR_3_X_VEL = math.cos(METEOR_3_DIR) * METEOR_VEL
METEOR_3_Y_VEL = math.sin(METEOR_3_DIR) * METEOR_VEL

YELLOW_SPACESHIP_IMAGE = pygame.image.load("spaceship_yellow.png")
YELLOW_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90
)

RED_SPACESHIP_IMAGE = pygame.image.load("spaceship_red.png")
RED_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270
)

METEOR_IMAGE = pygame.image.load("meteor.png")
METEOR_1 = pygame.transform.rotate(
    pygame.transform.scale(METEOR_IMAGE, (METEOR_WIDTH, METEOR_HEIGHT)), 90
)
METEOR_2 = pygame.transform.rotate(
    pygame.transform.scale(METEOR_IMAGE, (METEOR_WIDTH, METEOR_HEIGHT)), 210
)
METEOR_3 = pygame.transform.rotate(
    pygame.transform.scale(METEOR_IMAGE, (METEOR_WIDTH, METEOR_HEIGHT)), 330
)

SPACE = pygame.transform.scale(pygame.image.load("space.png"), (WIDTH, HEIGHT))

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2