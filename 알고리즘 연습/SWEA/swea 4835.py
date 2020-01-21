a= int(input())
for i in range(a):
    temp , mul = map(int,input().split())
    card = list(map(int,input().split()))
    result=[]
    for k in range(len(card)-mul+1):
        tmp_sum=0 
        for alpha in range(mul):
            tmp_sum+=card[k+alpha]
        result.append(tmp_sum)
    print("#{} {}".format(i+1,max(result)-min(result)))