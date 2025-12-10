# 2-2. 적 객체 여러 개 (좌우 이동)

import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("적 여러 개 (좌우 이동)")

clock = pygame.time.Clock()
poop_img = pygame.image.load("poop.png")
poop_img = pygame.transform.scale(poop_img, (40, 40))

# --- 스프라이트 클래스 정의 ---

class Player(pygame.sprite.Sprite):
    # ... (py_game09와 동일, 상하좌우 이동)
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("dukbird.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed = 5
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]: self.rect.x += self.speed
        if keys[pygame.K_UP]: self.rect.y -= self.speed
        if keys[pygame.K_DOWN]: self.rect.y += self.speed
        self.rect.clamp_ip(screen.get_rect())

class Poop(pygame.sprite.Sprite):
    def __init__(self, y_pos, speed):
        super().__init__()
        self.image = poop_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = y_pos # Y축 위치 고정
        self.speed_x = speed # X축 이동 속도 (랜덤 아님)

    def update(self):
        # X축 이동 (좌우)
        self.rect.x += self.speed_x
        
        # 화면 경계에 닿으면 반사
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.speed_x *= -1
            
# --- 게임 초기화 ---

all_sprites = pygame.sprite.Group() 
poop_group = pygame.sprite.Group() 

player = Player()
all_sprites.add(player)

# 적 여러 개 생성 (각기 다른 줄에 위치)
poop_configs = [
    (50, 2),  # y=50, speed=2
    (150, -3), # y=150, speed=-3
    (250, 4)  # y=250, speed=4
]

for y, s in poop_configs:
    new_poop = Poop(y, s)
    all_sprites.add(new_poop)
    poop_group.add(new_poop)

# --- 메인 루프 ---

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    all_sprites.update() 
    
    # 충돌 처리 (똥 vs 플레이어)
    hits = pygame.sprite.spritecollide(player, poop_group, False) # 똥 제거 안 함
    if hits:
        player.image.fill((255, 0, 0)) # 충돌 시 덕새 색깔 변경 (시각적 변수 변경)
    else:
        player.image = pygame.image.load("dukbird.png") # 충돌 안 할 시 원래 이미지
        player.image = pygame.transform.scale(player.image, (50, 50))
    
    # ------------------ 그리기 ------------------
    screen.fill((170, 200, 255))
    all_sprites.draw(screen) 
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()