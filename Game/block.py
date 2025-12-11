import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("벽돌 깨기 게임")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
BRICK_COLORS = [RED, ORANGE, YELLOW, GREEN, BLUE]

PADDLE_WIDTH = 100
PADDLE_HEIGHT = 20
paddle_x = (SCREEN_WIDTH - PADDLE_WIDTH) // 2
paddle_y = SCREEN_HEIGHT - 40
paddle_speed = 7
paddle = pygame.Rect(paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)


BALL_RADIUS = 10
ball_x = SCREEN_WIDTH // 2
ball_y = SCREEN_HEIGHT // 2
ball_dx = 5 * random.choice([-1, 1])
ball_dy = -5 
ball = pygame.Rect(ball_x - BALL_RADIUS, ball_y - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)


BRICK_ROWS = 5
BRICK_COLS = 10
BRICK_WIDTH = (SCREEN_WIDTH - (BRICK_COLS + 1) * 5) // BRICK_COLS 
BRICK_HEIGHT = 20
BRICK_GAP = 5
bricks = []
for row in range(BRICK_ROWS):
    for col in range(BRICK_COLS):
        brick_x = col * (BRICK_WIDTH + BRICK_GAP) + BRICK_GAP
        brick_y = row * (BRICK_HEIGHT + BRICK_GAP) + 30
        brick = pygame.Rect(brick_x, brick_y, BRICK_WIDTH, BRICK_HEIGHT)
        bricks.append({'rect': brick, 'color': BRICK_COLORS[row % len(BRICK_COLORS)]})

font = pygame.font.Font(None, 36)
game_over = False
game_won = False
score = 0

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and (game_over or game_won):
                paddle_x = (SCREEN_WIDTH - PADDLE_WIDTH) // 2
                paddle = pygame.Rect(paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)
                
                ball_x = SCREEN_WIDTH // 2
                ball_y = SCREEN_HEIGHT // 2
                ball_dx = 5 * random.choice([-1, 1])
                ball_dy = -5
                ball = pygame.Rect(ball_x - BALL_RADIUS, ball_y - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)
                
                bricks = []
                for row in range(BRICK_ROWS):
                    for col in range(BRICK_COLS):
                        brick_x = col * (BRICK_WIDTH + BRICK_GAP) + BRICK_GAP
                        brick_y = row * (BRICK_HEIGHT + BRICK_GAP) + 30
                        brick = pygame.Rect(brick_x, brick_y, BRICK_WIDTH, BRICK_HEIGHT)
                        bricks.append({'rect': brick, 'color': BRICK_COLORS[row % len(BRICK_COLORS)]})
                
                game_over = False
                game_won = False
                score = 0

    if not game_over and not game_won:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle.left > 0:
            paddle.x -= paddle_speed
        if keys[pygame.K_RIGHT] and paddle.right < SCREEN_WIDTH:
            paddle.x += paddle_speed

        ball.x += ball_dx
        ball.y += ball_dy

        if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
            ball_dx *= -1 
        if ball.top <= 0:
            ball_dy *= -1 
        
        if ball.bottom >= SCREEN_HEIGHT:
            game_over = True

        if ball.colliderect(paddle):
            ball_dy *= -1
            
            collision_offset = ball.centerx - paddle.centerx          
            normalized_offset = collision_offset / (PADDLE_WIDTH / 2)           
            ball_dx = normalized_offset * 5 

        remaining_bricks = []
        for brick_data in bricks:
            brick_rect = brick_data['rect']
            if ball.colliderect(brick_rect):
                score += 10 

                
                if ball_dx > 0 and ball.left < brick_rect.right and ball.right > brick_rect.right: 
                    ball_dx *= -1
                elif ball_dx < 0 and ball.right > brick_rect.left and ball.left < brick_rect.left: 
                    ball_dx *= -1
                elif ball_dy > 0 and ball.top < brick_rect.bottom and ball.bottom > brick_rect.bottom: 
                    ball_dy *= -1
                elif ball_dy < 0 and ball.bottom > brick_rect.top and ball.top < brick_rect.top: 
                    ball_dy *= -1
                else:
                    ball_dy *= -1

            else:
                remaining_bricks.append(brick_data)
        bricks = remaining_bricks

        if not bricks:
            game_won = True
            
    screen.fill(BLACK) 

    pygame.draw.rect(screen, BLUE, paddle)

    pygame.draw.circle(screen, WHITE, ball.center, BALL_RADIUS)

    for brick_data in bricks:
        pygame.draw.rect(screen, brick_data['color'], brick_data['rect'])


    score_text = font.render(f"점수: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    if game_over:
        game_over_text = font.render("Game Over! (Tap Space Bar to restart)", True, WHITE)
        text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(game_over_text, text_rect)
    
    if game_won:
        game_win_text = font.render(f"승리! 축하합니다! 최종 점수: {score} (Space Bar로 다시 시작)", True, WHITE)
        text_rect = game_win_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(game_win_text, text_rect)

    pygame.display.flip() 
    clock.tick(60) 

pygame.quit()