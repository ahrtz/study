T=int(input())

for tc in range(T):
    a=float(input())
    ans=[]
    tmp=0
    for i in range(13):
        if tmp ==a:
            break
        if tmp + 1*(2)**(-i-1)>a:
            
            ans.append(0)
        else:
            tmp += 1*(2)**(-i-1)
            ans.append(1)
    
    if len(ans)>12:
        print("#{} {}".format(tc+1,'overflow'))
    else:
        print("#{} {}".format(tc+1,''.join(repr(k) for k in ans)))
