def solution(a):
    res=''
    while a>0:
        a-=1
        res='124'[a%3]+res
        a=a//3


    return res
