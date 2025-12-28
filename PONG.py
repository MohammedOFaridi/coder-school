import pygame
import sys

# Initialize pygame
pygame.init()

# Setup Game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Setup the clock
clock = pygame.time.Clock()

# Ball properties
ball_x = SCREEN_WIDTH // 2
ball_y = SCREEN_HEIGHT // 2
ball_radius = 10
ball_x_vel = 5
ball_y_vel = 4

# Paddle properties
paddle_width = 15
paddle_height = 100
paddle_speed = 8

# Left paddle (Player 1)
left_paddle_x = 50
left_paddle_y = SCREEN_HEIGHT // 2 - paddle_height // 2

# Right paddle (Player 2)
right_paddle_x = SCREEN_WIDTH - 50 - paddle_width
right_paddle_y = SCREEN_HEIGHT // 2 - paddle_height // 2

# Score
left_score = 0
right_score = 0
font = pygame.font.Font(None, 74)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get pressed keys
    keys = pygame.key.get_pressed()

    # Move left paddle
    if keys[pygame.K_w] and left_paddle_y > 0:
        left_paddle_y -= paddle_speed
    if keys[pygame.K_s] and left_paddle_y < SCREEN_HEIGHT - paddle_height:
        left_paddle_y += paddle_speed

    # Move right paddle
    if keys[pygame.K_UP] and right_paddle_y > 0:
        right_paddle_y -= paddle_speed
    if keys[pygame.K_DOWN] and right_paddle_y < SCREEN_HEIGHT - paddle_height:
        right_paddle_y += paddle_speed

    # Move the ball
    ball_x += ball_x_vel
    ball_y += ball_y_vel

    # Ball collision with top and bottom walls
    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= SCREEN_HEIGHT:
        ball_y_vel = -ball_y_vel

    # Ball collision with left paddle
    if (ball_x - ball_radius <= left_paddle_x + paddle_width and
        left_paddle_y <= ball_y <= left_paddle_y + paddle_height and
        ball_x_vel < 0):
        ball_x_vel *= -1

    # Ball collision with right paddle
    if (ball_x + ball_radius >= right_paddle_x and
        right_paddle_y <= ball_y <= right_paddle_y + paddle_height and
        ball_x_vel > 0):
        ball_x_vel *= -1

    # Check if ball goes off the screen (scoring)
    if ball_x < 0:
        right_score += 1
        ball_x = SCREEN_WIDTH // 2
        ball_y = SCREEN_HEIGHT // 2
        ball_x_vel = 5
        ball_y_vel = 4

    if ball_x > SCREEN_WIDTH:
        left_score += 1
        ball_x = SCREEN_WIDTH // 2
        ball_y = SCREEN_HEIGHT // 2
        ball_x_vel = -5
        ball_y_vel = 4

    # Fill the screen with black
    screen.fill(BLACK)

    # Draw the middle line
    pygame.draw.line(screen, WHITE, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT), 5)

    # Draw paddles
    pygame.draw.rect(screen, RED, (left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, GREEN, (right_paddle_x, right_paddle_y, paddle_width, paddle_height))

    # Draw ball
    pygame.draw.circle(screen, WHITE, (int(ball_x), int(ball_y)), ball_radius)

    # Draw scores
    left_text = font.render(str(left_score), True, WHITE)
    right_text = font.render(str(right_score), True, WHITE)
    screen.blit(left_text, (SCREEN_WIDTH // 4, 50))
    screen.blit(right_text, (3 * SCREEN_WIDTH // 4, 50))

    # Update display
    pygame.display.flip()
    clock.tick(60)