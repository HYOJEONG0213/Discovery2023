#화면 구현 버전


#퍼즐 맞추기222
#https://velog.io/@hancihu/Python-Algorithm-%EC%95%8C%EA%B3%A0%EC%8A%A4%ED%8C%9F-%EA%B2%8C%EC%9E%84%ED%8C%90-%EB%8D%AE%EA%B8%B0-BOARDCOVER

#게임판의 크기 H, W (1≤H, W≤10)
#블록의 모양을 나타내는 격자의 크기 R, C (1≤R, C≤10)

from collections import deque
import pygame
import copy
from board_setting import *

#answer = []

pygame.init()

font = pygame.font.Font('Maplestory Bold.ttf', 36)  # 폰트 설정
message = ""
#message_pos = (W * 50 // 2, H * 150 // 4)  # 메시지 위치 설정 (x, y)
message_pos = (70, 500)  


def boardCover(screen, board, blocks, H, W, block_num2):
    Q = deque()
    L = 0
    b = [0] * len(blocks)
    Q.append((board, L, b, block_num2))
    temp_blocks = blocks
    block = []

    print("test: blocks: ")

    '''
    for i in range(len(blocks)):
        a= []
        for j in range(0, 4):
            for pos in range(len(temp_blocks[i])):
                    pos_list = list(temp_blocks[i][pos])
                    temp = pos_list[0]
                    pos_list[0] = pos_list[1]
                    pos_list[1] = temp * -1
                    temp_blocks[i][pos] = tuple(pos_list)
            temp_block = copy.deepcopy(temp_blocks[i])
            a.append(temp_block)
        block.append(a)
    print(block)'''

    for i in range(len(blocks)):
        block_set = []
        for j in range(0, 4):
            x_min = 0
            y_min = 0
            for pos in range(len(temp_blocks[i])):
                pos_list = list(temp_blocks[i][pos])
                temp = pos_list[0]
                pos_list[0] = pos_list[1]
                pos_list[1] = temp * -1
                temp_blocks[i][pos] = tuple(pos_list)
            for pos in range(len(temp_blocks[i])):
                pos_list = temp_blocks[i][pos]
                if x_min > pos_list[0]:
                    x_min = pos_list[0]
                if y_min > pos_list[1]:
                    y_min = pos_list[1]
            for pos in range(len(temp_blocks[i])):
                pos_list = list(temp_blocks[i][pos])
                pos_list[0] -= x_min
                pos_list[1] -= y_min
                temp_blocks[i][pos] = tuple(pos_list)
            temp_block = copy.deepcopy(temp_blocks[i])
            block_set.append(temp_block)
        block.append(block_set)
    

    for i in range(len(block)):
        for j in range(len(block[i])):
            block[i][j].sort(key=lambda coord: (coord[0], coord[1]))




    print(block)
    #pygame.time.wait(10000)  # 0.5초 대기

    
    while Q:    #BFS방법 이용하기
        print("\n\n새 블록 시작!")
        a = []
        block_to_remove = {}
        cur_board, level, cur_block, block_num2 = Q.popleft()  #큐에서 가장 왼쪽꺼 빼내고
        x, y = -1, -1
        
        print(cur_board)
        for i in range(H):      
            for j in range(W):
                if cur_board[i][j] == 0:    #board에서 비어있는 구역이라면
                        x = j
                        y = i
                        break   #비어있는 i, j값을 x, y로 저장하기

            if y != -1:     
                break
            print("\n")   

        if x == -1 and y == -1:     #모두 다 차있다면
            #sorted_values = [sorted(value) for value in block_to_remove.values()]
            #unique_values = set(tuple(value) for value in sorted_values)
            #if len(unique_values) != len(block_to_remove):
             #   continue

            answer = True
            print(cur_block)
            for i in range(H):
                for j in range(W):
                    board[i][j] = cur_board[i][j]
                    print(cur_board[i][j], end =' ')
                print("\n")
            print()
            draw_board(screen, board)
            return("clear!")
            #continue
            pygame.time.wait(3000)  # 0.5초 대기


        for i in range(H):      
            for j in range(W):
                if cur_board[i][j] !=0 and cur_board[i][j] !=1:         #현재 블록에서 어떤 블록을 썼는지 확인하기
                    block_num = cur_board[i][j]
                    if block_num not in block_to_remove:
                        block_to_remove[block_num] = []
                    block_to_remove[block_num].append((j, i))

        #block_to_remove = {}
        for block_num, coords_list in block_to_remove.items():  #현재까지 어떤 블록을 썼었는지 대칭이동 시키기(블럭 모양 확인)
            coords_list.sort(key=lambda coord: (coord[0], coord[1]))  # 람다 함수를 사용하여 y좌표를 기준으로 정렬하고, 그 후 x좌표를 기준으로 정렬합니다.
            min_x = min(x for x, y in coords_list)
            min_y = min(y for x, y in coords_list)

            shifted_coords = [(x - min_x, y - min_y) for x, y in coords_list]
            min_x = min(x for x, y in shifted_coords)
            min_y = min(y for x, y in shifted_coords)

            updated_coords_list = [(x - min_x, y - min_y) for x, y in shifted_coords]
            block_to_remove[block_num] = updated_coords_list

        

        

        #남은 블록들
        remained_block = []

        for shape in block:
            should_keep_shape = True  # 이번 블록을 유지할것인가
            for sublist in shape:
                #print("sublist: ", sublist)
                if sublist in block_to_remove.values():
                    should_keep_shape = False  #이미 써먹은 블록이면 pass
                    break  
            
            #print("해당 shape는 없는 블럭이네 ", shape, "이미 쓴 블록에 없네:", block_to_remove)
            if should_keep_shape==True:
                remained_block.append(shape)  #안 써먹은 블록이면 넣기
            #print("남은 블럭들: ", remained_block)
            print("\n")
        #print("남은 블럭들: ", remained_block)  


        for blocks in remained_block:
            if len(remained_block) == 1:
                draw_board(screen, cur_board)
                pygame.display.flip()
                board_empty_pos = []
                board_empty_pos.append((x, y))
                find_empty_block(cur_board, board_empty_pos, x, y, W, H)
                print("좌표 확인됌")
                print(len(board_empty_pos), len(blocks[0]), "\n")
                print(blocks[0])
                #pygame.time.wait(15)
                if len(board_empty_pos) == len(blocks[0]):
                    x_min = 99
                    y_min = 99
                    print("1차 통과")
                    #pygame.time.wait(300)
                    for pos in range(len(board_empty_pos)):
                        pos_list = board_empty_pos[pos]
                        if pos_list[0] < x_min:
                            x_min = pos_list[0]
                        if pos_list[1] < y_min:
                            y_min = pos_list[1]
                    for pos in range(len(board_empty_pos)):
                        pos_list = list(board_empty_pos[pos])
                        pos_list[0] -= x_min
                        pos_list[1] -= y_min
                        board_empty_pos[pos] = tuple(pos_list)
                    board_empty_pos.sort(key = lambda x:(x[0], x[1]))
                    print(board_empty_pos)
                    #pygame.time.wait(10000)
                    for cover in blocks:
                        flag = True
                        for i in range(len(cover)):
                            if cover[i] != board_empty_pos[i]:
                                flag = False
                                print("형님 좌표가 틀렸다는데요? 냅둬 좋은 꿈 꾸나보지")
                                print(cover[i], board_empty_pos[i], "\n")
                                #pygame.time.wait(1000)
                                break
                        if flag:
                            print("에에엥 여기까지 왔는데 왜 안되는겨")
                            print(cover, "  ", board_empty_pos)
                            new_board = [row[:] for row in cur_board]
                            first_x, first_y = cover[0]
                            print(first_x, first_y)
                            for dx, dy in cover:
                                #diff_x, diff_y = dx - first_x, dy - first_y
                                #nx, ny = x + diff_x, y + diff_y
                                nx, ny = x+ dx - first_y, y + dy - first_x
                                new_board[ny][nx] = level + block_num2
                                nx, ny
                            Q.append((new_board, level, remained_block, block_num2+1))  #새로운 상태의 보드를 생성하여 큐에 추가하기
                            draw_board(screen, new_board)
                            message = "해답 발견"
                            message_surface = font.render(message, True, (0, 0, 0))  # 메시지 Surface 생성
                            tw, th = message_surface.get_size()
                            tw_center = tw//2
                            th_center = th//2
                            sw, sh = screen.get_size() #생성된 스크린의 x y의 중앙값 추출
                            sw_center = sw // 2 #x축 센터
                            sh_center = sh // 2 #y축 센터
                            screen.blit(message_surface, (sw_center - tw_center, sh_center - th_center))

                            pygame.display.flip()

                            pygame.time.wait(3000)  # 0.5초 대기'''
                            return
            else:
                for cover in blocks:
                #for i in range(len(blocks)):
                    #for j in range(4):
                        #cover = block[(i*4) + j]
                    flag = True
                    first_x, first_y = cover[0]
                    for dx, dy in cover:
                        #diff_x, diff_y = dx - first_x, dy - first_y
                        #nx, ny = x + diff_x, y + diff_y
                        nx, ny = x + dx - first_y, y + dy - first_x
                        if nx < 0 or nx >= W or ny < 0 or ny >= H:   #범위 밖이라면
                            flag = False
                            break
                        elif cur_board[ny][nx] != 0:    #이미 그 자리에 차있다면
                            flag = False
                            break 
                    if flag:    #넣을 수 있다고 판단했다면
                        new_board = [row[:] for row in cur_board]   #원본 cur_board를 수정하지 않고 복사하고,
                        #new_block = copy.deepcopy(cur_block)
                        #a = []
                        #new_block[i] = 1
                        first_x, first_y = cover[0]
                        for dx, dy in cover:
                            #diff_x, diff_y = dx - first_x, dy - first_y
                            #nx, ny = x + diff_x, y + diff_y
                            nx, ny = x + dx - first_y, y + dy - first_x
                            new_board[ny][nx] = level + block_num2
                        

                        Q.append((new_board, level, remained_block, block_num2+1))  #새로운 상태의 보드를 생성하여 큐에 추가하기
                        draw_board(screen, new_board)
                        pygame.display.flip()

                        #pygame.time.wait(20)  # 0.5초 대기
                    
                
                #if count != 0:
                #    break
            #else:
                #answer.clear()
        '''a=[]
        for dx, dy in cover:
            nx, ny = x + dx, y+ dy
            a.append((ny, nx))
        answer.append(a)'''
    print("발견 실패!")
    message = "발견 실패!"
    message_surface = font.render(message, True, (0, 0, 0))  # 메시지를 렌더링하여 Surface 생성
    screen.blit(message_surface, message_pos)  # 메시지 Surface를 화면에 그리기
    pygame.display.flip()
    return board
        
def find_empty_block(cur_board, board_empty_pos, x, y, W, H):
    board_dx = [-1, 0, 1, 0]
    board_dy = [0, -1, 0, 1]
    for i in range(len(board_dx)):
        nx, ny = x + board_dx[i], y + board_dy[i]
        if nx < 0 or nx >= W or ny < 0 or ny >= H:
            continue
        if cur_board[ny][nx] == 0:
            flag = True
            for i in range(len(board_empty_pos)):
                if nx == board_empty_pos[i][0] and ny == board_empty_pos[i][1]:
                    flag = False
            if flag:
                board_empty_pos.append((nx, ny))
                print((nx, ny))
                find_empty_block(cur_board, board_empty_pos, nx, ny, W, H)
    return 

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