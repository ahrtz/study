for i in range(10):
    t=int(input())
    pswd=list(map(int,input().split()))
    while True:
        for i in range(1,6):
            tmp = pswd.pop(0)
            tmp -= i
            if tmp<=0:
                tmp = 0
                pswd.append(tmp)
                break            
            else:
                pswd.append(tmp)
        if pswd[-1]==0:
            break

    print("#{} {}".format(t," ".join(repr(k) for k in pswd)))





        #         pswd[i-1]-=i
        #     if pswd[i-1]==0:
                
        #         b=pswd[:i]
        #         c=pswd[i:]

        #         break
        # b=pswd[:5]
        # c=pswd[5:]
        # pswd=c+b