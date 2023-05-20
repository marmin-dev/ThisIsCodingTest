def binary_s(n,li):
    if li == []:
        return None
    start = 0
    end = len(li)
    mid = (start + end) // 2
    if n == li[mid]:
        return li[mid]
    if n > li[mid]:
        return binary_s(n, li[mid + 1:])
    elif n < li[mid]:
        return binary_s(n, li[:mid - 1])
def solution(li1,li2):
    li2.sort()
    for a in li1:

        if binary_s(a, li2) == None:
            print("no")
        else:
            print("yes")
solution([5,7,9],[8,3,7,9,2])

