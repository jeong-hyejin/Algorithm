import sys
sys.stdin = open('input_1206.txt')
T = 10
for tc in range(1, T+1):
    N = int(input())
    bld = list(map(int, input().split()))
    total = 0
    # 맨 앞과 뒤 2개씩 0이므로 인덱스를 2부터 N-2까지 설정
    for i in range(2, N-2):
        bld_lst = [bld[i-2], bld[i-1], bld[i+1], bld[i+2]]
        max_bld = 0
        for j in bld_lst:
            if max_bld < j:
                max_bld = j
        if bld[i] > max_bld:
            total += bld[i] - max_bld
    print('#{} {}'.format(tc, total))