num = int(input())

cnt=1

if num ==1 :
    print(1)

else:
    while num>=2:
        num = num - 6*cnt
    
        cnt+=1
    print(cnt)

    