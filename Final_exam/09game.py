# 3. 🍎 💩 복합형: 똥 피하고 사과 먹기 (종합 문제)

import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("똥 피하고 사과 먹기 (종합)")

clock = pygame.time.Clock()

apple_img = pygame.image.load("apple.png")
apple_img = pygame.transform.scale(apple_img, (40, 40))
poop_img = pygame.image.load("poop.png")
poop_img = pygame.transform.scale(poop_img, (40, 40))

# 사운드 준비 (시험 당일 파일 제공 조건 반영)
# eat_sound = pygame.mixer.Sound("eat.wav") 
# hit_sound = pygame.mixer.Sound("hit.wav")

# --- 스프라이트 클래스 정의 ---

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("dukbird.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed = 5
        self.score = 0
        self.health = 5 # 추가 변수: 체력

    def update(self):
        # 조건: 피하기 게임이 아니므로 상하좌우 모두 이동 가능
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]: self.rect.x += self.speed
        if keys[pygame.K_UP]: self.rect.y -= self.speed
        if keys[pygame.K_DOWN]: self.rect.y += self.speed
        self.rect.clamp_ip(screen.get_rect())

class Poop(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = poop_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = -self.rect.height
        # 똥은 위에서 아래로만 이동 (랜덤)
        self.speed_y = random.randint(2, 4)

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > HEIGHT:
            self.kill()

class Apple(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = apple_img
        self.rect = self.image.get_rect()
        
        # 사과는 화면 사방팔방에서 랜덤하게 등장 (원본 코드 유지)
        side = random.choice(["left", "right", "top", "bottom"])
        size = 40
        if side == "left":
            x, y = -size, random.randint(0, HEIGHT - size)
            vx, vy = random.randint(2, 4), random.randint(-2, 2)
        elif side == "right":
            x, y = WIDTH, random.randint(0, HEIGHT - size)
            vx, vy = -random.randint(2, 4), random.randint(-2, 2)
        elif side == "top":
            x, y = random.randint(0, WIDTH - size), -size
            vx, vy = random.randint(-2, 2), random.randint(2, 4)
        else: # "bottom"
            x, y = random.randint(0, WIDTH - size), HEIGHT
            vx, vy = random.randint(-2, 2), -random.randint(2, 4)

        self.rect.topleft = (x, y)
        self.vx = vx
        self.vy = vy

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        
        # 화면을 벗어나면 제거
        if self.rect.right < 0 or self.rect.left > WIDTH or self.rect.bottom < 0 or self.rect.top > HEIGHT:
            self.kill()

# --- 게임 초기화 ---

all_sprites = pygame.sprite.Group() 
poop_group = pygame.sprite.Group() 
apple_group = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

# 객체 생성 이벤트 설정
POOP_EVENT = pygame.USEREVENT + 1
APPLE_EVENT = pygame.USEREVENT + 2
pygame.time.set_timer(POOP_EVENT, 1500) # 1.5초마다 똥 생성
pygame.time.set_timer(APPLE_EVENT, 1000) # 1초마다 사과 생성

game_over = False

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
        
        if event.type == POOP_EVENT and not game_over:
            new_poop = Poop()
            all_sprites.add(new_poop)
            poop_group.add(new_poop)
            
        if event.type == APPLE_EVENT and not game_over:
            new_apple = Apple()
            all_sprites.add(new_apple)
            apple_group.add(new_apple)

    if not game_over:
        
        all_sprites.update() 
        
        # 1. 사과 충돌 (먹기)
        apple_hits = pygame.sprite.spritecollide(player, apple_group, True) # 사과는 제거
        for hit in apple_hits:
            player.score += 10 # 사과 먹을 시 변수 변경
            # eat_sound.play()
            
        # 2. 똥 충돌 (피격)
        poop_hits = pygame.sprite.spritecollide(player, poop_group, True) # 똥은 제거
        if poop_hits:
            player.health -= 1 # 똥 피격 시 변수 변경
            # hit_sound.play()
            
            if player.health <= 0:
                game_over = True
    
    # ------------------ 그리기 ------------------
    screen.fill((170, 200, 255))
    all_sprites.draw(screen) 
    
    # 점수/체력 표시
    draw_text(screen, f"Score: {player.score}", 24, 10, 10, (0, 0, 0))
    draw_text(screen, f"Health: {player.health}", 24, 10, 40, (255, 0, 0))
    
    if game_over:
        draw_text(screen, "GAME OVER", 50, WIDTH // 2 - 120, HEIGHT // 2, (255, 0, 0))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()