import sys
sys.stdin = open('input_1946.txt')
T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc))
    N = int(input())
    lst = []
    for i in range(N):
        alpa, cnt = input().split()
        cnt2 = int(cnt)
        while cnt2 > 0:
            lst.append(alpa)
            cnt2 -= 1
    for i in range(0, len(lst), 10):
        print(*lst[i:i+10], sep="")