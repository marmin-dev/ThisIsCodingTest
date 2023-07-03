def solution(board, moves):
    col = []
    stack = []
    answer = 0
    # 세로로 정리하기
    for i, a in enumerate(board[0]):
        col.append([a[i] for a in board if a[i] != 0])

    # moves 대로 뽑기
    for a in moves:
        if col[a - 1]:
            move = col[a - 1].pop(0)
            if stack and stack[-1] == move:
                stack.pop()
                answer += 2
            else:
                stack.append(move)
        else:
            pass
    return answer