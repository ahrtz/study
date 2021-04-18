def solution(a, edges):
    if sum(a)!=0:
        return -1
    if sum(a)==[0]*len(a):
        return 0
    r_dict = [[k] for k in range(len(a))]

    for i in edges:
        r_dict[i[0]].append(i[1])
        r_dict[i[1]].append(i[0])

    
    temp=sorted(r_dict,key=lambda x:len(x))
    print(temp)

    candidate=[i for i in range(len(a))]
    print(candidate)
    cnt=0
    for i in temp:
        if a[i[0]]==0:
            candidate.remove(i[0])
            
        else:
            for k in range(1,len(i)):
                if a[i[k]] ==0:
                    continue
                cnt+=(1*abs(a[i[0]]))
                a[i[k]]+=a[i[0]]
                a[i[0]]=0
                candidate.remove(i[0])
                break
                

    


    print(cnt)
    return cnt

solution([-5,0,2,1,2],[[0,1],[3,4],[2,3],[0,3]])