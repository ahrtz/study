<<<<<<< HEAD
t=int(input())
for tc in range(t):
    num_li=list(map(int,input().split()))
    set_li=set(num_li)
    for i in set_li:
        if num_li.count(i)==1 or num_li.count(i)==3:
            ans = i
        elif num_li.count(i)==2:
            continue
    print("#{} {}".format(tc+1,ans))
=======
import itertools
def permute(arr):
    result = [arr[:]]
    c = [0] * len(arr)
    i = 0
    while i < len(arr):
        if c[i] < i:
            if i % 2 == 0:
                arr[0], arr[i] = arr[i], arr[0]
            else:
                arr[c[i]], arr[i] = arr[i], arr[c[i]]
            result.append(arr[:])
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    return result


a=[1,2,3,4]
print(list(itertools.permutations(a,4)))
print(permute(a))
>>>>>>> 85ab2f57dc1f72190242378569f9432d6897fc9a
