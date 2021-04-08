import pygame

# Window
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('PONG')

FPS = 60

# Paddle 
PADDLE_WIDTH, PADDLE_HEIGHT = 5, 50
PADDLE_VEL = 5

# Colors (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Functions

def draw_window(paddle1, paddle2):
    WIN.fill(BLACK)
    pygame.draw.rect(WIN, WHITE, paddle1)
    pygame.draw.rect(WIN, WHITE, paddle2)
    pygame.display.update()

def main():
    paddle1 = pygame.Rect(100, 226, PADDLE_WIDTH, PADDLE_HEIGHT)
    paddle2 = pygame.Rect(800, 226, PADDLE_WIDTH, PADDLE_HEIGHT)

    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = false
        
        draw_window(paddle1, paddle2)
    pygame.quit()

if __name__ == '__main__':
    main()