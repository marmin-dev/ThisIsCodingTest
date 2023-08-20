def element(str1):
    arr1 =[]
    for i, s in enumerate(str1):
    # 교집합 구하기
        if i != len(str1) -1 :
            if str1[i].isalpha() or str1[i].isdigit():
                if str1[i + 1].isalpha() or str1[i + 1].isdigit():
                    arr1.append(str1[i]+str1[i + 1])
    return arr1

def solution(str1, str2):
    answer = 65536
    str1 = str1.lower()
    str2 = str2.lower()
    arr1 = element(str1)
    arr2 = element(str2)
    # 합집합을 만들기 위한 Set 생성
    str_set = set()
    str_same = []
    for s in arr1:
        str_set.add(s)
    for s in arr2:
        str_set.add(s)
    # 교집합 만들기
    for a in arr1:
        if a in arr2:
            str_same.append(a)
    str_same = set(str_same)
    if len(str_same) != 0:
        answer = 65536 * (len(str_same)/len(str_set))

    return int(answer)

print(solution("FRANCE", "french"))