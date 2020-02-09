T=int(input())
for tc in range(T):
    D,A,B,F = map(float,input().split())
    sec = D / (A+B)
    print("#{} {}".format(tc+1,sec * F))