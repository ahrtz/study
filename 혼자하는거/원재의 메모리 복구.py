a= int(input())

for j in range(a):
    dab=input()
    dab=list(dab)
    cnt=0
    start = []
    
    for k in range(len(dab)):
        start.append("0")
    
    for i in range(len(dab)):
        if start[i]!=dab[i]:
            start[i:]=dab[i]*(len(start) -i)
            cnt+=1
    print("#{} {}".format(j+1,cnt))
