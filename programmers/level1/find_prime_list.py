def solution(nums):
    answer = 0
    for a in range(len(nums)-2):
        for b in range(a + 1,len(nums)-1):
            for c in range(b + 1,len(nums)):
                count = 0
                pnum = nums[a] + nums[b] + nums[c]
                for d in range(1, pnum + 1):
                    if pnum % d == 0:
                        count += 1
                    elif count > 2:
                        break
                if count == 2:
                    answer += 1
    return answer


print(solution([1,2,7,6,4]))
#print(solution([1,2,3,4]))