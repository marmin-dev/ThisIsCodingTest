def solution(name, yearning, photo):
    answer = []
    name_dict = {}
    for i in range(len(name)):
        name_dict[name[i]] = yearning[i]
    for a in photo:
        counter = 0
        for b in a:
            if b in name_dict.keys():
                counter += name_dict[b]
        answer.append(counter)
    return answer