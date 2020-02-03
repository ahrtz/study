for i in range(10):
    width = int(input())
    pan=[]
    for _ in range(width):
        tmp=list(map(int,input().split()))
        pan.append(tmp)
    cnt=0
    for ii in range(100):
        temp=[]
        for j in range(100):
            if pan[j][ii]!=0:
                temp.append(pan[j][ii])
        print(temp)
        for k in range(len(temp)-1):
            if temp[k]==1 and temp[k+1]==2:
                cnt+=1

    print("#{} {}".format(i+1,cnt))
