# 2-1. 똥 피하기 & 점수 획득 (충돌 및 변수 변경)
import pygame
import random
import sys

pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2-1. 똥 피하기 (충돌)")
clock = pygame.time.Clock()
poop_img = pygame.image.load("poop.png")
poop_img = pygame.transform.scale(poop_img, (40, 40))

class Player(pygame.sprite.Sprite): 
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("dukbird.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed = 5
        self.score = 0   # [추가] 점수 변수
        self.lives = 3   # [추가] 생명 변수
    # ... update 메서드는 1-1과 동일 ...
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]: self.rect.x += self.speed
        if keys[pygame.K_UP]: self.rect.y -= self.speed
        if keys[pygame.K_DOWN]: self.rect.y += self.speed
        self.rect.clamp_ip(screen.get_rect())

class Poop(pygame.sprite.Sprite):
    # ... (1-1과 동일) ...
    def __init__(self):
        super().__init__()
        self.image = poop_img
        self.rect = self.image.get_rect()
        self.rect.topleft = (random.randint(0, WIDTH - 40), random.randint(0, HEIGHT - 40))
        self.speed_x = random.choice([-1, 1]) * random.randint(2, 4)
        self.speed_y = random.choice([-1, 1]) * random.randint(2, 4)
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.left < 0 or self.rect.right > WIDTH: self.speed_x *= -1
        if self.rect.top < 0 or self.rect.bottom > HEIGHT: self.speed_y *= -1

all_sprites = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
enemy = Poop()
all_sprites.add(enemy)
enemy_group.add(enemy)

running = True
game_over = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
    
    if not game_over:
        all_sprites.update()
        
        # [추가] 충돌 감지 (Player vs 똥)
        hits = pygame.sprite.spritecollide(player, enemy_group, True) # 똥 제거(True)
        if hits:
            player.lives -= 1 # [추가] 변수 변경: 생명 감소
            # 똥이 제거되었으므로 새 똥 생성
            new_poop = Poop()
            all_sprites.add(new_poop)
            enemy_group.add(new_poop)

        if player.lives <= 0:
            game_over = True

    screen.fill((170, 200, 255))
    all_sprites.draw(screen)
    # 점수/생명 표시 로직 추가 (생략)
    pygame.display.flip()
    clock.tick(60)
pygame.quit(); sys.exit()