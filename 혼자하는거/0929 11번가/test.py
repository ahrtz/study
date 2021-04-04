from collections import deque
def solution(S):
    cnt=0
    if 'aaa' in S:
        return -1
    if 'a' not in S:
        return 2*(len(S)+1)
    for i in range(1,len(S)):
        if S[i]!='a'

S='dog'
solution(S)