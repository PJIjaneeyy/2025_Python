# 1-1. 랜덤 움직이는 똥 피하기
import pygame
import random
import sys

pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("1-1. 랜덤 움직이는 똥 피하기")
clock = pygame.time.Clock()
poop_img = pygame.image.load("poop.png")
poop_img = pygame.transform.scale(poop_img, (40, 40))

class Player(pygame.sprite.Sprite): # py_game09.py의 Player 클래스
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

class Poop(pygame.sprite.Sprite): # 우주선 게임의 Alien 역할
    def __init__(self):
        super().__init__()
        self.image = poop_img
        self.rect = self.image.get_rect()
        self.rect.topleft = (random.randint(0, WIDTH - 40), random.randint(0, HEIGHT - 40))
        # [추가] 랜덤한 속도 설정 (우주선 게임 Alien 참고)
        self.speed_x = random.choice([-1, 1]) * random.randint(2, 4)
        self.speed_y = random.choice([-1, 1]) * random.randint(2, 4)

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        # 경계에 닿으면 방향 반전 (랜덤 움직임)
        if self.rect.left < 0 or self.rect.right > WIDTH: self.speed_x *= -1
        if self.rect.top < 0 or self.rect.bottom > HEIGHT: self.speed_y *= -1

all_sprites = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

enemy = Poop() # 똥 1개 생성
all_sprites.add(enemy)
enemy_group.add(enemy)

# [추가 기능 없음: 충돌 없음]
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
    
    all_sprites.update()
    screen.fill((170, 200, 255))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit(); sys.exit()