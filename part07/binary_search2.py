def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

result = binary_search([1,2,3,4,5,6,7,8,9,10],7,1,10)
print(result)
