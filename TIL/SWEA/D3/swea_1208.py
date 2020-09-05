import sys
sys.stdin = open('input_1208.txt')
T = 10
for tc in range(1, T+1):
    # dump 횟수 입력
    N = int(input())
    box = list(map(int, input().split()))
    # dump 횟수만큼 반복
    # box의 최댓값과 최솟값을 구해 각 각 -1, +1을 해준다.
    for i in range(N):
        min_box = 0
        max_box = 0
        for j in range(1, len(box)):
            if box[min_box] > box[j]:
                min_box = j
            if box[max_box] < box[j]:
                max_box = j
        box[max_box] -= 1
        box[min_box] += 1
    # dump가 끝나고 box에서의 최댓값과 최솟값을 구해 빼준다.
    min_b = 0
    max_b = 0
    for i in range(len(box)):
        if box[min_b] > box[i]:
            min_b = i
        if box[max_b] < box[i]:
            max_b = i
    print('#{} {}'.format(tc, box[max_b] - box[min_b]))