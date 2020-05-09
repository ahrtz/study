from collections import Counter

T=int(input())
for tc in range(T):
    num_list=list(map(int,input().split()))
    player1=[]
    player2=[]
    player1_cnt=[0]*10
    player2_cnt=[0]*10
    flag=156
    for i in range(len(num_list)//2):
        player1.append(num_list[2*i])
        player2.append(num_list[2*i+1])
        player1_cnt[num_list[2*i]]+=1
        player2_cnt[num_list[2*i+1]]+=1
        # print(player1_cnt,player2_cnt)
        for t in range(len(player1_cnt)-2):
            if player1_cnt[t] >=1 and player1_cnt[t+1]>=1 and player1_cnt[t+2]>=1:
                print(f'#{tc+1} {1}')
                flag=12
                break
        if 3 in player1_cnt:
            print(f'#{tc+1} {1}')
            break
        if 3 in player2_cnt and flag!=12:
            print(f'#{tc+1} {2}')
            break
        if flag!=12:
            for t in range(len(player1_cnt)-2):
                if player2_cnt[t] >=1 and player2_cnt[t+1]>=1 and player2_cnt[t+2]>=1:
                    print(f'#{tc+1} {2}')
                    flag=12
                    break
        if flag ==12:
            break
    else:
        print(f'#{tc+1} {0}')
