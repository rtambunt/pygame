import pygame
import random

pygame.font.init()

# Window
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('PONG')

BORDER = pygame.Rect(WIDTH // 2 - 2, 0, 4, HEIGHT)
FPS = 60

MAX_SCORE = 11
score_play1 = 0
score_play2 = 0

# Paddle 
PADDLE_WIDTH, PADDLE_HEIGHT = 5, 50
PADDLE_VEL = 5

# Ball 
BALL_WIDTH, BALL_HEIGHT = 7, 7
ball_vel_x = 4 * random.choice((1, -1))
ball_vel_y = 4 * random.choice((1, -1))

# Colors (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonts
SCORE_FONT = pygame.font.SysFont('Calibri', 40)
WINNER_FONT = pygame.font.SysFont('Calibri', 100)

# Functions
def draw_window(paddle1, paddle2, ball, score_play1, score_play2):
    WIN.fill(BLACK)
    pygame.draw.rect(WIN, WHITE, BORDER)

    score_play1_text = SCORE_FONT.render(str(score_play1), 1, WHITE)
    score_play2_text = SCORE_FONT.render(str(score_play2), 1, WHITE)
    WIN.blit(score_play1_text, (WIDTH // 4 , 10))
    WIN.blit(score_play2_text, (WIDTH - WIDTH // 4 - score_play2_text.get_width(), 10))

    pygame.draw.rect(WIN, WHITE, paddle1)
    pygame.draw.rect(WIN, WHITE, paddle2)
    pygame.draw.rect(WIN, WHITE, ball)
    pygame.display.update()

def paddle1_handle_movement(keys_pressed, paddle1):
    if keys_pressed[pygame.K_w] and paddle1.y > 0:
        paddle1.y -= PADDLE_VEL
    if keys_pressed[pygame.K_s] and paddle1.y + PADDLE_HEIGHT < HEIGHT:
        paddle1.y += PADDLE_VEL

def paddle2_handle_movement(keys_pressed, paddle2):
    if keys_pressed[pygame.K_UP] and paddle2.y > 0:
        paddle2.y -= PADDLE_VEL
    if keys_pressed[pygame.K_DOWN] and paddle2.y + PADDLE_HEIGHT < HEIGHT:
        paddle2.y += PADDLE_VEL

def ball_handle_movement(paddle1, paddle2, ball):
    global ball_vel_x, ball_vel_y, score_play1, score_play2

    ball.x += ball_vel_x
    ball.y += ball_vel_y

    if ball.colliderect(paddle1) and ball_vel_x < 0:
        if abs(ball.left - paddle1.right) <= 10:
            ball_vel_x *= -1
        elif abs(ball.top - paddle1.bottom) <= 10:
            ball_vel_y *= -1
        elif abs(ball.bottom - paddle1.top) <= 10:
            ball_vel_y *= -1
            
    if ball.colliderect(paddle2) and ball_vel_x > 0:
        if abs(ball.right - paddle2.left) <= 10:
            ball_vel_x *= -1
        elif abs(ball.bottom - paddle2.top) <= 10:
            ball_vel_y *= -1
        elif abs(ball.top - paddle2.bottom) <= 10:
            ball_vel_y *= -1

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_vel_y *= -1

    if ball.right <= 0:
        score_play2 += 1
        ball_restart(ball)
    
    if ball.left >= WIDTH:
        score_play1 += 1
        ball_restart(ball)

def ball_restart(ball):
    global ball_vel_x, ball_vel_y

    ball.x, ball.y = WIDTH // 2 - 20, HEIGHT // 2 - BALL_HEIGHT // 2
    ball_vel_x *= -1
    ball_vel_y *= random.choice((1, -1))

def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH // 2 - draw_text.get_width() // 2, HEIGHT // 2 - draw_text.get_height() // 2))
    pygame.display.update()
    pygame.time.delay(5000)

def main():
    paddle1 = pygame.Rect(100, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    paddle2 = pygame.Rect(WIDTH - 100, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = pygame.Rect(WIDTH // 2 - 20, HEIGHT // 2 - BALL_HEIGHT // 2, BALL_WIDTH, BALL_HEIGHT)

    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        winner_text = ''
        if score_play1 >= MAX_SCORE:
            winner_text = 'Player 1 Wins!'
        
        if score_play2 >= MAX_SCORE:
            winner_text = 'Player 2 Wins!'

        if winner_text != '':
            draw_winner(winner_text)
            break

        keys_pressed = pygame.key.get_pressed()
        paddle1_handle_movement(keys_pressed, paddle1)
        paddle2_handle_movement(keys_pressed, paddle2)
        ball_handle_movement(paddle1, paddle2, ball)
        draw_window(paddle1, paddle2, ball, score_play1, score_play2)

    pygame.quit()

if __name__ == '__main__':
    main()