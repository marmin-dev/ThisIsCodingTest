def solution(name):
    answer = 0
    name_len = len(name)
    moves = [min(ord(char) - ord('A'), ord('Z') - ord(char) + 1) for char in name]  # 각 알파벳 이동 횟수

    # 첫 번째 문자부터 탐색하여 이동 횟수 계산
    current_index = 0
    while True:
        answer += moves[current_index]
        moves[current_index] = 0  # 이동한 문자는 이동 횟수를 0으로 설정

        # 모든 문자가 완성되었으면 반복 종료
        if sum(moves) == 0:
            break

        # 다음으로 이동할 위치를 결정하는 로직 추가
        left = 1
        right = 1

        # 다음 이동할 위치가 0이 아닌 값일 때까지 왼쪽과 오른쪽으로 이동
        while moves[current_index - left] == 0:
            left += 1
        while moves[current_index + right] == 0:
            right += 1

        # 왼쪽과 오른쪽 중 이동 횟수가 적은 쪽으로 이동
        if left < right:
            answer += left
            current_index -= left
        else:
            answer += right
            current_index += right

    return answer

# 테스트 예시

