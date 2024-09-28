import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paddle settings
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 90
PADDLE_SPEED = 5

# Ball settings
BALL_SIZE = 15
BALL_SPEED_X = 7
BALL_SPEED_Y = 7

# Create game objects
player = pygame.Rect(50, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
opponent = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH//2 - BALL_SIZE//2, HEIGHT//2 - BALL_SIZE//2, BALL_SIZE, BALL_SIZE)

# Set up ball movement
ball_dx, ball_dy = BALL_SPEED_X * random.choice((1, -1)), BALL_SPEED_Y * random.choice((1, -1))

# Set up score
player_score, opponent_score = 0, 0
font = pygame.font.Font(None, 36)

# Game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the player's paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player.top > 0:
        player.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and player.bottom < HEIGHT:
        player.y += PADDLE_SPEED

    # Move the opponent's paddle (simple AI)
    if opponent.centery < ball.centery and opponent.bottom < HEIGHT:
        opponent.y += PADDLE_SPEED
    elif opponent.centery > ball.centery and opponent.top > 0:
        opponent.y -= PADDLE_SPEED

    # Move the ball
    ball.x += ball_dx
    ball.y += ball_dy

    # Ball collision with top and bottom walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_dy *= -1

    # Ball collision with paddles
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_dx *= -1

    # Score points
    if ball.left <= 0:
        opponent_score += 1
        ball.center = (WIDTH//2, HEIGHT//2)
        ball_dx *= random.choice((1, -1))
        ball_dy *= random.choice((1, -1))
    elif ball.right >= WIDTH:
        player_score += 1
        ball.center = (WIDTH//2, HEIGHT//2)
        ball_dx *= random.choice((1, -1))
        ball_dy *= random.choice((1, -1))

    # Clear the screen
    screen.fill(BLACK)

    # Draw game objects
    pygame.draw.rect(screen, WHITE, player)
    pygame.draw.rect(screen, WHITE, opponent)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT))

    # Display scores
    player_text = font.render(str(player_score), True, WHITE)
    opponent_text = font.render(str(opponent_score), True, WHITE)
    screen.blit(player_text, (WIDTH//4, 20))
    screen.blit(opponent_text, (3*WIDTH//4, 20))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
