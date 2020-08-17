T = int(input())
for tc in range(1, T+1):

    def getMin(curV):
        minV = 1000
        for i in lst:
            if minV > i and i > curV:
                minV = i
        return minV

    def isWall(x, y):
        if x >= N or x < 0:
            return True
        if y >= N or y < 0:
            return True

        if arr[y][x] != 0:
            return True
        return False

    N = int(input())
    lst = list(range(1, N**2+1))


    arr = [[0] * N for _ in range(N)]


    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    dir = 0

    curX = curY = 0
    curV = 0

    for i in range(1, N**2+1):
        val = getMin(curV)
        arr[curY][curX] = val
        testX = curX + dx[dir]
        testY = curY + dy[dir]
        if isWall(testX, testY):
            dir += 1
            if dir == 4:
                dir = 0

        curX = curX + dx[dir]
        curY = curY + dy[dir]
        curV = val

    print('#{}'.format(tc))
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i][j], end=" ")
        print()