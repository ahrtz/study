t=int(input())
for tc in range(t):
    num_li=list(map(int,input().split()))
    set_li=set(num_li)
    for i in set_li:
        if num_li.count(i)==1 or num_li.count(i)==3:
            ans = i
        elif num_li.count(i)==2:
            continue
    print("#{} {}".format(tc+1,ans))