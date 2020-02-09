import math
T=int(input())


for tc in range(T):
    a=int(input())
    if a==1:
        print("#{} {}".format(tc+1,1))
    elif a==8:
        print("#{} {}".format(tc+1,2))
    elif a==27:
        print("#{} {}".format(tc+1,3))
    elif math.isclose(a**(1/3),int(a**(1/3))+1):
        print("#{} {}".format(tc+1,round(a**(1/3))))
    else:
        print("#{} {}".format(tc+1,-1))