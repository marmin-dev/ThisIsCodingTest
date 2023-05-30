def solution(n, words):
    # p 는 단어의 첫번째 첫 알파벳
    p = [words[0][0]]
    # 인덱스 i, 단어
    for i, w in enumerate(words):
        # 만약 단어가 p에 없고 단어의 첫번째가 마지막과 같다면
        if w not in p and p[-1][-1] == w[0]:
            # 단어를 추가한다
            p.append(w)
        else:
            # 아니라면 i를 n으로 나눈값 + 1 그리고, 인덱스를 n으로 나눈 몫 + 1
            return [i % n + 1, (i//n)+1]
    return [0, 0]