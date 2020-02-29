import itertools
T=int(input())
for tc in range(T):
    N,M,C = map(int,input().split()) # N : 가로길이 M : 벌통크기 c: 벌통용량
# print(pan)
    pan = [list(map(int,input().split())) for _ in range(N)]
    result=0
    for r in range(N):
        for c in range(N-M+1):
            # 시작점 위치 픽
            for r1 in range(N):
                for c1 in range(N-M+1):
                    con1 = []
                    con2 = []
                    #두번째 시작점 위치 픽 예외주기
                    if r==r1 and ((c-M+1)<=c1<=(c+M-1)):
                        continue
                    else:
                        #각 조합의 시작점 뽑았음 여기서 부터 계산
                        # print((r,c),(r1,c1))
                        
                        for i in range(M):
                            con1.append(pan[r][c+i])
                            con2.append(pan[r1][c1+i])
                        cnt1 = 0
                        cnt2 = 0
                        for l in range(1,len(con1)+1):
                            tmp1 = list(itertools.combinations(con1,l))
                            for tmp in range(len(tmp1)):
                                if sum(tmp1[tmp])<=C:
                                    tmp_cnt=0
                                    for ttmp in range(len(tmp1[tmp])):
                                        tmp_cnt += tmp1[tmp][ttmp]**2
                                    if tmp_cnt>=cnt1:
                                        cnt1=tmp_cnt
                                        # print(tmp1[tmp])
                        for l in range(1,len(con2)+1):
                            tmp2 = list(itertools.combinations(con2,l))
                            for tmp in range(len(tmp2)):
                                if sum(tmp2[tmp])<=C:
                                    tmp_cnt2=0
                                    for ttmp in range(len(tmp2[tmp])):
                                        tmp_cnt2 += tmp2[tmp][ttmp]**2
                                        
                                    if tmp_cnt2>=cnt2:
                                        cnt2=tmp_cnt2
                        if result < cnt1+cnt2:
                            result = cnt1+cnt2
    print("#{} {}".format(tc+1,result))