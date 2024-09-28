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
BALL_SPEED_X = 5
BALL_SPEED_Y = 5

# Font
font = pygame.font.Font(None, 36)

# Game objects
player = pygame.Rect(50, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
opponent = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH//2 - BALL_SIZE//2, HEIGHT//2 - BALL_SIZE//2, BALL_SIZE, BALL_SIZE)

def reset_ball():
    ball.center = (WIDTH//2, HEIGHT//2)
    return BALL_SPEED_X * random.choice((1, -1)), BALL_SPEED_Y * random.choice((1, -1))

def move_paddle(paddle, up, down):
    if up and paddle.top > 0:
        paddle.y -= PADDLE_SPEED
    if down and paddle.bottom < HEIGHT:
        paddle.y += PADDLE_SPEED

def move_ai_paddle(paddle, ball):
    if paddle.centery < ball.centery and paddle.bottom < HEIGHT:
        paddle.y += PADDLE_SPEED
    elif paddle.centery > ball.centery and paddle.top > 0:
        paddle.y -= PADDLE_SPEED

def check_ball_collision(ball, player, opponent, ball_dx, ball_dy):
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_dy *= -1
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_dx *= -1
    return ball_dx, ball_dy

def update_score(ball, player_score, opponent_score):
    if ball.left <= 0:
        opponent_score += 1
        return opponent_score, player_score, True
    elif ball.right >= WIDTH:
        player_score += 1
        return player_score, opponent_score, True
    return player_score, opponent_score, False

def draw_objects(screen, player, opponent, ball):
    pygame.draw.rect(screen, WHITE, player)
    pygame.draw.rect(screen, WHITE, opponent)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT))

def draw_score(screen, player_score, opponent_score):
    player_text = font.render(str(player_score), True, WHITE)
    opponent_text = font.render(str(opponent_score), True, WHITE)
    screen.blit(player_text, (WIDTH//4, 20))
    screen.blit(opponent_text, (3*WIDTH//4, 20))

def draw_game_over(screen, winner):
    game_over_text = font.render(f"Game Over! {winner} wins!", True, WHITE)
    restart_text = font.render("Press SPACE to restart", True, WHITE)
    screen.blit(game_over_text, (WIDTH//2 - game_over_text.get_width()//2, HEIGHT//2 - 50))
    screen.blit(restart_text, (WIDTH//2 - restart_text.get_width()//2, HEIGHT//2 + 50))

def main():
    clock = pygame.time.Clock()
    player_score, opponent_score = 0, 0
    ball_dx, ball_dy = reset_ball()
    game_over = False
    speed_increase = 1.0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and game_over:
                player_score, opponent_score = 0, 0
                ball_dx, ball_dy = reset_ball()
                game_over = False
                speed_increase = 1.0

        if not game_over:
            keys = pygame.key.get_pressed()
            move_paddle(player, keys[pygame.K_UP], keys[pygame.K_DOWN])
            move_ai_paddle(opponent, ball)

            ball.x += ball_dx * speed_increase
            ball.y += ball_dy * speed_increase

            ball_dx, ball_dy = check_ball_collision(ball, player, opponent, ball_dx, ball_dy)

            player_score, opponent_score, scored = update_score(ball, player_score, opponent_score)
            if scored:
                ball_dx, ball_dy = reset_ball()
                speed_increase += 0.05

            if player_score >= 10 or opponent_score >= 10:
                game_over = True

        screen.fill(BLACK)
        draw_objects(screen, player, opponent, ball)
        draw_score(screen, player_score, opponent_score)

        if game_over:
            winner = "Player" if player_score >= 10 else "Opponent"
            draw_game_over(screen, winner)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
