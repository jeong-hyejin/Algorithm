T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    for i in range(M):
        arr.append(arr.pop(0))
    print('#{} {}'.format(tc, arr[0]))

'''
idx = M % N
arr[idx]
'''