def solution(s):
    answer = []
    c_z = 0
    count = 0
    while s != '1':
        zero = s.count('0')
        c_z += zero
        leng = len(s) - zero
        binary=bin(leng)
        s = binary.split('b')[1]
        print(s)
        count += 1
    answer.append(count)
    answer.append(c_z)
    return answer

print(solution("110010101001"))
binary = bin(len("110010101001"))
print(binary)