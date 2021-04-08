import pygame

# Window
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('PONG')

FPS = 60

BORDER = pygame.Rect(WIDTH // 2 - 2, 0, 4, HEIGHT)

# Paddle 
PADDLE_WIDTH, PADDLE_HEIGHT = 5, 50
PADDLE_VEL = 5

# Ball 
BALL_WIDTH, BALL_HEIGHT = 7, 7
ball_vel_x = -5
ball_vel_y = 0

# Colors (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Functions

def draw_window(paddle1, paddle2, ball):
    WIN.fill(BLACK)
    pygame.draw.rect(WIN, WHITE, BORDER)
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
    global ball_vel_x, ball_vel_y

    ball.x += ball_vel_x
    ball.y += ball_vel_y

    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_vel_x *= -1
       
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_vel_y *= -1

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

        keys_pressed = pygame.key.get_pressed()
        paddle1_handle_movement(keys_pressed, paddle1)
        paddle2_handle_movement(keys_pressed, paddle2)
        ball_handle_movement(paddle1, paddle2, ball)
        draw_window(paddle1, paddle2, ball)

    pygame.quit()

if __name__ == '__main__':
    main()