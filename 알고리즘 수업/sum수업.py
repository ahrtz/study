def suma(a):
    res=0
    for i in a:
        res+=i
    return res




for i in range(10):
    t = int(input())
    num_li=[]
    for i in range(100):
        numm=list(map(int,input().split()))
        num_li.append(numm)
    #세로행렬 만들기
    num_sero=[]
    for tmp in range(100):
        tmp_li=[]
        for sero in range(100):
            tmp_li.append(num_li[sero][tmp])
        num_sero.append(tmp_li)


    
    
    
    
    tmp_sum=suma(num_li[0])
    
    for li in num_li:
        if suma(li)>=tmp_sum:
            tmp_sum=suma(li)
    #이제 세로
    for li in num_sero:
        if suma(li)>tmp_sum:
            tmp_sum=suma(li)
    # 대각선 애들만 빼서 행렬 만들자
    lu=[]#leftup
    ru=[]#rightup
    for j in range(100):# 왼위 행렬 
        lu.append(num_li[j][j])
    #오위행렬
        ru.append(num_li[j][99-j]) 
    if suma(lu)>=tmp_sum:
        tmp_sum=suma(lu)
    if suma(ru)>=tmp_sum:
        tmp_sum=suma(ru)
    
    print("#{} {}".format(t,tmp_sum))   
