# 1 3 5 11 20.....
# N = (N-2)*2 + (N-1)
def f(n):
    if n <= 1:
        return 1
    else:
        return f(n-2)*2 + f(n-1)

T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc), end=" ")
    N = int(input())
    n = N // 10
    print(f(n))