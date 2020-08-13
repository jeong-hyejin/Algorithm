T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    for i in range(N):
        min = i
        for j in range(i+1, N):
            if lst[min] > lst[j]:
                min = j
        lst[i], lst[min] = lst[min], lst[i]
    
    print('#{}'.format(tc), end=' ')
    for i in lst:
        print(i, end=' ')
    print()