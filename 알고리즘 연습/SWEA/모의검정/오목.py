T= int(input())
case = []
pan=[[0 for _ in range(19)] for _ in range(19)]
flag=12
for _ in range(T):
    case.append(list(map(int,input().split())))
for n in range(len(case)):
    new_row=case[n][0]-1
    new_col=case[n][1]-1
    pan[new_row][new_col]=(n%2)+1
    a=pan[new_row]
    # 가로 통으로 뽑기 
    for i in range(len(pan)-5):
        if len(set(a[i:i+6]))==1  :
            continue
        elif len(set(a[i:i+5]))==1 and (1 in set(a[i:i+5]) or 2 in set(a[i:i+5])):
            print(n+1)
            flag=15
            break
    #세로 통으로 뽑기
    tmp=[]
    for row in range(19):
        tmp.append(pan[row][new_col])
    b=tmp
    for i in range(len(pan)-5):
        if  len(set(b[i:i+6]))==1:
            continue
        elif len(set(b[i:i+5]))==1 and (1 in set(b[i:i+5]) or 2 in set(b[i:i+5])):
            print(n+1)
            flag=15
            break
    #대각 통으로 뽑기
    tmp1=[]
    l=0
    while l<36:
        k = list(range(-18,18))
        if 0<=new_row+k[l]<19 and 0<=new_col+k[l]<19:
            tmp1.append(pan[new_row+k[l]][new_col+k[l]])
        l += 1

    for i in range(len(tmp1)-5):
        if  len(set(tmp1[i:i+6]))==1:
            continue
        elif len(set(tmp1[i:i+5]))==1 and (1 in set(tmp1[i:i+5]) or 2 in set(tmp1[i:i+5])):
            print(n+1)
            flag=15
            break

    tmp2=[]
    l=0
    while l<36:
        k = list(range(-18,18))
        if 0<=new_row-k[l]<19 and 0<=new_col+k[l]<19:
            tmp2.append(pan[new_row-k[l]][new_col+k[l]])
        l += 1

    for i in range(len(tmp2)-5):
        if len(set(tmp2[i:i+6]))==1:
            continue
        elif len(set(tmp2[i:i+5]))==1 and (1 in set(tmp2[i:i+5]) or 2 in set(tmp2[i:i+5])):
            print(n+1)
            flag=15
            break
    
if flag==12:
    print(-1)













    # for k in range(0,5): # 가로검사
        
    #     if 0<= new_col-4+k and new_col+k<19:
    #         tmp.append(pan[new_row][new_col-4+k:new_col+k+1])
    #     if 0<= new_col-4+k and new_col+k<19 and 0<= new_row-4+k and new_row+k<19 :# 우측아래 대각
    #         tmp.append([pan[new_row-4+k][new_col-4+k],pan[new_row-3+k][new_col-3+k],pan[new_row-2+k][new_col-2+k],pan[new_row-1+k][new_col-1+k],pan[new_row+k][new_col+k]])
    #     if 0<= new_col-4+k and new_col+k<19 and 0<= new_row-4+k and new_row+k<19:# 좌측위 대각
    #         tmp.append([pan[new_row+k][new_col-4+k],pan[new_row-1+k][new_col-3+k],pan[new_row-2+k][new_col-2+k],pan[new_row-3+k][new_col-1+k],pan[new_row-4+k][new_col+k]])
    #     if 0<= new_row-4+k and new_row+k<19:
    #         tmp.append([pan[new_row-4+k][new_col],pan[new_row-3+k][new_col],pan[new_row-2+k][new_col],pan[new_row-1+k][new_col],pan[new_row+k][new_col]])
    # print(i,tmp)


# pprint.pprint(pan)
    
