T=int(input())
for tc in range(T):
    bat=[]
    width = int(input())
    for _ in range(width):
        tmp = list(map(int,input().split()))
        bat.append(tmp)
    
    u=0
    d=0
    l=0
    r=0
    cut=1
    while cut<width//2+1:
        for row in range(width//2): #위
            for col in range(cut,width-cut):
                u += bat[row][col]
            cut+=1
        cut=1
        for rowd in range(width-1,width//2,-1): #아래쪽
            for cold in range(cut,width-cut):
                d+= bat[rowd][cold]
            cut+=1
        cut=1
        for coll in range(width//2): # 왼쪽
            for rowl in range(cut,width-cut):
            
                l += bat[rowl][coll] 
            cut+=1
        cut=1
        for colr in range(width-1,width//2,-1): # 오른쪽
            for rowr in range(cut,width-cut): 
                
                r += bat[rowr][colr]
            cut+=1
    cnt_list=[u,d,l,r]

    print("#{} {}".format(tc+1,max(cnt_list)-min(cnt_list)))