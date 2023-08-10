import pygame
from collections import deque

# 블록 타입과 색상 매핑
block_colors = {
    '.': (255, 255, 255),  # 빈 공간
    '#': (0, 0, 0)  # 블록
}

# 블록 모양 정의
coverType = [
    [[(0,0), (0,1), (-1,1)], [(0,0),(1,0),(1,1)], [(0,0),(1,0),(0,1)], [(0,0),(0,1),(1,1)]],
    [[(0,0),(0,1),(0,2)], [(0,0),(1,0),(2,0)]]
]

def draw_board(screen, board):
    screen.fill((255, 255, 255))  # 배경을 흰색으로 채우기
    
    block_size = 50  # 각 블록의 크기
    border_size = 5  # 테두리 크기


    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            rect = pygame.Rect(x * block_size, y * block_size, block_size, block_size)
            pygame.draw.rect(screen, (0, 0, 0), rect)  # 블록 테두리 그리기
            inner_rect = pygame.Rect(rect.left + border_size, rect.top + border_size,
                                     rect.width - 2 * border_size, rect.height - 2 * border_size)
            color = block_colors[cell]


            pygame.draw.rect(screen, color, inner_rect)
    
    pygame.display.flip()

def rotate_block(block):
    # 블록을 시계방향으로 90도 회전
    return [[-y, x] for x, y in block]

pygame.init()

H, W = 3, 7
board = [['.' for _ in range(W)] for _ in range(H)]

screen = pygame.display.set_mode((W * 50, H * 50))
pygame.display.set_caption("Block Game")

running = True
placing_block = False
current_block_type = 0
current_block_rotation = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            if not placing_block:
                mouse_x, mouse_y = event.pos
                block_x = mouse_x // 50
                block_y = mouse_y // 50
                if 0 <= block_x < W and 0 <= block_y < H:
                    board[block_y][block_x] = '#'
                    draw_board(screen, board)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if not placing_block:
                placing_block = True
                mouse_x, mouse_y = event.pos
                block_x = mouse_x // 50
                block_y = mouse_y // 50
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if placing_block:
                placing_block = False
                board[block_y][block_x] = '#'
                draw_board(screen, board)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                current_block_rotation = (current_block_rotation + 1) % len(coverType[current_block_type])
                draw_board(screen, board)

    if placing_block:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        block_x = mouse_x // 50
        block_y = mouse_y // 50

        if 0 <= block_x < W and 0 <= block_y < H:
            board[block_y][block_x] = '#'
            draw_board(screen, board)

    pygame.time.Clock().tick(60)

pygame.quit()
