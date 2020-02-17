
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
    for x in Ap:
        if abs((x[1]-1)-ar)+abs((x[0]-1)-ac)<=x[2]:
            tmpa.append(x[3])
            
        if abs((x[1]-1)-br)+abs((x[0]-1)-bc)<=x[2]:
            tmpb.append(x[3])
    APower.append(tmpa)
    BPower.append(tmpb)



    for mv in range(M):
        a_newx = ar + d[A_route[mv]][0]
        a_newy = ac + d[A_route[mv]][1]
        b_newx = br + d[B_route[mv]][0]
        b_newy = bc + d[B_route[mv]][1]
        tmp_A=[]
        tmp_B=[]
        for x in Ap:
            if abs((x[1]-1)-a_newx)+abs((x[0]-1)-a_newy)<=x[2]:
                tmp_A.append(x[3])
                
            if abs((x[1]-1)-b_newx)+abs((x[0]-1)-b_newy)<=x[2]:
                tmp_B.append(x[3])
        ar=a_newx
        ac=a_newy
        br=b_newx
        bc=b_newy
        APower.append(tmp_A)
        BPower.append(tmp_B)
    for i in range(len(APower)):
        if APower[i]==[]:
            APower[i]=[0]
        if BPower[i]==[]:
            BPower[i]=[0]



    cnt = 0
    for i in range(len(APower)):
        if len(APower[i])==1 and len(BPower[i])==1 and APower[i][0]!=BPower[i][0]:
            cnt+= APower[i][0]
            cnt+= BPower[i][0]
        elif len(APower[i])==1 and len(BPower[i])==1 and APower[i][0]==BPower[i][0]:
            cnt+= APower[i][0]
        else:
            if len(set(APower[i]) & set(BPower[i]))==0:
                cnt+= max(APower[i])
                cnt+= max(BPower[i])
            if len(set(APower[i]) & set(BPower[i]))>=1:
                APower[i] = sorted(APower[i])
                BPower[i] = sorted(BPower[i])
                if APower[i][-1]!=BPower[i][-1]:
                    cnt+=APower[i][-1]
                    cnt+=BPower[i][-1]
                else:
                    ca=0
                    cb=0
                    try:
                        ca+=APower[i][-1]
                        ca+=APower[i][-2]
                    except :
                        pass
                    try:
                        
                        cb+=BPower[i][-1]
                        cb+=BPower[i][-2]
                        
                    except :
                        pass
                    cnt+= max(ca,cb)

    print(APower)
    print("#{} {}".format(tc+1,cnt))