cur_board = [[1, 2, 0, 0, 0, 0, 1],
             [1, 2, 3, 0, 0, 0, 1],
             [1, 0, 3, 3, 1, 1, 1]]

block_to_remove = {}


for i in range(3):
    for j in range(7):
        if cur_board[i][j] !=0 and cur_board[i][j] !=1:         #중복 블록 확인하기
            if cur_board[i][j] not in block_to_remove:
                block_to_remove[cur_board[i][j]] = []
            block_to_remove[cur_board[i][j]].append((j, i))

for block_num, coords_list in block_to_remove.items():
    min_x = min(x for x, y in coords_list)
    min_y = min(y for x, y in coords_list)

    shifted_coords = [(x - min_x, y - min_y) for x, y in coords_list]
    min_x = min(x for x, y in shifted_coords)
    min_y = min(y for x, y in shifted_coords)

    updated_coords_list = [(x - min_x, y - min_y) for x, y in shifted_coords]
    block_to_remove[block_num] = updated_coords_list


print(block_to_remove)