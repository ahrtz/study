T= int(input())
case = []
pan=[[0 for _ in range(21)] for _ in range(21)]
flag=12
d=[(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
for _ in range(T):
    case.append(list(map(int,input().split())))
for n in range(len(case)):
    new_row=case[n][0]
    new_col=case[n][1]
    pan[new_row][new_col]=(n%2)+1
    c=pan[new_row][new_col]
    v=[0]*8

    for l in range(len(d)):
        nnew_row=new_row+d[l][0]
        nnew_col=new_col+d[l][1]
        cnt=0
        while pan[nnew_row][nnew_col]==c:
            
            nnew_row=nnew_row+d[l][0]
            nnew_col=nnew_col+d[l][1]
            cnt+=1
                
        v[l]=cnt
    for m in range(4):
        if v[m]+v[m+4] == 4:
            flag=14
            print(n+1)
            break
    
    if flag ==14:
        break
if flag ==12:
        print(-1)







