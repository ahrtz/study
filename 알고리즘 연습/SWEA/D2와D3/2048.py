T=int(input())
for tc in range(T):
    N, dir = input().split()
    N=int(N)
    pan=[]
    for i in range(N): # 왼은 이거 사용
        pan.append(list(map(int,input().split())))
    
    
    #오른쪽용판
    rpan=[]
    for r_row in range(N):
        t_tmp=[]
        for r_col in range(N-1,-1,-1):
            t_tmp.append(pan[r_row][r_col])
        rpan.append(t_tmp)

    




    npan=[]
    for garo in range(N): # 위 쪽용 판pan ( 위로 올리는건 왼쪽 내리는건 오른쪽가는거랑 같음)
        tmp1=[]
        for sero in range(N):
            tmp1.append(pan[sero][garo])
        npan.append(tmp1)
    
    dpan=[]
    for d_row in range(N):
        d_tmp=[]
        for d_col in range(N-1,-1,-1):
            d_tmp.append(npan[d_row][d_col])
        dpan.append(d_tmp)
    


    res=[]
    if dir =="up": # 왼쪽정렬
        for row in range(N):
            temp=[]
            ocnt = npan[row].count(0)
            for av in range(ocnt):
                npan[row].remove(0)
            
            check=0
            while check<len(npan[row])-1:

                if npan[row][check]!=npan[row][check+1]:
                    temp.append(npan[row][check])
                    check += 1
                elif npan[row][check]==npan[row][check+1]:
                    temp.append(npan[row][check]*2)
                    temp.append(0) # 겹쳐서 하는거 방지 
                    check += 2
            dif = len(npan[row])-len(temp)
            if dif!=0:
                temp.append(npan[row][-1])
            #temp 에서 0의 개수 다 세서 뒤로 보내기 
            cnt = temp.count(0)
            for _ in range(cnt):
                temp.remove(0)
            for _ in range(N-len(temp)):
                temp.append(0)
            res.append(temp)
        pan=[]
        for garo in range(N): 
            tmp1=[]
            for sero in range(N):
                tmp1.append(res[sero][garo])
            pan.append(tmp1)
    
    if dir =="down": # 
        for row in range(N):
            temp=[]
            ocnt = dpan[row].count(0)
            for av in range(ocnt):
                dpan[row].remove(0)
            
            check=0
            while check<len(dpan[row])-1:

                if dpan[row][check]!=dpan[row][check+1]:
                    temp.append(dpan[row][check])
                    check += 1
                elif dpan[row][check]==dpan[row][check+1]:
                    temp.append(dpan[row][check]*2)
                    temp.append(0) # 겹쳐서 하는거 방지 
                    check += 2
            dif = len(dpan[row])-len(temp)
            if dif!=0:
                temp.append(dpan[row][-1])
            #temp 에서 0의 개수 다 세서 뒤로 보내기 
            cnt = temp.count(0)
            for _ in range(cnt):
                temp.remove(0)
            for _ in range(N-len(temp)):
                temp.append(0)
            res.append(temp)
        tttmp=[]
        for d_row in range(N):
            d_tmp=[]
            for d_col in range(N-1,-1,-1):
                d_tmp.append(res[d_row][d_col])
            tttmp.append(d_tmp)
        pan=[]
        for garo in range(N): # 위 쪽용 판pan ( 위로 올리는건 왼쪽 내리는건 오른쪽가는거랑 같음)
            tmp1=[]
            for sero in range(N):
                tmp1.append(tttmp[sero][garo])
            pan.append(tmp1)






    if dir =="left": # 왼쪽정렬
        for row in range(N):
            temp=[]
            ocnt = pan[row].count(0)
            for av in range(ocnt):
                pan[row].remove(0)
            
            check=0
            while check<len(pan[row])-1:
                if pan[row][check]!=pan[row][check+1]:
                    temp.append(pan[row][check])
                    check += 1
                elif pan[row][check]==pan[row][check+1]:
                    temp.append(pan[row][check]*2)
                    temp.append(0) # 겹쳐서 하는거 방지 
                    check += 2
            dif = len(pan[row])-len(temp)
            if dif!=0:
                temp.append(pan[row][-1])
            #temp 에서 0의 개수 다 세서 뒤로 보내기 
            cnt = temp.count(0)
            for _ in range(cnt):
                temp.remove(0)
            for _ in range(N-len(temp)):
                temp.append(0)
            res.append(temp)
        pan=res
    # 대가리가 안돌아가니까 판을 돌리자 
    if dir =="right": # 왼쪽정렬
        for row in range(N):
            temp=[]
            ocnt = rpan[row].count(0)

            for av in range(ocnt):
                rpan[row].remove(0)
            
            check=0
            while check<len(rpan[row])-1:
                if rpan[row][check]!=rpan[row][check+1]:
                    temp.append(rpan[row][check])
                    check += 1
                elif rpan[row][check]==rpan[row][check+1]:
                    temp.append(rpan[row][check]*2)
                    temp.append(0) # 겹쳐서 하는거 방지 
                    check += 2
            dif = len(rpan[row])-len(temp)
            if dif!=0:
                temp.append(rpan[row][-1])
            #temp 에서 0의 개수 다 세서 뒤로 보내기 
            cnt = temp.count(0)
            for _ in range(cnt):
                temp.remove(0)
            for _ in range(N-len(temp)):
                temp.append(0)
            res.append(temp)
        #결과판은 res
            # 다시 원래대로 판을 돌리자 
        # print(res)
        pan=[]
        for r_row in range(N):
            t_tmp=[]
            for r_col in range(N-1,-1,-1):
                t_tmp.append(res[r_row][r_col])
            pan.append(t_tmp)

    print("#{}".format(tc+1))
    for resu in pan:
        print(" ".join(repr(k) for k in resu))