def search(k, A):
    l = 1
    cnt = 0
    while l <= k:
        c = (l + k) // 2
        if c == A:
            cnt += 1
            break
        elif c < A:
            l = c
            cnt += 1
        else:
            k = c
            cnt += 1

    return cnt

T = int(input())
for tc in range(1, T+1):
    k, A, B = map(int, input().split())
    if search(k, A) < search(k, B):
        print('#{} A'.format(tc))
    elif search(k, A) == search(k, B):
        print('#{} 0'.format(tc))
    else:
        print('#{} B'.format(tc))
