T=int(input())
for tc in range(T):
    tmp=input()
    a=input()
    num=["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    print("#{}".format(tc+1))
    for i in num:
        # print(a.count(i))
        print( a.count(i)*(i+" "),end="")
    print()