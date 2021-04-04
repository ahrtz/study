def solution(A):
    # print(sorted(A))
    tmp = sorted(A)
    cnt=0
    for i in range(len(tmp)):
        cnt+= abs(tmp[i]-(i+1))

    return cnt

A=[1,2,1]
print(solution(A))