num = int(input())

cnt=0  
sum=0
while sum<num:
    cnt += 1
    sum = sum + cnt
    

summ = sum-num
alpha=cnt+1

if cnt % 2 ==0:
    print(str(alpha-(summ+1))+"/"+str(summ+1))
else:
    print(str(summ+1)+"/"+str(alpha-(summ+1)))

