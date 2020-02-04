def mooon(a):
   


    if a==a[::-1]:
        return True
    else:
        return False



for i in range(10):
    tc=int(input())
    pan=[]
    for k in range(100): # 가로행렬
        tmp=str(input())
        pan.append(tmp)
    # #세로행렬 만들기
    sero_pan=[]
    for gojung in range(100):
        tmp1=[]
        for sero in range(100):
            tmp1.append(pan[sero][gojung])
        sero_pan.append(tmp1)
    
    cnt=0
    #가로방향 count 
    for r_num in range(len(pan)): # 행 정하는거
        for num in range(len(pan[r_num])-1): # 시작점 
            for k in range(num+1,len(pan[r_num])): # 끝점
                
                if mooon(pan[r_num][num:k]):
                    
                    if cnt<=len(pan[r_num][num:k]):
                        cnt=len(pan[r_num][num:k])
                        # print(pan[r_num][num:k])
                        # print(r_num)
                    
    #세로방향 count
    cnt1=0
    for ro_num in range(len(sero_pan)):
        for numa in range(len(sero_pan[ro_num])-1): # 반복
            for ka in range(numa+1,len(sero_pan[ro_num])):
                
                if mooon(sero_pan[ro_num][numa:ka]):
                    
                    if cnt1<=len(sero_pan[ro_num][numa:ka]):
                        cnt1=len(sero_pan[ro_num][numa:ka])
                        # print(sero_pan[ro_num][numa:ka])
    print("#{} {}".format(tc,max(cnt,cnt1)))