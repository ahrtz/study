def minX(arr):
    # Write your code here
    temp=0
    val=0
    for i in arr:
        temp+=i
        if temp<1:
            if temp*(-1)>val:
                val=temp*(-1)
    return val+1
print(res)