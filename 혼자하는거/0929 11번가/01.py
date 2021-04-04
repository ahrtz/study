def solution(S):
    
    if 'aaa' in S:
        return -1
    if 'a' not in S:
        return 2*(len(S)+1)
    tmp_a = S.count('a')
    not_A = len(S)-tmp_a
    cnt=(not_A+1)*2-tmp_a
    return cnt

print(solution('abadc'))