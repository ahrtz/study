def check(a,b): ## 돌다가 몇개 안골랐는데 커지면 그냥 튀어나가라
    global minV
    suma=0
    for i in range(len(a)):
        suma += pan[i][a[i]]
    if minV<suma:
        
        return


    if len(a)==b:
        suma=0
        for i in range(len(a)):
            suma += pan[i][a[i]]
        if minV>suma:
            minV=suma
        return 
    
    candid=list(range(b))
    for i in range(len(a)):
        if a[i] in candid:
            candid.remove(a[i])
        # dis = len(a)-i
        # if a[i]-dis in candid:
        #     candid.remove(a[i]-dis)
        # if a[i]+dis in candid:
        #     candid.remove(a[i]+dis)
    if len(candid)!=0:
        for i in candid:
            a.append(i)
            check(a,b)
            a.pop()
    else:
        return 0 


T=int(input())
for tc in range(T):
    N=int(input())
    pan=[]
    num=list(range(N))



    for _ in range(N):
        tmp = list(map(int,input().split()))
        pan.append(tmp)
    minV=109232735987
    for i in range(N):
        check([i],N)

    print("#{} {}".format(tc+1,minV))