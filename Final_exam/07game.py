# 2-1. 덕새 여러 마리 (객체 여러 개 생성, 랜덤 이동)

import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("덕새 여러 마리 (랜덤 이동)")

clock = pygame.time.Clock()

# --- 스프라이트 클래스 정의 ---

class MovingDuksae(pygame.sprite.Sprite):
    def __init__(self, is_player=False):
        super().__init__()
        self.image = pygame.image.load("dukbird.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - 50)
        self.rect.y = random.randint(0, HEIGHT - 50)
        
        self.is_player = is_player
        self.speed = 3
        
        # 랜덤 이동을 위한 속도 설정
        self.vx = random.choice([-1, 1]) * random.randint(1, 3)
        self.vy = random.choice([-1, 1]) * random.randint(1, 3)

    def update(self):
        # 플레이어(첫 번째 덕새)만 키보드 조작
        if self.is_player:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]: self.rect.x -= self.speed
            if keys[pygame.K_RIGHT]: self.rect.x += self.speed
            if keys[pygame.K_UP]: self.rect.y -= self.speed
            if keys[pygame.K_DOWN]: self.rect.y += self.speed
        
        # 나머지 객체는 랜덤하게 움직임 (좌우/위아래 경계 반사)
        else:
            self.rect.x += self.vx
            self.rect.y += self.vy
            
            if self.rect.left < 0 or self.rect.right > WIDTH:
                self.vx *= -1
            if self.rect.top < 0 or self.rect.bottom > HEIGHT:
                self.vy *= -1

        self.rect.clamp_ip(screen.get_rect())

# --- 게임 초기화 ---

all_sprites = pygame.sprite.Group() 

# 플레이어 덕새 (키보드 조작)
player1 = MovingDuksae(is_player=True)
all_sprites.add(player1)

# 추가 덕새 4마리 생성 (랜덤 이동)
for i in range(4):
    other_duksae = MovingDuksae(is_player=False)
    all_sprites.add(other_duksae)

running = True

# --- 메인 루프 ---

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update() 
    
    # ------------------ 그리기 ------------------
    screen.fill((170, 200, 255))
    all_sprites.draw(screen) 
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()