# 1. 🥇 유형: 똥 피하고 코인 먹기 (좌우 이동 제한)
import pygame
import random
import sys

pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("똥 피하고 코인 먹기 (좌우 이동)")
clock = pygame.time.Clock()
# 이미지 로드 (코인 이미지는 임의의 원으로 대체)
poop_img = pygame.image.load("poop.png")
poop_img = pygame.transform.scale(poop_img, (40, 40))

# --- Player (좌우 이동 제한) ---
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("dukbird.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 20 # 하단 고정
        self.speed = 7
        self.score = 0
        self.lives = 3
    def update(self):
        keys = pygame.key.get_pressed()
        # [핵심] 좌우(X축) 이동만 허용
        if keys[pygame.K_LEFT]: self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]: self.rect.x += self.speed
        self.rect.clamp_ip(screen.get_rect())

# --- Item 클래스 (똥/코인의 부모) ---
class FallingItem(pygame.sprite.Sprite):
    def __init__(self, is_poop):
        super().__init__()
        self.is_poop = is_poop
        if is_poop:
            self.image = poop_img
        else:
            # 코인: 이미지 대신 노란색 원으로 표현
            self.image = pygame.Surface((30, 30), pygame.SRCALPHA) # 투명 배경
            pygame.draw.circle(self.image, (255, 223, 0), (15, 15), 15)
            
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = -self.rect.height
        self.speed_y = random.randint(3, 6)

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > HEIGHT:
            self.kill() # 화면 밖으로 나가면 제거

# --- 게임 초기화 ---
all_sprites = pygame.sprite.Group() 
item_group = pygame.sprite.Group() 

player = Player()
all_sprites.add(player)

# 아이템 생성 이벤트
ITEM_CREATE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(ITEM_CREATE_EVENT, 500) # 0.5초마다 아이템 생성

def create_item():
    is_poop = random.choice([True, False, False]) # 똥 1: 코인 2 비율
    new_item = FallingItem(is_poop)
    all_sprites.add(new_item)
    item_group.add(new_item)

# --- 메인 루프 ---
running = True
game_over = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == ITEM_CREATE_EVENT and not game_over:
            create_item()

    if not game_over:
        all_sprites.update()
        
        # [핵심] 충돌 처리 및 변수 변경
        hits = pygame.sprite.spritecollide(player, item_group, True) # 충돌 시 아이템 제거(True)
        for item in hits:
            if item.is_poop:
                player.lives -= 1 # 똥: 생명 감소 (변수 변경)
                # print("똥 피격!")
            else:
                player.score += 10 # 코인: 점수 증가 (변수 변경)
                # print("코인 획득!")
                
        # 게임 오버 조건
        if player.lives <= 0:
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