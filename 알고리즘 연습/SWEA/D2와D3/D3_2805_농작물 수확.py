T=int(input())
for tc in range(T):
    width = int(input())
    bat=[]
    for i in range(width):
        nong = list(map(int,input()))
        bat.append(nong)
    cnt=0
    #위 절반 아래절반 쪼개자 슬라이싱으로하자
    for k in range(width//2+1): # 행고정
        # print(bat[k][width//2 -k :width//2 +1+k ])
        cnt+= sum(bat[k][width//2 -k :width//2 +1+k ])
    #아래절반
    for k in range(-1,-(width//2)-1,-1):
        # print(bat[k][width//2 +k+1 :width//2 -(1+k)+1])
        cnt+= sum(bat[k][width//2 +k+1 :width//2 -(1+k)+1])

    # for k in range(width-1,width//2,-1):
    #     print(bat[k][width//2 -(k-3) :width//2 +k-1 ])
    print("#{} {}".format(tc+1,cnt))
    