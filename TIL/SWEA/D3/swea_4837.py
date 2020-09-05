T = int(input())
for tc in range(1, T+1):

    N, K = map(int, input().split())

    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    # a = list(range(1, 13))
    n = len(A)

    count = 0
    for i in range(1<<n):
        lst = []
        for j in range(n):
            if i & (1<<j):
                lst.append(A[j])
        if len(lst) == N:
            total = 0
            for k in lst:
                total += k
            if total == K:
                count += 1
    print('#{} {}'.format(tc, count))