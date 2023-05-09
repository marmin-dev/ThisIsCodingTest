def solution(n, arr1, arr2):
    answer = []
    decode1 = []
    decode2 = []
    for a in arr1:
        bina = bin(a)
        ar1 = bina.split("b")
        if len(ar1[1]) < n:
            tar_ar = "0" * (n - len(ar1[1])) + ar1[1]
            decode1.append(tar_ar)
        else:
            tar_ar = ar1[1]
            decode1.append(tar_ar)
    for a in arr2:
        bina = bin(a)
        ar2 = bina.split("b")
        if len(ar2[1]) < n:
            tar_ar = "0" * (n - len(ar2[1])) + ar2[1]
            decode2.append(tar_ar)
        else:
            tar_ar = ar2[1]
            decode2.append(tar_ar)
    for a in range(len(decode1)):
        ans_str = ''
        for b in range(len(decode1[a])):
            if decode1[a][b] == "1" or decode2[a][b] == "1":
                ans_str += '#'
            else:
                ans_str += ' '
        answer.append(ans_str)
    return answer



print(solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]))