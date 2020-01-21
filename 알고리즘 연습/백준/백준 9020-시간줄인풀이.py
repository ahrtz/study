import sys
N = 10001
sieve = [True] * N
def prime_sieve(N):
    for i in range(2, N):
        if sieve[i]:
            for j in range(2*i, N, i):
                sieve[j] = False
prime_sieve(N)

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    idx = 0
    while True:
        if sieve[n//2 - idx] and sieve[n//2 + idx]:
            print(n//2 - idx, n//2 + idx)
            break
        idx += 1
