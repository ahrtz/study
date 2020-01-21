a = int(input())
cnt= 0
lis=[]
while cnt<a:
    k =list(map(int,input().split())) 
    lis.append(k)
    cnt+=1


for i in lis:
    rank = 1
    for j in lis:
        if i[0] < j[0] and i[1] < j[1]:
                rank += 1
    print(rank, end=" ")