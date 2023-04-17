def solution(numbers):
    answer = 0
    alp = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    ll = []
    al = []
    for e in numbers:
        al.append(e)
        az = ''.join(e)
        if az in alp and az != '':
            for i, b in enumerate(alp):
                if al == b:
                    ll.append(str(i))
    answer = ''.join(ll)
    answer = int(answer)


    return answer
print(solution("onetwothreefourfivesixseveneightnine"))