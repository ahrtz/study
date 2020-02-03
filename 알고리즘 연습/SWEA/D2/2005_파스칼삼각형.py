a= int(input())
for i in range(a):
    line = int(input())
    li=[[1],[1,1]]
    cnt=0
    while cnt<line:

        if line == 1  :
            li = [[1]]
            cnt+=1
        elif line == 2 :
            li=[[1],[1,1]]
            cnt+=1
        else:
            for k in range(3,line+1):
                tmp = [1]
                for j in range(1,k-1):
                    tmp.append(li[-1][j-1]+li[-1][j])
                tmp.append(1)
                li.append(tmp)
            cnt+=1
    print(li)
