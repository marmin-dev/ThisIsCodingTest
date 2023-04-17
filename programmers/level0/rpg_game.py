def solution(keyinput, board):
    loc = [0,0]
    board = [int(board[0]/2), int(board[1]/2)]
    for move in keyinput:
        if move == "left" and -1 * board[0] <= loc[0]:
            loc[0] = loc[0] - 1
        elif move == "right" and board[0] >= loc[0]:
            loc[0] = loc[0] + 1
        elif move == "up" and board[1] >= loc[1]:
            loc[1] = loc[1] + 1
        elif move == "down" and -1 * board[1] <= loc[1]:
            loc[1] -= loc[1] - 1
    return loc

print(solution(["left", "right", "up", "right", "right"],[11, 11]))