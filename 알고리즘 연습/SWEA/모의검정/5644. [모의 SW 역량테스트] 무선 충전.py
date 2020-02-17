
import pprint


T=int(input())
for tc in range(T):
    M,A = map(int,input().split())
    pan=[[0 for _ in range(10)] for _ in range(10)]
    A_route = list(map(int,input().split()))
    B_route = list(map(int,input().split()))
    Ap=[]
    
    for _ in range(A):
        tmp = list(map(int,input().split()))
        Ap.append(tmp)
    Ap_power=[] # 추후 같은 범위에 있는지 체크할때

    APower=[]
    BPower=[]


    
    d=[(0,0),(-1,0),(0,1),(1,0),(0,-1)]
    
    a=[0,0] # 시작점 좌표
    b=[9,9]
    ar,ac=a[0],a[1]
    br,bc=b[0],b[1]
    tmpa=[]
    tmpb=[]
    for l in range(len(Ap)):
        if abs((Ap[l][1]-1)-ar)+abs((Ap[l][0]-1)-ac)<=Ap[l][2]:
            tmpa.append(Ap[l][3]+0.00000001*l)
            
        if abs((Ap[l][1]-1)-br)+abs((Ap[l][0]-1)-bc)<=Ap[l][2]:
            tmpb.append(Ap[l][3]+0.00000001*l)
    APower.append(tmpa)
    BPower.append(tmpb)



    for mv in range(M):
        a_newx = ar + d[A_route[mv]][0]
        a_newy = ac + d[A_route[mv]][1]
        b_newx = br + d[B_route[mv]][0]
        b_newy = bc + d[B_route[mv]][1]
        tmp_A=[]
        tmp_B=[]
        for l in range(len(Ap)):
            if abs((Ap[l][1]-1)-a_newx)+abs((Ap[l][0]-1)-a_newy)<=Ap[l][2]:
                tmp_A.append(Ap[l][3]+0.00000001*l)
                
            if abs((Ap[l][1]-1)-b_newx)+abs((Ap[l][0]-1)-b_newy)<=Ap[l][2]:
                tmp_B.append(Ap[l][3]+0.00000001*l)
        ar=a_newx
        ac=a_newy
        br=b_newx
        bc=b_newy
        APower.append(tmp_A)
        BPower.append(tmp_B)
    for asd in range(len(APower)):
        if APower[asd]==[]:
            APower[asd]=[0]
        if BPower[asd]==[]:
            BPower[asd]=[0]



    cnt = 0
    for i in range(len(APower)):
        if len(APower[i])==1 and len(BPower[i])==1 and APower[i][0]!=BPower[i][0]:
            cnt+= int(APower[i][0])
            cnt+= int(BPower[i][0])
        elif len(APower[i])==1 and len(BPower[i])==1 and APower[i][0]==BPower[i][0]:
            cnt+= int(APower[i][0]//2)
            cnt+= int(BPower[i][0]//2)
        else:
            if len(set(APower[i]) & set(BPower[i]))==0: # 교집합이 없으면
                cnt+= int(max(APower[i]))
                cnt+= int(max(BPower[i]))
            if len(set(APower[i]) & set(BPower[i]))>=1: # 있으면
                APower[i] = sorted(APower[i])
                BPower[i] = sorted(BPower[i])
                if APower[i][-1]!=BPower[i][-1]:
                    cnt+=int(APower[i][-1])
                    cnt+=int(BPower[i][-1])
                else:
                    ca=0
                    cb=0
                    try:
                        ca+=int(APower[i][-1])
                        ca+=int(APower[i][-2])
                    except :
                        pass
                    try:
                        cb+=int(BPower[i][-1])
                        cb+=int(BPower[i][-2])
                    except :
                        pass
                    cnt+= int(max(ca,cb))

    print(APower)
    print(BPower)
    print("#{} {}".format(tc+1,cnt))