a= int(input())
for i in range(a):
    str1=input()
    str2=input()
    result = []
    for K in set(str1):
        result.append(str2.count(K))
    print("#{} {}".format(i+1,max(result)))