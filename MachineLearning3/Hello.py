# 八皇后问题
import numpy as np
import sys


def next_valid_col(current_queen_pos, board_size, total_queen):
    valid_col = []
    for i in range(board_size):
        period = np.arange(total_queen)
        if (i not in current_queen_pos[period, 1]) and ((total_queen + i) not in (current_queen_pos[period, 0] + \
            current_queen_pos[period, 1])) and ((total_queen - i) not in (current_queen_pos[period, 0] - \
            current_queen_pos[period, 1])):
            valid_col.append(i)
    return valid_col


def dict_last_none_empty(dicts):
    keys = dicts.keys()
    return_key = -1
    for key in keys:
        length = len(dicts[key])
        if length != 0:
            return_key = key
    return return_key


def explore_queen(current_queen_pos, board_size, total_queen, explore_field, num_ans):
    if total_queen == 0:
        explore_field = {0: [0, 1, 2, 3, 4, 5, 6, 7]}
        current_queen_pos[0] = [0, explore_field[0].pop(0)]
        total_queen = 1
        explore_field[total_queen] = next_valid_col(current_queen_pos, board_size, total_queen)
        print('Placing first queen')
        print(current_queen_pos, total_queen, explore_field)
        explore_queen(current_queen_pos, board_size, total_queen, explore_field, num_ans)
    elif dict_last_none_empty(explore_field) == -1:
        print(explore_field)
        print("Finished Searching")
        print("Total solution: %d" % num_ans)
        return
    elif total_queen == board_size:
        total_queen = dict_last_none_empty(explore_field)
        next_queen_pos = explore_field[total_queen].pop(0)
        current_queen_pos[total_queen + 1:, :] = 0
        current_queen_pos[total_queen] = [total_queen, next_queen_pos]
        total_queen += 1
        num_ans += 1
        explore_field[total_queen] = next_valid_col(current_queen_pos, board_size, total_queen)
        print("solution count: %d" % num_ans)
        print(current_queen_pos, total_queen, explore_field)
        explore_queen(current_queen_pos, board_size, total_queen, explore_field, num_ans)
    elif (len(explore_field[total_queen]) == 0) and (total_queen < board_size):
        total_queen = dict_last_none_empty(explore_field)
        next_queen_pos = explore_field[total_queen].pop(0)
        current_queen_pos[total_queen + 1:, :] = 0
        current_queen_pos[total_queen] = [total_queen, next_queen_pos]
        total_queen += 1
        explore_field[total_queen] = next_valid_col(current_queen_pos, board_size, total_queen)
        print("Going back")
        print(current_queen_pos, total_queen, explore_field)
        explore_queen(current_queen_pos, board_size, total_queen, explore_field, num_ans)
    else:
        next_queen_pos = explore_field[total_queen].pop(0)
        current_queen_pos[total_queen] = [total_queen, next_queen_pos]
        total_queen = total_queen + 1
        explore_field[total_queen] = next_valid_col(current_queen_pos, board_size, total_queen)
        print("Placing Next Queen")
        print(current_queen_pos, total_queen, explore_field)
        explore_queen(current_queen_pos, board_size, total_queen, explore_field, num_ans)


BoardSize = 8
sys.setrecursionlimit(1000000)
Initial_queen_pos = np.zeros([BoardSize, 2])
explore_queen(Initial_queen_pos, BoardSize, 0, {}, 0)
