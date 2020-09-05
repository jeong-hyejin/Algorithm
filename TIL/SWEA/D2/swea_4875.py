# DFS - 재귀
def isWall(y, x):
    if x >= 0 and x < N and y >= 0 and y < N and (maze[y][x] == 0 or maze[y][x] == 3):
        return True
    return False

def DFS(startY, startX):
    global result
    if maze[startY][startX] == 3:
        result = 1
        return
    visited.append((startY, startX))
    for d in range(4):
        newY = startY + dy[d]
        newX = startX + dx[d]
        if isWall(newY, newX) and (newY, newX) not in visited:
            DFS(newY, newX)
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    visited = []
    result = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for x in range(N):
        for y in range(N):
            if maze[y][x] == 2:
                startY = y
                startX = x

    DFS(startY, startX)
    print('#{} {}'.format(tc, result))