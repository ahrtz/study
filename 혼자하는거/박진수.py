def jongee(x):
    if x == N:
        return 1
    if x > N:
        return 0
    return jongee(x+10) + jongee(x+20) * 2


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    print('#{} {}'.format(tc, jongee(0)))