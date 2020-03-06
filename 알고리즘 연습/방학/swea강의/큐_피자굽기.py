T= int(input())
for tc in range(T):
    N,M = map(int,input().split())
    pizza_list=list(map(int,input().split()))
    pizza=[]
    for idx,cheese in enumerate(pizza_list):
        pizza.append((idx+1,cheese))
    
    oven=[]
    for _ in range(N):
        oven.append(pizza.pop(0))
    while len(oven)>1:
        tmp,tmp_cheese=oven.pop(0)
        if tmp_cheese != 0 :
            tmp_cheese = tmp_cheese//2
            oven.append((tmp,tmp_cheese))
        else: # 0일때 
            if len(pizza)!=0:
                tmp,tmp_cheese=pizza.pop(0)
                tmp_cheese=tmp_cheese//2
                oven.append((tmp,tmp_cheese))
    
    print("#{} {}".format(tc+1,oven[0][0]))

