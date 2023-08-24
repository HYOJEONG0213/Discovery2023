import pygame
import sys
import subprocess

# Pygame 초기화
pygame.init()

# 화면 크기 설정
screen_width = 400
screen_height = 696
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Block Game")

Lobby_1 = pygame.image.load("Lobby_1.png")
Lobby_2 = pygame.image.load("Lobby_2.png")
image_y = 0
current_image = Lobby_1


def draw_images():
    screen.blit(current_image, (0, image_y))


black = (0, 0, 0)
white = (255, 255, 255)

# 폰트 설정
font = pygame.font.Font('Maplestory Bold.ttf', 36)  # 폰트 설정



def show_instructions():
    instructions = ["블럭 맞추기 게임!",
                    "마우스로 블럭을 클릭하면 블럭이 놓아집니다.",
                    "R키를 누르면 블럭이 회전합니다."
                    "블럭 맞추다가 모르겠으면 H 버튼을 눌러보세요!"]
    screen.fill(black)
    
    for i, line in enumerate(instructions):
        text = font.render(line, True, white)
        screen.blit(text, (50, 200 + i * 40))
    pygame.display.flip()

# 버튼 생성
start_button = pygame.Rect(35, 200, 330, 35)   #x, y, width, height 좌표
instructions_button = pygame.Rect(35, 285, 330, 35)

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if current_image == Lobby_2 and event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if start_button.collidepoint(mouse_pos):
                pygame.quit()
                subprocess.run(["python", "main.py"])
                sys.exit()
            elif instructions_button.collidepoint(mouse_pos):
                show_instructions()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:    # 엔터 키를 누르면
                current_image = Lobby_2
                pygame.draw.rect(screen, (0,0,0,0), start_button)
                pygame.draw.rect(screen, (0,0,0,0), instructions_button)
                pygame.display.flip()
    # 배경 색
    screen.fill(white)

    draw_images()

    # 버튼 그리기
    

    # 버튼 텍스트 그리기
    #start_text = font.render("게임 시작", True, black)
    #instructions_text = font.render("게임 방법", True, black)
    #screen.blit(start_text, (start_button.x + 50, start_button.y + 10))
    #screen.blit(instructions_text, (instructions_button.x + 30, instructions_button.y + 10))

    pygame.display.flip()

# Pygame 종료
pygame.quit()
sys.exit()