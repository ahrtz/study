T=int(input())
for tc in range(T):
    N=int(input())
    pan= [list(map(int,input().split())) for _ in range(N)]

    d=((0.1),(1,0))
    rc=[]
    size=[]
    for r in range(N):
        for c in range(N):
            if pan[r][c]>=1:
                r_start = r
                c_start = c
                r1=1
                c1=1
                while pan[r_start][c_start]>=1:
                    check_r = r_start+r1
                    r1 += 1
                    if check_r>=N or pan[check_r][c_start]==0:
                        break
                while pan[r_start][c_start] >= 1:
                    check_c = c_start+c1
                    c1 += 1
                    if check_c>=N or pan[r_start][check_c]==0:
                        break
                r1-=1
                c1-=1
                rc.append((r1,c1))
                
                for r2 in range(r_start,r_start+r1):
                    for c2 in range(c_start,c_start+c1):
                        pan[r2][c2]=0                    
    rc.sort(key= lambda x: (x[0]*x[1],x[0]))
    rc1=[]
    for i in rc:
        rc1.append(i[0])
        rc1.append(i[1])
    # print(rc)
    # print(rc1)
    print("#{} {} {}".format(tc+1,len(rc)," ".join(repr(k) for k in rc1)))