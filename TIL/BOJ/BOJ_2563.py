white = [[0] * 100 for _ in range(100)]
N = int(input())
for _ in range(N):
    x1, y1 = map(int, input().split())
    for y in range(10):
        for x in range(10):
            white[y1+y-1][x1+x-1] = 1
cnt = 0
for i in white:
    cnt += i.count(1)
print(cnt)