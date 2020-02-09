T=int(input())
for tc in range(T):
    a=int(input())
    if a%2 == 0:
        print("#{} {}".format(tc+1,"Even"))
    else:
        print("#{} {}".format(tc+1,"Odd"))