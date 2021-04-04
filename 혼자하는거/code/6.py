def countPerms(n):
    # Write your code here
    if n==1:
        return 5
    temp=[1,1,1,1,1]
    cnt=1
    while cnt<n:
        cnt+=1
        temp2=[0,0,0,0,0]
        temp2[0]=temp[1]+temp[2]+temp[4]
        temp2[1]=temp[0]+temp[2]
        temp2[2]=temp[1]+temp[3]
        temp2[3]=temp[2]
        temp2[4]=temp[2]+temp[3]
        temp=temp2[:]
    res=sum(temp)

    return res%((10**9)+7)