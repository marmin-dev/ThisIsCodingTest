def sequential_search( target, array):
    # 각 원소를 하니씩 확인하며
    for i in range(len(array)):
        # 현재의 원소가 찾고자 하는 원소와 동일한 경우
        if array[i] == target:
            return i + 1

print(sequential_search(4,[1,3,6,7,3,2,4,5,7,8,9,3,2]))