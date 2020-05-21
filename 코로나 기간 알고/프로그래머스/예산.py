def solution(budgets, M):
    left=0
    right = max(budgets)
    ans=0
    while left<=right:
        mid = (left+right)//2
        tmp=0
        for bud in budgets:
            if bud<=mid:
                tmp+=bud
            else:
                tmp+=mid
        if tmp<=M:
            left = mid+1
            ans=mid
        else:
            right=mid-1


    return ans