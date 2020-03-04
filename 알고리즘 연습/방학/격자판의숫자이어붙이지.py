def move(r1,c1,cn,n):
    global ans_list
    if cn == 7:
        ans_list.add(n)
        
    else: 
        for k in range(4):
            newr = r1+d[k][0]
            newc = c1 + d[k][1]
            if 0<=newr<4 and 0<=newc<4:
                move(newr,newc,cn+1,n+pan[newr][newc])


T=int(input())
for tc in range(T):
    pan=[list(map(str,input().split())) for _ in range(4)]
    ans_list=set()
    d= [(0,1),(1,0),(-1,0),(0,-1)]
    
    for r in range(4):
        for c in range(4):
            move(r,c,0,"")
    print("#{} {}".format(tc+1,len(ans_list)))
