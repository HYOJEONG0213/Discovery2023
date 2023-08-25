import pygame
import sys
from Game import *
import random

board_5x5 = [
             [[1,0,1,0,1],
             [0,0,0,0,0],
             [0,0,0,0,1],
             [1,0,0,0,1],
             [1,0,1,1,1],],

             [[1,0,0,0,1],
            [0,0,0,0,1],
            [0,0,0,0,0],
            [1,0,0,0,1],
            [0,0,0,1,1],],

            [[1,1,0,0,0],
            [1,1,0,0,0],
            [1,0,0,0,1],
            [0,0,0,0,0],
            [0,0,0,0,1],],

            [[0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],],

            [[0,0,0,0,0],
            [0,1,0,1,0],
            [0,0,0,0,0],
            [0,0,1,1,0],
            [0,0,0,0,0],]
            ]
block_list_5x5 = [[[(0,0), (0,1), (1,1)], [(0,0), (0,1), (0,2), (1,2)], [(0,0), (0,1), (0,2), (1,1)], [(0,0), (0,1), (1,0), (1,1)]],
                  [[(0,0), (0,1), (1,1)], [(0,0), (0,1), (0,2)], [(0,0), (0,1), (0,2), (1,2)], [(0,0), (0,1), (0,2), (1,1)], [(0,0), (0,1), (1,0), (1,1)]],
                 [[(0,0),(0,1),(0,2)],[(0,0),(0,1),(1,1)],[(0,0),(0,1),(0,2),(0,3)],[(0,0),(0,1),(1,0),(2,0)],[(0,0),(0,1),(0,2),(1,0)]],
                 [[(0,0),(0,1),(1,1)],[(0,0),(0,1),(0,2),(0,3)],[(0,0),(1,0),(1,1),(2,0)], [(0,0),(1,0),(1,1),(2,1)],[(0,0),(0,1),(0,2),(0,3),(1,3)],[(0,0),(0,1),(1,0),(1,1),(1,2)]],
                 [[(0,0), (0,1), (0,2)], [(0,0), (0,1), (0,2), (1,2)], [(0,0), (0,1), (0,2), (1,1)], [(0,0),(0,1),(0,2),(0,3),(0,4)], [(0,0),(0,1),(0,2),(0,3),(0,4)]]
]


board_7x7 = [
    [[0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],],
]
block_list_7x7 = [[[(0,0),(0,1),(1,1)], #3칸
                    [(0,0),(0,1),(0,2),(0,3)],[(0,0),(1,0),(1,1),(2,0)],[(0,0),(0,1),(1,1),(1,2)],[(0,0),(1,0),(1,1),(2,1)],[(0,0),(0,1),(1,0),(1,1)], #4칸
                    [(0,0),(0,1),(0,2),(0,3),(1,0)],[(0,0),(0,1),(0,2),(0,3),(1,3)],[(0,0),(0,1),(0,2),(1,0),(1,1)],[(0,0),(0,1),(1,0),(1,1),(1,2)],
                    [(0,0),(0,1),(0,2),(0,3),(0,4),(1,0)]],#6칸
                ]


board_10x10 = [
    [[0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],],
]
block_list_10x10 = [[[(0,0),(0,1),(0,2)],[(0,0),(0,1),(1,1)], #3칸
                     
                    [(0,0),(0,1),(0,2),(0,3)],[(0,0),(0,1),(1,0),(2,0)],[(0,0),(0,1),(0,2),(1,0)],[(0,0),(1,0),(1,1),(2,0)],
                    [(0,0),(0,1),(1,1),(1,2)],[(0,0),(1,0),(1,1),(2,1)],[(0,0),(0,1),(1,0),(1,1)], #4칸

                    [(0,0),(0,1),(0,2),(0,3),(0,4)],[(0,0),(0,1),(0,2),(0,3),(1,0)],[(0,0),(0,1),(0,2),(0,3),(1,3)],
                    [(0,0),(0,1),(0,2),(1,0),(1,1)],[(0,0),(0,1),(1,0),(1,1),(1,2)],[(0,0),(0,1),(0,2),(1,2),(1,3)],
                    [(0,0),(0,1),(1,1),(1,2),(1,3)],[(0,0),(0,1),(0,2),(1,0),(2,0)],[(0,0),(0,1),(0,2),(1,0),(1,2)],
                    [(0,0),(0,1),(0,2),(0,3),(1,1)],[(0,0),(0,1),(0,2),(0,3),(1,2)], #5칸
                ]]


# Pygame 초기화
pygame.init()

# 화면 크기 설정
screen_width = 400
screen_height = 696
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Block Game")

Lobby_1 = pygame.image.load("Lobby_1.png")
Lobby_2 = pygame.image.load("Lobby_2.png")
Introduce = pygame.image.load("Introduce.png")
Rule = pygame.image.load("Rule.png")
SelectPuzzle = pygame.image.load("Select_image.png")
image_y = 0

current_image = Lobby_1

def draw_images():
    screen.blit(current_image, (0, image_y))
    #pygame.draw.rect(screen, black, button_5x5)
    #pygame.draw.rect(screen, black, button_7x7)
    #pygame.draw.rect(screen, black, button_10x10)


black = (0, 0, 0)
white = (255, 255, 255)
null_color = (0, 0, 0, 0)

# 폰트 설정
font = pygame.font.Font('Maplestory Bold.ttf', 36)  # 폰트 설정


def Lobby2():
    global current_image
    current_image = Lobby_2
    pygame.draw.rect(screen, black, instructions_button)
    pygame.draw.rect(screen, black, rules_button)
    pygame.draw.rect(screen, black, start_button)
    pygame.draw.rect(screen, black, exit_button)
    pygame.display.flip()
    

def instructions():
    pygame.init()
    global current_image
    current_image = Introduce
    pygame.draw.rect(screen, black, back_button)
    pygame.display.flip()


def rule():
    pygame.init()
    global current_image
    current_image = Rule
    pygame.draw.rect(screen, black, back_button)
    pygame.display.flip()

def Select_puzzle():
    pygame.init()
    global current_image
    current_image = SelectPuzzle
    pygame.draw.rect(screen, null_color, button_5x5)
    pygame.draw.rect(screen, null_color, button_7x7)
    pygame.draw.rect(screen, null_color, button_10x10)
    pygame.display.flip()


# 버튼 생성
instructions_button = pygame.Rect(35, 200, 330, 35)   #x, y, width, height 좌표
rules_button = pygame.Rect(35, 285, 330, 35)
start_button= pygame.Rect(35, 370, 330, 35)
exit_button= pygame.Rect(35, 455, 330, 35)
back_button = pygame.Rect(0, 35, 60, 60)
button_5x5 = pygame.Rect(75, 120, 250, 140)
button_7x7 = pygame.Rect(75, 280, 250, 140)
button_10x10 = pygame.Rect(75, 440, 250, 140)

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif current_image == Lobby_2 and event.type == pygame.MOUSEBUTTONDOWN:   #로비에서 게임메뉴 버튼을 눌렀을 때
            mouse_pos = pygame.mouse.get_pos()
            if start_button.collidepoint(mouse_pos):
                Select_puzzle()
                #pygame.quit()
                #subprocess.run(["python", "main.py"])
                #sys.exit()
            elif instructions_button.collidepoint(mouse_pos):
                instructions()
            elif rules_button.collidepoint(mouse_pos):
                rule()
            elif exit_button.collidepoint(mouse_pos):
                running = False
        elif (current_image == Introduce) and event.type == pygame.MOUSEBUTTONDOWN:   #뒤로가기 버튼을 눌렀을 때 Lobby2로 돌아가기
            mouse_pos = pygame.mouse.get_pos()
            if back_button.collidepoint(mouse_pos):
                Lobby2()
        elif (current_image == Rule) and event.type == pygame.MOUSEBUTTONDOWN:   #뒤로가기 버튼을 눌렀을 때 Lobby2로 돌아가기
            mouse_pos = pygame.mouse.get_pos()
            if back_button.collidepoint(mouse_pos):
                Lobby2()
        elif current_image == Lobby_1 and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:    # 엔터 키를 누르면
                Lobby2()
        elif (current_image == SelectPuzzle) and event.type == pygame.MOUSEBUTTONDOWN:   #퍼즐 선택창에서 퍼즐크기를 선택했을 때
            mouse_pos = pygame.mouse.get_pos()
            if button_5x5.collidepoint(mouse_pos):
                print("5x5 버튼 선택!")
                r = random.randint(0, len(board_5x5)-1)
                print(r)
                game = Game(board_5x5[3], block_list_5x5[3])
                sys.exit()
            if button_7x7.collidepoint(mouse_pos):
                print("7x7 버튼 선택!")
                r = random.randint(0, len(board_7x7)-1)
                print(r)
                game = Game(board_7x7[r], block_list_7x7[r])
                sys.exit()
            if button_10x10.collidepoint(mouse_pos):
                print("10x10 버튼 선택!")
                r = random.randint(0, len(board_10x10)-1)
                print(r)
                game = Game(board_10x10[r], block_list_10x10[r])
                sys.exit()
            

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