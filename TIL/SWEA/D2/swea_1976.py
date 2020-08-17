T = int(input())
for tc in range(1, T+1):

    lst = list(map(int, input().split()))


    if lst[0] + lst[2] > 12:
        h = (lst[0] + lst[2]) - 12

    else:
        h = lst[0] + lst[2]

    if lst[1] + lst[3] > 60:
        h += 1
        m = (lst[1] + lst[3]) - 60

    else:
        m = lst[1] + lst[3]

    print('#{} {} {}'.format(tc,h, m))