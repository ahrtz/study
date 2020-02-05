# def check(a):
#     b=list(str(a))
#     if b==sorted(b):
#         return a
#     else:
#         return 0




a=int(input())

for i in range(a):
    n= int(input())
    num_li = list(map(int,input().split()))
    
    final=[]
    for k in range(n-1):
        for j in range(k+1,n):
            tmp = num_li[k]*num_li[j]
            if len(str(tmp))==0:
                continue
            # if check(tmp):
            #     final.append(tmp)
            for l in range(len(str(tmp))-1):
                if str(tmp)[l] >str(tmp)[l+1]:
                    break
            
            else:
                final.append(tmp)
    # print(final)
    
    if len(final)==0:
        print("#{} {}".format(i+1,-1))
    else:
        print("#{} {}".format(i+1,max(final)))