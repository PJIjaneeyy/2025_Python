# 4. 💣 유형: 적(똥)이 플레이어를 향해 투사체 발사 (난이도 최상)
import pygame
import random
import sys

pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("적의 반격 (Enemy Shooter)")
clock = pygame.time.Clock()

# 이미지 로드
poop_img = pygame.image.load("poop.png")
poop_img = pygame.transform.scale(poop_img, (40, 40))

# --- 투사체 클래스 정의 ---
class EnemyBullet(pygame.sprite.Sprite):
    """적이 발사하는 투사체"""
    def __init__(self, x, y):
        super().__init__()
        # 이미지 대신 작은 갈색 사각형으로 투사체 표현
        self.image = pygame.Surface((10, 10))
        self.image.fill((100, 50, 0)) # 갈색
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed_y = 5 # 아래로 이동

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > HEIGHT:
            self.kill()

# --- Player (좌우 이동 제한) ---
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("dukbird.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 20 
        self.speed = 7
        self.score = 0
        self.lives = 3
    def update(self):
        keys = pygame.key.get_pressed()
        # [핵심] 좌우(X축) 이동만 허용
        if keys[pygame.K_LEFT]: self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]: self.rect.x += self.speed
        self.rect.clamp_ip(screen.get_rect())

# --- Poop (발사 로직 포함) ---
class Poop(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = poop_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(-50, -10)
        self.speed_y = random.randint(1, 3)
        self.last_shot = pygame.time.get_ticks() # 마지막 발사 시간 기록
        self.shoot_delay = random.randint(1000, 3000) # 1~3초 간격 랜덤 발사 지연 시간

    def update(self):
        self.rect.y += self.speed_y
        
        # 화면 경계 반사 (좌우로도 움직이게 설정)
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.speed_y = -self.speed_y # Y축 반사 대신 X축 반사를 추가해 볼 수도 있음
            
        # 화면 아래로 벗어나면 재배치
        if self.rect.top > HEIGHT:
            self.rect.x = random.randint(0, WIDTH - self.rect.width)
            self.rect.y = random.randint(-50, -10)
            self.speed_y = random.randint(1, 3)

    def shoot(self):
        """작은 똥 투사체를 발사"""
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            bullet = EnemyBullet(self.rect.centerx, self.rect.bottom)
            all_sprites.add(bullet)
            enemy_bullets.add(bullet)

# --- Item (Coin) ---
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 223, 0), (15, 15), 15)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - 30)
        self.rect.y = -self.rect.height
        self.speed_y = random.randint(3, 5)

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > HEIGHT:
            self.kill()

# --- 게임 초기화 ---
all_sprites = pygame.sprite.Group() 
poop_group = pygame.sprite.Group() 
coin_group = pygame.sprite.Group()
enemy_bullets = pygame.sprite.Group() # 새로운 투사체 그룹

player = Player()
all_sprites.add(player)

# 적(똥) 5마리 생성
for _ in range(5):
    p = Poop()
    all_sprites.add(p)
    poop_group.add(p)

# 코인 생성 이벤트
COIN_CREATE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(COIN_CREATE_EVENT, 2000) # 2초마다 코인 생성

def draw_text(surface, text, size, x, y, color):
    font = pygame.font.SysFont(None, size)
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, (x, y))

# --- 메인 루프 ---
running = True
game_over = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == COIN_CREATE_EVENT and not game_over:
            coin = Coin()
            all_sprites.add(coin)
            coin_group.add(coin)

    if not game_over:
        all_sprites.update()
        
        # 1. 똥 발사 로직 실행
        for poop in poop_group:
            poop.shoot() 
        
        # 2. 플레이어와 코인 충돌 (획득)
        coin_hits = pygame.sprite.spritecollide(player, coin_group, True)
        for _ in coin_hits:
            player.score += 10 
        
        # 3. 플레이어와 적 투사체 충돌 (피격)
        bullet_hits = pygame.sprite.spritecollide(player, enemy_bullets, True)
        if bullet_hits:
            player.lives -= 1 # 생명 감소
            # print("적 투사체 피격!")
            
        # 4. 플레이어와 적(똥 본체) 충돌 (즉사)
        poop_body_hits = pygame.sprite.spritecollide(player, poop_group, False)
        if poop_body_hits or player.lives <= 0:
            game_over = True
    
    # --- 그리기 ---
    screen.fill((170, 200, 255))
    all_sprites.draw(screen) 
    
    # 점수/생명 표시
    draw_text(screen, f"Score: {player.score} | Lives: {player.lives}", 24, 10, 10, (0, 0, 0))
    if game_over:
        draw_text(screen, "GAME OVER", 50, WIDTH // 2 - 120, HEIGHT // 2, (255, 0, 0))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()