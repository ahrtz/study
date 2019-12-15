# import time
# start = time.time()

num = int(input())

cnt=0  
sum=0
while sum<num:
    cnt += 1
    sum = sum + cnt
    

summ = sum-num
alpha=cnt+1
print(cnt)
print(summ)
print(str(alpha-(summ+1))+"/"+str(summ+1))
# print(str(summ+1)+"/"+str(alpha-(summ+1)))

# print("time :", time.time() - start)