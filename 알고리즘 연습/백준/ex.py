prices=[1,2,3,2,3]
answer = []
for i in range(len(prices)-1):
    count=0
    for k in range(i+1,len(prices)):
        if prices[i]<=prices[k]:
            count+=1
        else:
            count+=1
            answer.append(count)
            break
        if k==len(prices)-1:
            answer.append(count)
answer.append(0)
print(answer)