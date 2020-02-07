T=int(input())
for tc in range(T):
    al,bl = map(int,input().split())
    a_list= list(map(int,input().split()))
    b_list= list(map(int,input().split()))
    if len(a_list)>len(b_list):
        a_list,b_list=b_list,a_list
        al,bl=bl,al
    res=[]
    # print(al,bl,a_list,b_list)
    for mv in range(bl-al+1):
        tmp_b=b_list[mv:mv+len(a_list)]
        alpha=0
        for i in range(len(a_list)):
            alpha += a_list[i]*tmp_b[i]
        res.append(alpha)
    print("#{} {}".format(tc+1,max(res)))    
