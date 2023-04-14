array = [3,5,1,2,4] # 5개의 데이터(N =5)
summary = 0

# 모든 데이터를 하나씩 확인하며 합계를 계산
for x in array:
    summary += x

# 결과를 출력
print(summary)
# => 즉 이 알고리즘은 O(N)의 복잡도를 가진다.