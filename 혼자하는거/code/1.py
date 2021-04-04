def balancedSum(arr):
    target = arr[-1]
    start=0
    end =len(arr)-1
    sum_start=arr[start]
    sum_end=arr[end]
    while  start+2!=end:
        if sum_start<=sum_end:
            start+=1
            sum_start+=arr[start]
        elif sum_start>sum_end:
            end-=1
            sum_end+=arr[end]
    return start+1


    # print(res)
    # fptr.write(str(result) + '\n')

    # fptr.close()

# print(balancedSum(arr))