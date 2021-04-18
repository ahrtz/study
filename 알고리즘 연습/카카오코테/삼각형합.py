
def solution(triangle):
  
    answer = 0
    for i in range(1,len(triangle)): # 행 번호
        for j in range(i+1):   # 열번호
            if j==0:
                triangle[i][j]+= triangle[i-1][j]
            elif j==i:
                triangle[i][j]+= triangle[i-1][j-1]
            else:
                triangle[i][j]+= max(triangle[i-1][j],triangle[i-1][j-1])


    # sumtriange(triangle,0,0,triangle[0][0])
    return max(triangle[-1])


# def sumtriange(tri,idx,cnt,hap):
#     global summax
#     if cnt==len(tri)-1:
        
#         if hap>summax:
#             summax=hap
#         return hap - tri[cnt][idx]
#     if idx==len(tri):
#         return
#     sumtriange(tri,idx,cnt+1,hap+tri[cnt][idx])
#     sumtriange(tri,idx+1,cnt+1,hap+tri[cnt][idx+1])
    


solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])