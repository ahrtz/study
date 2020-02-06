import itertools
n,m,d = 5,5,3
castle = [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[0,0,0,1,1],[1,1,0,1,0]]

# for i in range(n):
#     tmp = list(map(int,input().split()))
#     castle.append(tmp)

# 궁수 배치 배열했다 치고

a=castle[-1].index(1)
b=castle[-1].index(1,a+1)
c=castle[-1].index(1,b+1)
nu=[a,b,c]
#궁수 인덱스 뺏다.
cnt=0
#궁수한개만 해보자 
saguri=[]
for k in nu:
    
    for i in range(n):#행 n
        tmp=[]
        for j in range(m): # 열 M
            dis=1
            while dis <= d:
                if castle[i][j]==1 and abs(n-i)+abs(k-j)<=dis:
                    saguri.append((i,j,dis,k))
                    break
                dis +=1
                print(dis)





            # for dis in range(1,d+1):

                # if castle[i][j]==1 and abs(n-i)+abs(k-j)<=dis:
                #     saguri.append((i,j,dis,k))
                #     break
                         
                # for dis in range(1,d+1):
                #     dsav=abs(n-i)+abs(k-j)
                    
                #     if dsav==dis and (i,j) not in saguri and (i,j) not in tmp:
                #         tmp.append((i,j,dsav))
                        
                    

                    
print(saguri)

