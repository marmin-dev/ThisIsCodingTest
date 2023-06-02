def solution(name):
    # 알파벳 이동 횟수 계산 함수
    def get_move_count(char):
        # 알파벳 이동 횟수를 A를 기준으로 계산
        return min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

    length = len(name)  # 이름의 길이
    move_counts = [get_move_count(char) for char in name]  # 각 알파벳에 대한 이동 횟수 리스트
    cursor = 0  # 커서의 위치
    total_moves = 0  # 총 이동 횟수

    while True:
        # 현재 커서 위치의 알파벳을 완성하기 위한 이동 횟수를 총 이동 횟수에 더함
        total_moves += move_counts[cursor]
        move_counts[cursor] = 0  # 커서 위치의 알파벳은 완성되었으므로 이동 횟수를 0으로 설정

        # 모든 알파벳이 완성되었으면 반복 종료
        if sum(move_counts) == 0:
            break

        left = 1  # 왼쪽으로 이동할 칸 수
        right = 1  # 오른쪽으로 이동할 칸 수

        # 왼쪽으로 이동할 수 있는 칸 탐색
        while move_counts[cursor - left] == 0:
            left += 1

        # 오른쪽으로 이동할 수 있는 칸 탐색
        while move_counts[cursor + right] == 0:
            right += 1

        # 왼쪽과 오른쪽 중 이동 횟수가 더 적은 방향으로 커서를 이동시키고 총 이동 횟수에 더함
        if left < right:
            cursor -= left
            total_moves += left
        else:
            cursor += right
            total_moves += right

    return total_moves

# 테스트 예시
name = "JAZ"
result = solution(name)
print(result)  # 출력: 11