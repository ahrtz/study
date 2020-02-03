def queen(a,N):
    # 맨처음 퀸의 위치(a)를 주어주고 시작 
    # 될수 있는것들 
    global cnt
    if len(a)==N:
        cnt+1
        return 0 
 
        candidate = list(range(n)) # 0부터 n-1까지를 후보 배열로 만든다.
        for i in range(len(sol)):
            if sol[i] in candidate: # 같은 열에 있는 지 확인
                candidate.remove(sol[i]) # 같은 열에 있다면 후보에서 제외
            distance = len(sol) - i
            if sol[i] + distance in candidate: # 같은 대각성 상(+)에 있는 지 확인
                candidate.remove(sol[i] + distance) # 같은 대각선 상에 있다면 후보에서 제외
            if sol[i] - distance in candidate: # 같은 대각선 상(-)에 있는 지 확인
                candidate.remove(sol[i] - distance) # 같은 대각선 상에 있다면 후보에서 제외
            if candidate != []:
                for i in candidate:
                    sol.append(i) # 후보의 요소를 정답 배열의 i+1로 추가
                    nqueen(sol, n) # 재귀적으로 다음 행도 확인
            else:
                return 0



            

T= int(input())

for tc in range(1,T+1):
    N = int(input())
    cnt = 0
    pan = [[0]*N for _ in range(N)]
    for i in range(N): # 이제 가로로 진행한다. 


        











            
            #     for k in range(4):
            #         for l in range(1,N,1):
            #             new_i = i+dx[k]*l
            #             new_j = j+dy[k]*l
                        
            #             if 0<=new_i<=N-1 and 0<=new_j<=N-1 and pan[new_i][new_j]==0:
                            
            #                 locate_row.append(i)
            #                 locate_col.append(j)
            #                 pan[i][j]=1
            #                 print("###{}{}".format(i,j))
            #                 print(new_i,new_j)
    print(pan)                        
    
                            
    # print("#{} {}".format(tc,cnt))



