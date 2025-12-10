# 3-1. 덕새 총 쏘기 (총알 발사 기능)
import pygame
import random
import sys

pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3-1. 덕새 총 쏘기")
clock = pygame.time.Clock()
WHITE = (255, 255, 255)

# --- Bullet 클래스 (우주선 게임 참고) ---
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 15))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed_y = -7 # 위로 이동
    def update(self):
        self.rect.y += self.speed_y
        if self.rect.bottom < 0:
            self.kill() # 화면 밖으로 나가면 제거

class Player(pygame.sprite.Sprite): 
    # ... (생성자 및 update 메서드 중략, 2-1과 동일) ...
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("dukbird.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 30) # 아래쪽에 배치
        self.speed = 5
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]: self.rect.x += self.speed
        if keys[pygame.K_UP]: self.rect.y -= self.speed
        if keys[pygame.K_DOWN]: self.rect.y += self.speed
        self.rect.clamp_ip(screen.get_rect())

    def shoot(self): # [추가] Player의 총알 발사 메서드
        bullet = Bullet(self.rect.centerx, self.rect.top) # 총알 생성
        all_sprites.add(bullet)
        bullets.add(bullet) # 총알 그룹에도 추가 (충돌 검사용)


# 똥은 잠시 제외하고 Player와 Bullet만 테스트
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group() # [추가] 총알 그룹

player = Player()
all_sprites.add(player)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: # 스페이스바 입력 시
                player.shoot() # [추가] 총알 발사
    
    all_sprites.update()
    screen.fill((0, 0, 0)) # 배경 검은색으로 (우주 테마)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit(); sys.exit()