from blockset_ai import *


board = [[1,0,0,0,0,0,1],
        [1,0,0,0,0,0,1],
        [1,1,0,0,1,1,1]]
block = [(0,0), (0,1), (-1,1)]
'''block = [[(0,0), (0,1), (-1,1)], [(0,0),(1,0),(1,1)], [(0,0),(1,0),(0,1)], [(0,0),(0,1),(1,1)], #ㄴ 모양
         [(0,0), (0,1), (0,2)], [(0,0), (1,0), (2,0)], #일렬, 3칸
         [(0,0), (0,1), (0,2), (1,0)], [(0,0), (0,1), (0,2), (-1,0)], [(0,0), (0,1), (0,2), (1,2)], [(0,0), (0,1), (0,2), (-1,2)], [(0,0), (1,0), (2,0), (0,1)], [(0,0), (1,0), (2,0), (0,-1)], [(0,0), (1,0), (2,0), (2,1)], [(0,0), (1,0), (2,0), (2,-1)], #긴 ㄴ모양
         [(0,0), (0,1), (0,2), (1,1)], [(0,0), (0,1), (0,2), (-1,1)], [(0,0), (1,0), (2,0), (1,1)], [(0,0), (1,0), (2,0), (1,-1)], #ㅗ 모양
         [(0,0), (0,1), (1,1), (1,2)], [(0,0), (0,1), (-1,1), (-1,2)], [(0,0), (1,0), (1,1), (2,1)], [(0,0), (1,0), (1,-1), (2,-1)], #ㄹ모양
         [(0,0), (0,1), (1,0), (1,1)], #ㅁ모양
         [(0,0), (0,1), (0,2), (0,3)], [(0,0), (1,0), (2,0), (3,0)], #일렬,4칸
         [(0,0), (0,1), (1,1), (2,1), (2,2)], [(0,0), (0,-1), (1,-1), (2,-1), (2,-2)], [(0,0), (1,0), (2,0), (2,1), (2,2)], [(0,0), (-1,0), (-1,1), (-2,1), (-2,2)], #긴 ㄹ모양
         [(0,0), (0,1), (1,0), (1,1), (2,0)], [(0,0), (0,1), (1,0), (1,1), (2,1)], [(0,0), (0,1), (1,0), (1,1), (-1,0)], [(0,0), (0,1), (1,0), (1,1), (-1,1)], [(0,0), (0,1), (1,0), (1,1), (0,2)], [(0,0), (0,1), (1,0), (1,1), (1,2)], [(0,0), (0,1), (1,0), (1,1), (0,-1)], [(0,0), (0,1), (1,0), (1,1), (1,-1)], #b 모양
         [(0,0), (0,1), (1,1), (1,2), (1,3)], [(0,0), (0,1), (-1,1), (-1,2), (-1,3)], [(0,0), (0,1), (0,2), (1,2), (1,3)], [(0,0), (0,1), (0,2), (-1,2), (-1,3)], [(0,0), (1,0), (1,1), (2,1), (3,1)], [(0,0), (1,0), (1,-1), (2,-1), (3,-1)], [(0,0), (1,0), (2,0), (2,1), (3,1)], [(0,0), (1,0), (2,0), (2,-1), (3,-1)], #2/3칸 모양
         [(0,0), (0,1), (1,0), (2,0), (2,1)], [(0,0), (0,-1), (1,0), (2,0), (2,-1)], [(0,0), (1,0), (0,1), (0,2), (1,2)], [(0,0), (-1,0), (0,1), (0,2), (-1,2)], #ㄷ모양
         [(0,0), (0,1), (0,2), (0,3), (0,4)], [(0,0), (1,0), (2,0), (3,0), (4,0), (5,0)], #일렬, 5칸
         ]'''

pygame.init()

H, W = 3, 7
block_num = 2
original_board = [row[:] for row in board]  # 게임 보드의 초기 상태 저장

screen = pygame.display.set_mode((W * 50, H * 50))
pygame.display.set_caption("Block Game")

def check_block_placement(mouse_x, mouse_y, block_x, block_y):  #해당 위치에 블록을 넣을 수 있는지 판별
    for dx, dy in block:
        nx, ny = block_x + dx, block_y + dy
        if nx < 0 or nx >= W or ny < 0 or ny >= H:
            return False
        if board[ny][nx] != 0:
            return False
    return True

running = True
hovered_block = None  # 마우스 위에 있는 블록 위치
color_changed = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:  #마우스 이동 이벤트 발생시 마우스 x, y값 가져옴
            mouse_x, mouse_y = event.pos
            block_x = mouse_x // 50
            block_y = mouse_y // 50
            
            if hovered_block == None:
                if check_block_placement(mouse_x, mouse_y, block_x, block_y):   #블록을 현재 위치에 넣을 수 있다면 확인하기
                    for dx, dy in block:
                        nx, ny = block_x + dx, block_y + dy
                        if 0 <= nx < W and 0 <= ny < H:
                            #original_board[ny][nx] = board[ny][nx]      
                            board[ny][nx] = block_num   #신규 hover된 위치의 색깔을 바꾸기
                    color_changed = True
                    hovered_block = (block_x, block_y)  # 현재 이 블록에 hover했다고 설정한다.

            if hovered_block != None and hovered_block != (block_x, block_y):   #이전 hover된 블록과 현재 hover된 블록이 다르다면
                for dx, dy in block:
                    nx, ny = hovered_block[0] + dx, hovered_block[1] + dy
                    if 0 <= nx < W and 0 <= ny < H:
                        board[ny][nx] = original_board[ny][nx]      #보드의 상태를 하버되기 전 상태로 되돌리기
                color_changed = True
            
                if check_block_placement(mouse_x, mouse_y, block_x, block_y):   #블록을 현재 위치에 넣을 수 있다면 확인하기
                    for dx, dy in block:
                        nx, ny = block_x + dx, block_y + dy
                        if 0 <= nx < W and 0 <= ny < H:
                            #original_board[ny][nx] = board[ny][nx]      
                            board[ny][nx] = block_num   #신규 hover된 위치의 색깔을 바꾸기
                    color_changed = True
                    hovered_block = (block_x, block_y)  # 현재 이 블록에 hover했다고 설정한다.
                else:
                    hovered_block = None

        elif event.type == pygame.MOUSEBUTTONDOWN:    #마우스 클릭시
            if color_changed and hovered_block:     #색상이 변경된 상태이면서 hover한 블록이 있는 경우
                for dx, dy in block:
                    nx, ny = hovered_block[0] + dx, hovered_block[1] + dy
                    if 0 <= nx < W and 0 <= ny < H:
                        board[ny][nx] = original_board[ny][nx]  #원래 상태로 되돌리기
                color_changed = False   #색상 변경 상태 초기화
                hovered_block = None
            else:
                mouse_x, mouse_y = event.pos
                block_x = mouse_x // 50
                block_y = mouse_y // 50
                if check_block_placement(mouse_x, mouse_y, block_x, block_y):
                    for dx, dy in block:
                        nx, ny = block_x + dx, block_y + dy
                        if 0 <= nx < W and 0 <= ny < H:
                            original_board[ny][nx] = board[ny][nx]
                            board[ny][nx] = block_num
                    color_changed = True
                    block_num += 1
                    

    draw_board(screen, board)
    pygame.time.Clock().tick(60)

pygame.quit()
