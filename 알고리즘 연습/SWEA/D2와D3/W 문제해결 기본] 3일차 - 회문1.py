def ok(n):
    if n==n[::-1]:
        return True
    else:
        return False

for tc in range(10):
    a=int(input())
    pan=[]
    for _ in range(8):
        tmp=list(input())
        pan.append(tmp)
    #가로검색
    cnt=0
    for row in range(0,len(pan)):
        for col in range(0,len(pan)-a+1):
            if ok(pan[row][col:col+a]):
                cnt += 1
                # print(pan[row][col:col+4])
    #세로로 판돌리기
    npan=[] 
    for ccol in range(0,len(pan)):
        tmp=[]
        for rrow in range(0,len(pan)):
            tmp.append(pan[rrow][ccol])
        npan.append(tmp)
    
    for row in range(0,len(pan)):
        for col in range(0,len(pan)-a+1):
            if ok(npan[row][col:col+a]):
                cnt += 1
                # print(npan[row][col:col+4])
                # print(row,col)    
            
    print("#{} {}".format(tc+1,cnt))

