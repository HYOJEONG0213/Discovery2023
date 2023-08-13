#화면 구현 버전


#퍼즐 맞추기222
#https://velog.io/@hancihu/Python-Algorithm-%EC%95%8C%EA%B3%A0%EC%8A%A4%ED%8C%9F-%EA%B2%8C%EC%9E%84%ED%8C%90-%EB%8D%AE%EA%B8%B0-BOARDCOVER

#게임판의 크기 H, W (1≤H, W≤10)
#블록의 모양을 나타내는 격자의 크기 R, C (1≤R, C≤10)

from collections import deque
import pygame





#answer = []


def draw_board(screen, board):
    screen.fill((255, 255, 255))  # 화면을 흰색으로 채우기

    block_size = 50  # 각 블록의 크기
    border_size = 2  # 테두리 크기


    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            rect = pygame.Rect(x * block_size, y * block_size + 50, block_size, block_size)
            pygame.draw.rect(screen, (255, 255, 255), rect)  # 블록 테두리 그리기
            inner_rect = pygame.Rect(rect.left + border_size, rect.top + border_size, rect.width - 2 * border_size, rect.height - 2 * border_size)

            color = select_color(cell)
            
            pygame.draw.rect(screen, (255,255,255), rect, border_size)
            pygame.draw.rect(screen, color, inner_rect)
    
    

def select_color(cell):
    if cell == 0:
        color = (255, 255, 255)     #흰색: 비어있는 블럭
    elif cell == 1:
        color = (0, 0, 0)   #검정색: 이미 차있는 블럭
    elif cell == 2:
        color = (0, 255, 0)     #초록색(녹색성분)
    elif cell == 3:
        color = (0, 128, 0)     #초록색
    elif cell == 4:
        color = (255, 0, 0)   #레드(빨강 성분)
    elif cell == 5:
        color = (255, 165, 0)   #주황색(빨강, 녹색성분)
    elif cell == 6:
        color = (255, 99, 71)   #주황색
    elif cell == 7:
        color =  (0, 0, 255)   #파란색
    elif cell == 8:
        color = (0, 0, 128)   #파란색
    elif cell == 9:
        color = (0, 0, 139)   #파란색
    elif cell == 10:
        color = (128, 0, 128)   #보라색(빨강, 파랑 성분)
    elif cell == 11:
        color = (148, 0, 211)    #보라색
    elif cell == 12:
        color = (255, 255, 0)    #노란색(빨강, 녹색 성분)
    elif cell == 13:
        color = (255, 255, 102)    #노란색
    elif cell == 14:
        color = (255, 105, 180)    #핑크색 (빨강 성분)
    elif cell == 15:
        color = (255, 182, 193)    #핑크색 (빨강 성분)    
    else:
        color = (255, 255, 255)
    return color


def boardCover(screen, board, block):
    Q = deque()
    L = 0
    Q.append((board, L))
    
    count = 0
    
    while Q:    #BFS방법 이용하기
        cur_board, level = Q.popleft()  #큐에서 가장 왼쪽꺼 빼내고
        
        x, y = -1, -1
        for i in range(H):
            for j in range(W):
                if cur_board[i][j] == 0:    #board에서 비어있는 구역이라면
                    x = j
                    y = i
                    break   #비어있는 i, j값을 x, y로 저장하기
            if y != -1:     
                break   
                
        if x == -1 and y == -1:     #모두 다 차있다면
            count += 1
            draw_board(screen, cur_board)
            for i in range(H):
                for j in range(W):
                    print(cur_board[i][j], end =' ')
                print("\n")
            print()
            return 1
            #continue
        
        
        for cover in block:
            flag = True
            for dx, dy in cover:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= W or ny < 0 or ny >= H:   #범위 밖이라면
                    flag = False
                    break
                elif cur_board[ny][nx] != 0:    #이미 그 자리에 차있다면
                    flag = False
                    break 
            if flag:    #넣을 수 있다고 판단했다면
                new_board = [row[:] for row in cur_board]   #원본 cur_board를 수정하지 않고 복사하고,
                #a = []
                for dx, dy in cover:
                    nx, ny = x + dx, y + dy
                    new_board[ny][nx] = level+2
                    #a.append([ny, nx])
                    #board[ny][nx] = block_num   #채우기
                    #answer.append([ny, nx])
                #answer.append(a)
                #new_board = [''.join(row) for row in new_board]  # 리스트를 문자열로 변환
                Q.append((new_board, level+1))  #새로운 상태의 보드를 생성하여 큐에 추가하기
                draw_board(screen, new_board)
                pygame.time.wait(10)  # 0.5초 대기
                
                #if count != 0:
                #    break
            #else:
                #answer.clear()
        '''
        a=[]
        for dx, dy in cover:
            nx, ny = x + dx, y+ dy
            a.append([ny, nx])
        answer.append(a)'''
    return count
        

# 블럭들의 모양 그리기
def draw_block(screen, block_list, H, color_num):
    block_info = []
    block_size = 30  # 블록의 크기
    border_size = 5  # 테두리 크기
    start_x = 50  # 블록들의 모양 시작 X 좌표
    start_y = H * block_size + 200  # 블록들의 모양 시작 Y 좌표
    spacing = 10  # 블록들 간의 간격

    for idx, block in enumerate(block_list):
        max_block_width = max(x for y, x in block)  # 각 블록의 최대 너비 계산
        block_width = len(block[0])  # 블록의 너비
        block_height = len(block)  # 블록의 높이

        for y, x in block:
            rect = pygame.Rect(start_x + (x * (block_size + spacing)) + (max_block_width - block_width) * (block_size + spacing) / 2,
                           start_y + (y * block_size),
                           block_size, block_size)
            inner_rect = pygame.Rect(rect.left + border_size, rect.top + border_size,
                                 rect.width - 2 * border_size, rect.height - 2 * border_size)
            color = select_color(color_num)

            pygame.draw.rect(screen, color, inner_rect)     # 블록 내부 그리기
            pygame.draw.rect(screen, (255,255,255), rect, border_size)  # 블록 테두리 그리기

            block_info.append({"color_num":color_num, "rect":rect})

        if idx % 2 == 0:
            start_x += block_width + 150
        else:
            start_x = 50
            start_y += block_height + 100
        color_num +=1
    return block_info



'''screen = pygame.display.set_mode((210, 90))
pygame.time.wait(5000)  # 5초 대기
pygame.quit()'''

'''
if __name__=="__main__":
    board = [[1,0,0,0,0,0,1],
        [1,0,0,0,0,0,1],
        [1,1,0,0,1,1,1]]
    
    block = [[(0,0), (0,1), (-1,1)], [(0,0),(1,0),(1,1)], [(0,0),(1,0),(0,1)], [(0,0),(0,1),(1,1)], #ㄴ 모양
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
         ]
    
    H = 3
    W = 7


    screen = pygame.display.set_mode((W * 30, H * 30))

    boardCover(screen)
    #print(answer)

    pygame.time.wait(5000)  # 5초 대기
    pygame.quit()'''