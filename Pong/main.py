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

# Colors (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Functions

def draw_window(paddle1, paddle2):
    WIN.fill(BLACK)
    pygame.draw.rect(WIN, WHITE, BORDER)
    pygame.draw.rect(WIN, WHITE, paddle1)
    pygame.draw.rect(WIN, WHITE, paddle2)
    pygame.display.update()

def paddle1_handle_movement(keys_pressed, paddle1):
    if keys_pressed[pygame.K_w]:
        paddle1.y -= PADDLE_VEL
    if keys_pressed[pygame.K_s]:
        paddle1.y += PADDLE_VEL

def paddle2_handle_movement(keys_pressed, paddle2):
    if keys_pressed[pygame.K_UP]:
        paddle2.y -= PADDLE_VEL
    if keys_pressed[pygame.K_DOWN]:
        paddle2.y += PADDLE_VEL

def main():
    paddle1 = pygame.Rect(100, 226, PADDLE_WIDTH, PADDLE_HEIGHT)
    paddle2 = pygame.Rect(800, 226, PADDLE_WIDTH, PADDLE_HEIGHT)

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

        draw_window(paddle1, paddle2)

    pygame.quit()

if __name__ == '__main__':
    main()