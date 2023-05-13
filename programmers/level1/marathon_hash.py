def solution(participant, completion):
    hashDict = {}
    sumHash = 0

    for part in participant:
        hashDict[hash(part)] = part
        sumHash += hash(part)
    print("s",sumHash)
    print(hashDict)
    for comp in completion:
        sumHash -= hash(comp)
    print("S",sumHash)
    return hashDict[sumHash]

print(solution(["leo", "kiki", "eden"],["eden", "kiki"]))