arr = [[0] * 100 for _ in range(100)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(abs(y2-y1)):
        for x in range(abs(x2-x1)):
            arr[y1+y][x1+x] = 1
cnt = 0
for i in range(100):
    cnt += arr[i].count(1)
print(cnt)