def solution(s):
    answer = []
    moon = ''
    arr = []
    arr2 = []
    # 문자열 배열로 파싱
    for ss in range(1,len(s) -1):
        if s[ss] == '{':
            arr2 = []
        if ss == len(s) - 2:
            arr2.append(moon)
        if s[ss].isdigit():
            moon += s[ss]
        if s[ss] == ',' and s[ss] != '':
            arr2.append(moon)
            moon = ''
        if s[ss] == '}':
            arr.append(arr2)
    # 정렬
    arr.sort(key= lambda x:len(x))

    for ss in arr:
        for sss in ss:
            if int(sss) not in answer:
                answer.append(int(sss))
    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))