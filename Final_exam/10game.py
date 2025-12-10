# 덕새의 우주 모험: 똥 피하고 총 쏘기
import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("덕새의 우주 모험: 똥 피하고 총 쏘기")

clock = pygame.time.Clock()

# --- 색상 및 이미지 로드 ---
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE_SKY = (170, 200, 255)

# 덕새 이미지는 py_game09에서 로드됨
poop_img = pygame.image.load("poop.png")
poop_img = pygame.transform.scale(poop_img, (40, 40))

# --- 사운드 준비 (파일 제공 시 주석 해제) ---
# explosion_sound = pygame.mixer.Sound("explosion.wav") 
# shoot_sound = pygame.mixer.Sound("laser.wav") 


# --- Sprite 클래스 정의 ---

class Player(pygame.sprite.Sprite):
    # py_game09.py 코드 기반
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("dukbird.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 30) # 아래쪽에 배치
        self.speed = 5
        self.score = 0
        self.health = 3
        
    def update(self): # Player의 동작 정의
        keys = pygame.key.get_pressed()
        
        # Player는 상하좌우 모두 이동 가능하도록 설정
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
            
        self.rect.clamp_ip(screen.get_rect()) # 화면 경계 제한

    def shoot(self):
        """총알을 생성하고 그룹에 추가하는 메서드 (우주선 게임 기능)"""
        # 총알은 플레이어의 중앙 상단에서 발사됨
        bullet = Bullet(self.rect.centerx, self.rect.top) 
        all_sprites.add(bullet)
        bullets.add(bullet)
        # shoot_sound.play() # 사운드 재생

class Poop(pygame.sprite.Sprite):
    """적(똥) 클래스: 우주선 게임의 Alien처럼 동작"""
    def __init__(self):
        super().__init__()
        self.image = poop_img
        self.rect = self.image.get_rect()
        
        # 랜덤 위치 (X축)와 화면 상단 밖 (Y축)에서 시작
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(-50, -10)
        
        # 랜덤 속도로 아래로 이동 (우주선 게임의 Alien 로직) 
        self.speed_y = random.randint(2, 5) 

    def update(self):
        self.rect.y += self.speed_y
        
        # 화면 아래로 벗어나면 재배치 (우주선 게임의 Alien 로직)
        if self.rect.top > HEIGHT: 
            self.rect.x = random.randint(0, WIDTH - self.rect.width)
            self.rect.y = random.randint(-50, -10)
            self.speed_y = random.randint(2, 5)
            
    def explode(self):
        """충돌 시 폭발 처리 (우주선 게임 기능)"""
        # explosion_sound.play() # 폭발 사운드 재생
        pass # 현재는 소리만 처리

class Bullet(pygame.sprite.Sprite):
    """총알 클래스 (우주선 게임 기능)"""
    def __init__(self, x, y):
        super().__init__()
        # 이미지 대신 작은 흰색 사각형(총알) 생성 [cite: 330, 331]
        self.image = pygame.Surface((5, 15))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed_y = -7 # 위로 빠르게 이동

    def update(self):
        self.rect.y += self.speed_y
        
        # 화면 위로 벗어나면 스프라이트 그룹에서 제거 [cite: 337]
        if self.rect.bottom < 0:
            self.kill() 


# --- 게임 초기화 및 그룹 생성 ---
all_sprites = pygame.sprite.Group()
poop_group = pygame.sprite.Group() # 적 그룹 (Alien)
bullets = pygame.sprite.Group() # 총알 그룹

player = Player()
all_sprites.add(player)

# 똥 10개 생성 (우주선 게임의 Alien 로직) [cite: 314]
for i in range(10):
    new_poop = Poop()
    all_sprites.add(new_poop)
    poop_group.add(new_poop)

# --- 유틸리티 함수 ---
def draw_text(surface, text, size, x, y, color):
    font = pygame.font.SysFont('malgungothic', size) # 한글 지원 폰트 (시스템 폰트)
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, (x, y))

# --- 메인 루프 ---
running = True
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            # 스페이스 바 누를 때 총알 발사 
            if event.key == pygame.K_SPACE and not game_over:
                player.shoot()

    if not game_over:
        
        # 1. 게임 상태 업데이트
        all_sprites.update() 
        
        # 2. 총알 vs 똥 충돌 검사
        # 충돌 시 총알과 똥 모두 제거 (True, True) 
        hits = pygame.sprite.groupcollide(poop_group, bullets, True, True) 
        for hit in hits:
            player.score += 10 # 총알이 똥에 맞으면 점수 변수 변경
            hit.explode()      # 똥 폭발 처리
            
            # 똥이 제거되었으므로 즉시 새로운 똥 생성 (우주선 게임 로직)
            new_poop = Poop()
            all_sprites.add(new_poop)
            poop_group.add(new_poop)
            
        # 3. 덕새 vs 똥 충돌 검사
        player_hit_poops = pygame.sprite.spritecollide(player, poop_group, False) # 똥은 제거 안 함
        if player_hit_poops:
            player.health -= 1 # 똥 피격 시 변수 변경
            game_over = True # 충돌 시 바로 게임 오버 [cite: 534, 535]
    
    # ------------------ 그리기 ------------------
    screen.fill(BLACK) # 배경을 검은색으로 (우주선 게임 테마)
    
    all_sprites.draw(screen) 
    
    # 점수/체력 표시
    draw_text(screen, f"SCORE: {player.score}", 24, 10, 10, WHITE)
    draw_text(screen, f"HEALTH: {player.health}", 24, WIDTH - 120, 10, (255, 100, 100))
    
    if game_over:
        draw_text(screen, "GAME OVER", 50, WIDTH // 2 - 120, HEIGHT // 2, (255, 0, 0))
    
    pygame.display.flip()
    clock.tick(60) # FPS 제어 [cite: 124]

pygame.quit()
sys.exit()