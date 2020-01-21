num = int(input())
for k in range(num):

    start,arrive = map(int,input().split())
    trial= arrive -start
    sum = 0
    i = 1 
    while sum < trial :
        sum += (2*i)
        i += 1 

    if sum - trial == 0 :
        print((i-1)*2)
    elif sum - trial <= (i-1)//2:
        print(((i-1)*2))
    elif sum - trial >= (i-1)//2 :
        print((i-1)*2-1)
    ///////////////////////////
    t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    c = b - a
    num = 1
    while True:
        if num ** 2 <= c < (num + 1) ** 2:
            break
        num += 1
    if num ** 2 == c:
        print((num * 2) - 1)
    elif num ** 2 < c <= num ** 2 + num:
        print(num * 2)
    else:
        print((num * 2) + 1)