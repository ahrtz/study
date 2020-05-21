from collections import deque
def solution(land):
    land = deque(land)
    while len(land)>1:
        tmp=land.popleft()
        for i in range(4):
            tmp1=[]
            for j in range(4):
                if i==j:
                    continue
                else:
                    tmp1.append(land[0][i]+tmp[j])
            land[0][i]=max(tmp1)
    
    
    



    return max(list(land[0]))
land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
print(solution(land))