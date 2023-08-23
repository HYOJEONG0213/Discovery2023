import pygame

def draw_board(screen, board):
    screen.fill((255, 255, 255))  # 화면을 흰색으로 채우기

    board_block_size = 40  # 각 블록의 크기
    border_size = 2  # 테두리 크기


    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            rect = pygame.Rect(x * board_block_size, y * board_block_size + 50, board_block_size, board_block_size)
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
        color = (255, 182, 193)    #핑크색 (빨강 성분) <- hover
    else:
        color = (255, 255, 255)
    return color

def draw_block(screen, block_list, H, color_num):
    sw, sh = screen.get_size() #생성된 스크린의 x y의 중앙값 추출
    #sw_center = sw // 2 #x축 센터
    sh_center = sh // 2 #y축 센터

    block_info = []
    block_size = 25  # 블록의 크기
    border_size = 2  # 테두리 크기
    start_x = 0  # 블록들의 모양 시작 X 좌표
    start_y = H * 60  + block_size*2 # 블록들의 모양 시작 Y 좌표
    spacing = 5  # 블록들 간의 간격

    for idx, block in enumerate(block_list):

        x_avg, y_avg = 0, 0
        for x, y in block:
            if x_avg < x:
                x_avg = x
            if y_avg < y:
                y_avg = y
        x_avg = (x_avg + 1) / 2
        y_avg = (y_avg + 1) / 2

        if idx % 3 == 2:
            start_x = (sw/4)*3 - (x_avg * (block_size + spacing))

        elif idx % 3 == 1:
            start_x = (sw/4)*2 - (x_avg * (block_size + spacing))

        else:
            start_x = sw/4 - (x_avg * (block_size + spacing))

        for x, y in block:
            rect = pygame.Rect(start_x + (x * (block_size + spacing)),
                           start_y + (y * block_size + spacing) - (y_avg * (block_size + spacing)),
                           block_size, block_size)
            inner_rect = pygame.Rect(rect.left + border_size, rect.top + border_size,
                                 rect.width - 2 * border_size, rect.height - 2 * border_size)
            color = select_color(color_num)

            pygame.draw.rect(screen, color, inner_rect)     # 블록 내부 그리기
            pygame.draw.rect(screen, (255,255,255), rect, border_size)  # 블록 테두리 그리기

            block_info.append({"color_num":color_num, "rect":rect})
        
        if idx % 3 == 2:
            start_y += sh/(len(block_list)) + (block_size/2)*3

        color_num +=1
    return block_info