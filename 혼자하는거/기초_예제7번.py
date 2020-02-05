
a=[1, 3, 2, 5, 2, 2, 3, 1, 1, 6]
print(len(a))

result=[]
for i in range(len(a)):
    start = i -a[i] 
    end = i + a[i]
    if start < 0 :
        start = 0
    if end > len(a):
        end = len(a)
    result.append(sum(a[start:end+1]))
print(result)
