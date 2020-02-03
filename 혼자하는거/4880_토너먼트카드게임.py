def tour(a):
    tmp=[]
    if len(a) % 2 ==0:
        for i in range(0,len(a),2):
            if a[i][-1]==a[i+1][-1] :
                tmp.append(a[i])
            elif a[i][-1]==1 and a[i+1][-1]==2:
                tmp.append(a[i+1])
            elif a[i][-1]==1 and a[i+1][-1]==3:
                tmp.append(a[i])
            elif a[i][-1]==2 and a[i+1][-1]==1:
                tmp.append(a[i])
            elif a[i][-1]==2 and a[i+1][-1]==3:
                tmp.append(a[i+1])
            elif a[i][-1]==3 and a[i+1][-1]==1:
                tmp.append(a[i+1])
            elif a[i][-1]==3 and a[i+1][-1]==2:
                tmp.append(a[i])
    else:
        for i in range(0,len(a)-1,2):
            if a[i][-1]==a[i+1][-1] :
                tmp.append(a[i])
            elif a[i][-1]==1 and a[i+1][-1]==2:
                tmp.append(a[i+1])
            elif a[i][-1]==1 and a[i+1][-1]==3:
                tmp.append(a[i])
            elif a[i][-1]==2 and a[i+1][-1]==1:
                tmp.append(a[i])
            elif a[i][-1]==2 and a[i+1][-1]==3:
                tmp.append(a[i+1])
            elif a[i][-1]==3 and a[i+1][-1]==1:
                tmp.append(a[i+1])
            elif a[i][-1]==3 and a[i+1][-1]==2:
                tmp.append(a[i])
    if len(tmp)==1:
        return tmp
    else:
        return tour(tmp)   



a=int(input())
for i in range(1,a+1):
    temm = int(input())
    num_li = list(map(int,input().split()))
    num_li = list(enumerate(num_li,start=1))
    num_a=num_li[:(len(num_li)//2)+1]
    num_b=num_li[(len(num_li)//2)+1:]
    
    resu=[]
    resu.append(tour(num_a)[0])
    resu.append(tour(num_b)[0])
    print("#{} {}".format(i,tour(resu)[0][0]))

