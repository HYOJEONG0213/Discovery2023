from blockset_ai import *


board = [[1,0,0,0,0,0,1],
        [1,0,0,0,0,0,1],
        [1,1,0,0,1,1,1]]
block_list = [[(0,0), (1,0), (0,1)], [(0,0), (0,1), (0,2)], [(0,0), (0,1), (0,2), (1,0)], [(0,0), (0,1), (0,2), (1,1)], [(0,0), (0,1), (1,0), (1,1)]]
block = []
#block = [(0,0), (0,1), (-1,1)]
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
selected_color_num = None
original_board = [row[:] for row in board]  # 게임 보드의 초기 상태 저장
original_block = [row[:] for row in block_list]
hover_color = 15

screen = pygame.display.set_mode((W * 50, H * 200))
pygame.display.set_caption("Block Game")

font = pygame.font.Font('Maplestory Bold.ttf', 36)  # 폰트 설정
message = ""
message_pos = (60, 500)  # 메시지 위치 설정 (x, y)

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
        elif block!=None and event.type == pygame.MOUSEMOTION:  #마우스 이동 이벤트 발생시 마우스 x, y값 가져옴
            mouse_x, mouse_y = event.pos
            block_x = mouse_x // 50
            block_y = mouse_y // 60
            
            if hovered_block == None:
                if check_block_placement(mouse_x, mouse_y, block_x, block_y):   #블록을 현재 위치에 넣을 수 있다면 확인하기
                    for dx, dy in block:
                        nx, ny = block_x + dx, block_y + dy
                        if 0 <= nx < W and 0 <= ny < H:
                            #original_board[ny][nx] = board[ny][nx]      
                            board[ny][nx] = hover_color   #신규 hover된 위치의 색깔을 바꾸기
                    color_changed = True
                    hovered_block = (block_x, block_y)  # 현재 이 블록에 hover했다고 설정한다.

            if hovered_block != None and hovered_block != (block_x, block_y):   #이전 hover된 블록과 현재 hover된 블록이 다르다면
                for dx, dy in block:
                    nx, ny = hovered_block[0] + dx, hovered_block[1] + dy
                    if 0 <= nx < W and 0 <= ny < H:
                        board[ny][nx] = original_board[ny][nx]      #보드의 상태를 하버되기 전 상태로 되돌리기
                        for i in range(len(board)):
                            for j in range(len(board[0])):
                                if board[i][j] == hover_color:
                                    board[i][j] = 0
                color_changed = True
            
                if check_block_placement(mouse_x, mouse_y, block_x, block_y):   #블록을 현재 위치에 넣을 수 있다면 확인하기
                    for dx, dy in block:
                        nx, ny = block_x + dx, block_y + dy
                        if 0 <= nx < W and 0 <= ny < H:
                            #original_board[ny][nx] = board[ny][nx]      
                            board[ny][nx] = hover_color   #신규 hover된 위치의 색깔을 바꾸기
                    color_changed = True
                    hovered_block = (block_x, block_y)  # 현재 이 블록에 hover했다고 설정한다.
                else:
                    hovered_block = None

        elif block!=None and event.type == pygame.MOUSEBUTTONDOWN:    #마우스 클릭시
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
                block_y = mouse_y // 60
                if check_block_placement(mouse_x, mouse_y, block_x, block_y):
                    for dx, dy in block:
                        nx, ny = block_x + dx, block_y + dy
                        if 0 <= nx < W and 0 <= ny < H:
                            original_board[ny][nx] = board[ny][nx]
                            board[ny][nx] = block_num
                    color_changed = True
                    block = []
                    message = ""
                    block_list.remove(block_list[select_block_num])
                    block_num += 1
                    '''for block_info in block_info:
                        if block_info["color_num"] == selected_color_num:
                            block_list'''
                    block = None
                    

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:  # 오른쪽 마우스 버튼 클릭 이벤트일 때
            mouse_x, mouse_y = event.pos
            block_x = mouse_x // 50
            block_y = mouse_y // 50
            a = []
            if 0 <= block_x < W and 0 <= block_y < H:
                clicked_color_num = board[block_y][block_x]
                if clicked_color_num != 0:  # 클릭한 위치에 색상이 있는 경우
                    for y in range(H):
                        for x in range(W):
                            if board[y][x] == clicked_color_num:
                                board[y][x] = 0
                                a.append((y, x))
                    block_num -=1
            block_list.append(a)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                print(block)
                for pos in range(len(block)):
                    pos_list = list(block[pos])
                    temp = pos_list[0]
                    pos_list[0] = pos_list[1]
                    pos_list[1] = temp * -1
                    block[pos] = tuple(pos_list)
                print(block)


    draw_board(screen, board)
    block_info = draw_block(screen, block_list, H, block_num)

    

    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # 마우스 왼쪽 버튼 클릭 이벤트일 때
        mouse_x, mouse_y = event.pos
        selected_color_num = None
        for block_info in block_info:
            if block_info["rect"].collidepoint(mouse_x, mouse_y):
                selected_color_num = block_info["color_num"]
                break
                # selected_color_num에 해당하는 블록들을 찾아 처리
                #for block_info in block_info:
                    #if block_info["color_num"] == selected_color_num:
        if selected_color_num != None:
            print(selected_color_num)
            message = "{}번 블럭 선택".format(selected_color_num-1)
            block = block_list[selected_color_num-block_num]
            select_block_num = selected_color_num-block_num
    message_surface = font.render(message, True, (0, 0, 0))  # 메시지를 렌더링하여 Surface 생성
    screen.blit(message_surface, message_pos)  # 메시지 Surface를 화면에 그리기


    pygame.display.flip()



    pygame.time.Clock().tick(60)

pygame.quit()