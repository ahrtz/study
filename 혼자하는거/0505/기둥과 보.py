from pprint import pprint 
## 제거를 다시해야댐
def solution(n, build_frame):
    pan=[[0]*(n+1) for _ in range(n+1)]
    answer = []
    for frame in build_frame:
        ## 바닥에 기둥 설치
        if frame[1]==0 and frame[2]==0 and frame[3]==1:
            pan[frame[0]][frame[1]]+=10
            pan[frame[0]][frame[1]+1]+=10
        ## 그냥 기둥 설치
        elif frame[2]==0 and frame[3]==1:
            if pan[frame[0]][frame[1]]//10>=1 or pan[frame[0]][frame[1]]%10>=2: # 왼쪽에 보 있거나 아래에 기둥있거나
                pan[frame[0]][frame[1]]+=10
                pan[frame[0]][frame[1]+1]+=10
                
        ## 보 설치 
        elif frame[1]!=0 and frame[2]==1 and frame[3]==1: ##  아래에 기둥 왼쪽보 
            if pan[frame[0]][frame[1]]//10>=1 or pan[frame[0]][frame[1]]%10>=2 :
                pan[frame[0]][frame[1]]+=2
                pan[frame[0]+1][frame[1]]+=2
        
        # 이제 제거 해야댐 기둥제거
        elif frame[2]==0 and frame[3]==0:
            if pan[frame[0]][frame[1]+1]%10>=2: # 양측에서 지지 대고 있으면(한쪽에서만 지지대도 괜찮음)
                pan[frame[0]][frame[1]]-=10
                pan[frame[0]][frame[1]+1]-=10
            elif pan[frame[0]][frame[1]]%10==0 and pan[frame[0]][frame[1]+1]//10<2 : # 기둥만 서있는거 
                pan[frame[0]][frame[1]]-=10
                pan[frame[0]][frame[1]+1]-=10
            elif frame[1]==0:
                if pan[frame[0]][frame[1]+1]//10==1: # 바닥이 기둥인거+ 위에 아무것도 없음 
                    pan[frame[0]][frame[1]]-=10
                    pan[frame[0]][frame[1]+1]-=10


        # 보 제거
        elif frame[2]==1 and frame[3]==0:
            if pan[frame[0]][frame[1]]//10 >=1 and pan[frame[0]+1][frame[1]]//10 >=1:
                pan[frame[0]][frame[1]]-=2
                pan[frame[0]+1][frame[1]]-=2
            elif pan[frame[0]][frame[1]]%10>3 and pan[frame[0]-1][frame[1]]//10>1 and pan[frame[0]+1][frame[1]]%10>3 and pan[frame[0]+2][frame[1]]//10>1:
                pan[frame[0]][frame[1]]-=2
                pan[frame[0]+1][frame[1]]-=2

    pprint(pan)
    for i in range(len(pan)):
        for j in range(len(pan)):
            if pan[i][j]>=10:
                answer.append([i,j,0])
                pan[i][j]-=10
                pan[i][j+1]-=10
            if pan[i][j]%10>1:
                answer.append([i,j,1])
                pan[i][j]-=2
                pan[i+1][j]-=2


    
    return answer
build_frame=	[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
n=5
print(solution(n,build_frame))