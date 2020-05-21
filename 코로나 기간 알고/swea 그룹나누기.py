T=int(input())
for tc in range(T):
    N,M= map(int,input().split())
    pair_list=list(map(int,input().split()))

    cnt=1
    
    team=[0]*(N+1)

    for i in range(M):
        if team[pair_list[2*i]]==0 and team[pair_list[(2*i)+1]] == 0:
            team[pair_list[2*i]]=cnt
            team[pair_list[(2*i)+1]]=cnt
            cnt+=1
        elif team[pair_list[2*i]]!=0 and team[pair_list[(2*i)+1]] == 0:
            team[pair_list[(2*i)+1]]=team[pair_list[2*i]]
        elif team[pair_list[2*i]]==0 and team[pair_list[(2*i)+1]] != 0:
            team[pair_list[2*i]]=team[pair_list[(2*i)+1]]
        else:# 둘이 다른 그룹에 이미 속해 있을때 
            a_cnt=team.count(team[pair_list[2*i]])# 앞에꺼 갯수
            print(a_cnt,'%')
            tmp_val=team[pair_list[2*i]]
            for n in range(a_cnt):
                a_idx=team.index(tmp_val)# 앞 팀원들의 인덱스를 찾아서 뒷조에 다 편입 
                team[a_idx]=team[pair_list[(2*i)+1]]


    # len(set(team))-1 <- 0번 팀을 제외 한 팀의 갯수 
    # team.count(0)-1 <- 맨 앞 빈 인덱스 0 이 있기 때문에 빼줌 
    print(f'#{tc+1} {len(set(team))-1+team.count(0)-1}')

    
    
