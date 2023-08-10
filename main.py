import pygame

# 블록 모양
block_shape = [(0, 0), (0, 1), (-1, 1)]

pygame.init()

H, W = 3, 7
board = [['.' for _ in range(W)] for _ in range(H)]
original_board = [row[:] for row in board]  # 게임 보드의 초기 상태 저장

screen = pygame.display.set_mode((W * 50, H * 50))
pygame.display.set_caption("Block Color Change")

def draw_board(screen, board):
    screen.fill((255, 255, 255))  # 배경을 흰색으로 채우기
    
    block_size = 50  # 각 블록의 크기
    border_size = 5  # 테두리 크기

    
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            rect = pygame.Rect(x * block_size, y * block_size, block_size, block_size)
            pygame.draw.rect(screen, (255, 255, 255), rect)  # 블록 테두리 그리기
            inner_rect = pygame.Rect(rect.left + border_size, rect.top + border_size, rect.width - 2 * border_size, rect.height - 2 * border_size)
            
            color = (0, 0, 0) if cell == '#' else (255, 255, 255)
            pygame.draw.rect(screen, color, inner_rect)
    
    pygame.display.flip()

def check_block_placement(mouse_x, mouse_y, block_x, block_y):
    for dx, dy in block_shape:
        nx, ny = block_x + dx, block_y + dy
        if nx < 0 or nx >= W or ny < 0 or ny >= H:
            return False
        if board[ny][nx] == '#':
            return False
    return True

running = True
hovered_block = None  # 마우스 위에 있는 블록 위치
color_changed = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = event.pos
            block_x = mouse_x // 50
            block_y = mouse_y // 50
            
            if hovered_block is not None and hovered_block != (block_x, block_y):
                for dx, dy in block_shape:
                    nx, ny = hovered_block[0] + dx, hovered_block[1] + dy
                    if 0 <= nx < W and 0 <= ny < H:
                        board[ny][nx] = original_board[ny][nx]
                color_changed = True
            
            if check_block_placement(mouse_x, mouse_y, block_x, block_y):
                for dx, dy in block_shape:
                    nx, ny = block_x + dx, block_y + dy
                    if 0 <= nx < W and 0 <= ny < H:
                        original_board[ny][nx] = board[ny][nx]
                        board[ny][nx] = '#'
                color_changed = True
                hovered_block = (block_x, block_y)
            else:
                hovered_block = None

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if color_changed and hovered_block:
                color_changed = False
            else:
                mouse_x, mouse_y = event.pos
                block_x = mouse_x // 50
                block_y = mouse_y // 50
                if check_block_placement(mouse_x, mouse_y, block_x, block_y):
                    for dx, dy in block_shape:
                        nx, ny = block_x + dx, block_y + dy
                        if 0 <= nx < W and 0 <= ny < H:
                            original_board[ny][nx] = board[ny][nx]
                            board[ny][nx] = '#'
                    color_changed = True
                    hovered_block = None

    draw_board(screen, board)
    pygame.time.Clock().tick(60)

pygame.quit()
