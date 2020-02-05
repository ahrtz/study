t=int(input())
for i in range(t):
    a=int(input())
    resu=0
    for k in range(a):
        c,b =map(int,input().split())
        resu += c*b
    print(f"#{i+1} {resu}")