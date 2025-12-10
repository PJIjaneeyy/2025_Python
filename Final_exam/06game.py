# 1-1. 💩 피하기 게임 (py_game09 기반 디벨롭, 덕새 좌우 이동 제한)

import pygame
import random
import sys # sys.exit() 사용을 위해 추가

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("똥 피하기 게임 (좌우 제한)")

clock = pygame.time.Clock()

# 이미지 로드 (사과 이미지는 사용 안 함)
poop_img = pygame.image.load("poop.png")
poop_img = pygame.transform.scale(poop_img, (40, 40))

# --- 스프라이트 클래스 정의 ---

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("dukbird.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        
        # 덕새를 화면 하단 중앙에 배치 (피하기 게임 스타일)
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 20 
        self.speed = 5 # 이동 속도 증가
        self.lives = 3 # 추가 변수: 생명

    def update(self):
        keys = pygame.key.get_pressed()
        
        # 조건: 객체는 X축을 따라서만 좌우로 이동 가능
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            
        # UP, DOWN 키 입력은 무시됨
        # if keys[pygame.K_UP]: self.rect.y -= self.speed
        # if keys[pygame.K_DOWN]: self.rect.y += self.speed
        
        self.rect.clamp_ip(screen.get_rect()) # 화면 경계 제한

class Poop(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = poop_img
        self.rect = self.image.get_rect()
        
        # 위에서 아래로 후두둑 떨어짐
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = -self.rect.height # 화면 상단 밖에서 시작
        self.speed_y = random.randint(2, 5) # 떨어지는 속도 랜덤

    def update(self):
        self.rect.y += self.speed_y
        
        # 화면 아래로 벗어나면 스스로 제거
        if self.rect.top > HEIGHT:
            self.kill() # 스프라이트 그룹에서 제거

# --- 게임 초기화 ---

all_sprites = pygame.sprite.Group() 
poop_group = pygame.sprite.Group() 

player = Player()
all_sprites.add(player)

# 똥 생성 이벤트 (일정 주기로 똥 생성)
POOP_CREATE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(POOP_CREATE_EVENT, 1000) # 1초마다 이벤트 발생

# --- 사운드 추가 (시험 당일 파일 제공 예정 조건 반영) ---
# explosion_sound = pygame.mixer.Sound("explosion.wav")

game_over = False

def create_poop():
    new_poop = Poop()
    all_sprites.add(new_poop)
    poop_group.add(new_poop)

def draw_text(surface, text, size, x, y, color=(0, 0, 0)):
    font = pygame.font.SysFont(None, size)
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, (x, y))

# --- 메인 루프 ---

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == POOP_CREATE_EVENT and not game_over:
            create_poop() # 1초마다 똥 생성

    if not game_over:
        
        # 2. 게임 상태 업데이트
        all_sprites.update() 
        
        # 3. 충돌 감지 및 변수 변경 (똥 vs 플레이어)
        hits = pygame.sprite.spritecollide(player, poop_group, True) # 충돌한 똥은 제거(True)
        if hits:
            player.lives -= 1 # 객체가 부딪혔을 때 변수 변경
            # explosion_sound.play() # 사운드 재생 (파일 제공 시 주석 해제)
            
            if player.lives <= 0:
                game_over = True
    
    # ------------------ 그리기 ------------------
    screen.fill((170, 200, 255))
    all_sprites.draw(screen) 
    
    # 점수/생명 표시
    draw_text(screen, f"Lives: {player.lives}", 24, 10, 10, (255, 0, 0))
    
    if game_over:
        draw_text(screen, "GAME OVER", 50, WIDTH // 2 - 120, HEIGHT // 2, (255, 0, 0))
        draw_text(screen, "Press R to Restart", 30, WIDTH // 2 - 110, HEIGHT // 2 + 50, (0, 0, 0))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()