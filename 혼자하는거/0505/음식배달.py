from itertools import combinations
T = int(input())
for tc in range(T):
    r = int(input())
    pan=[]
    restaurant=[]
    customer=[]
    for i in range(r):
        tmp=list(map(int,input().split()))
        pan.append(tmp)
        for c in range(r):
            if tmp[c]>1:
                restaurant.append([i,c])
            elif tmp[c]==1:
                customer.append([i,c])
    min_price=10**30
    len_res=(len(restaurant))
    # print(pan)
    # print(restaurant)
    for i in range(1,len_res+1):
        
        candid=combinations(range(len_res),i)
        for item in candid: # 후보결정
            # item=[0,1,2,3,5,6,7,8,9]
            price=0
            for customer_idx in customer:
                tmp_min_price=10**50      
                for idx in range(len(item)): # 음식점 인덱스 뽑기
                    tmp_price=0
                    tmp_price+=abs(restaurant[item[idx]][0]-customer_idx[0])+abs(restaurant[item[idx]][1]-customer_idx[1])
                    if tmp_price<tmp_min_price:
                        tmp_min_price=tmp_price
                price+=tmp_min_price
                if price > min_price:
                    break
            for idx in range(len(item)):
                price+=pan[restaurant[item[idx]][0]][restaurant[item[idx]][1]]
            if price<min_price:
                min_price=price
    if min_price==10**30:
        min_price=0
    print(f"#{tc+1} {min_price}")