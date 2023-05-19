a = [1,2,5,4,3]
b = [5,5,6,6,3]

def solution(q,w,k):
    q.sort()
    w.sort(reverse=True)
    for a in range(k):
        if q[a] < w[a]:
            q[a], w[a]=w[a], q[a]
        else:
            break
    return sum(q)
print(solution(a,b,3))
