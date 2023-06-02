from collections import deque
def solution(people, limit):
    answer = 0
    people = deque(sorted(people))
    while people:
        if len(people) == 1:
            people.pop()
            answer += 1
            break
        if people[-1] + people[0] <= limit:
            people.pop()
            people.popleft()
            answer += 1
        else:
            people.pop()
            answer += 1
    return answer