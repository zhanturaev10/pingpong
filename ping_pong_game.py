import pygame
import sys
import random

# Constants for screen dimensions and colors
SCREEN_WIDTH, SCREEN_HEIGHT = 1530, 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Ball properties
BALL_RADIUS = 20
ball_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
ball_velocity = [5, 5]

# Paddle properties
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
player_paddle_pos = [0, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2]
opponent_paddle_pos = [SCREEN_WIDTH - PADDLE_WIDTH, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2]
PADDLE_SPEED = 10

# Initialize pygame
pygame.init()

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ping Pong Game")

# Load ball and paddle images
BALL_IMAGE_PATH = 'ball.png'
PADDLE_IMAGE_PATH = 'paddle1.png'
ball_image = pygame.image.load(BALL_IMAGE_PATH)
paddle_image = pygame.image.load(PADDLE_IMAGE_PATH)
ball_image = pygame.transform.scale(ball_image, (BALL_RADIUS * 2, BALL_RADIUS * 2))
paddle_image = pygame.transform.scale(paddle_image, (PADDLE_WIDTH, PADDLE_HEIGHT))

# Fonts
font = pygame.font.Font(None, 60)

clock = pygame.time.Clock()

player_score = 0
opponent_score = 0


# Function to change the resolution
def change_resolution(width, height):
    global SCREEN_WIDTH, SCREEN_HEIGHT, screen
    SCREEN_WIDTH, SCREEN_HEIGHT = width, height
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move player paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_paddle_pos[1] > 0:
        player_paddle_pos[1] -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and player_paddle_pos[1] < SCREEN_HEIGHT - PADDLE_HEIGHT:
        player_paddle_pos[1] += PADDLE_SPEED

    # Move opponent paddle
    opponent_paddle_pos[1] = ball_pos[1] - PADDLE_HEIGHT // 2

    # Update ball position
    ball_pos[0] += ball_velocity[0]
    ball_pos[1] += ball_velocity[1]

    # Ball collision with top and bottom walls
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= SCREEN_HEIGHT - BALL_RADIUS:
        ball_velocity[1] = -ball_velocity[1]

    # Ball collision with paddles
    if (player_paddle_pos[0] + PADDLE_WIDTH >= ball_pos[0] - BALL_RADIUS >= player_paddle_pos[0]
            and player_paddle_pos[1] + PADDLE_HEIGHT >= ball_pos[1] >= player_paddle_pos[1]):
        ball_velocity[0] = -ball_velocity[0]
    if (opponent_paddle_pos[0] <= ball_pos[0] + BALL_RADIUS <= opponent_paddle_pos[0] + PADDLE_WIDTH
            and opponent_paddle_pos[1] <= ball_pos[1] <= opponent_paddle_pos[1] + PADDLE_HEIGHT):
        ball_velocity[0] = -ball_velocity[0]

    # Ball out of bounds
    if ball_pos[0] <= BALL_RADIUS:
        opponent_score += 1
        ball_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
        ball_velocity = [random.choice([-5, 5]), random.choice([-5, 5])]

    if ball_pos[0] >= SCREEN_WIDTH - BALL_RADIUS:
        player_score += 1
        ball_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
        ball_velocity = [random.choice([-5, 5]), random.choice([-5, 5])]

    # Clear the screen
    screen.fill(WHITE)

    # Draw ball
    screen.blit(ball_image, (int(ball_pos[0] - BALL_RADIUS), int(ball_pos[1] - BALL_RADIUS)))

    # Draw paddles
    screen.blit(paddle_image, (int(player_paddle_pos[0]), int(player_paddle_pos[1])))
    screen.blit(paddle_image, (int(opponent_paddle_pos[0]), int(opponent_paddle_pos[1])))

    # Draw scores
    player_score_text = font.render(str(player_score), True, BLACK)
    opponent_score_text = font.render(str(opponent_score), True, BLACK)
    screen.blit(player_score_text, (SCREEN_WIDTH // 4, 50))
    screen.blit(opponent_score_text, (3 * SCREEN_WIDTH // 4, 50))

    # Update the display
    pygame.display.update()

    # Cap the frame rate
    clock.tick(60)
