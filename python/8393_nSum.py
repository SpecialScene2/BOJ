N = int(input())

Memo = {}
Memo[1] = 1
def sum(N):
    if N in Memo:
        return Memo[N]
    if N == 1:
        value = 1
    elif N > 1:
        value = sum(N-1) + N
    Memo[N] = value
    return value

for n in range(1, N+1):
    sum(n)
print(sum(n))   

