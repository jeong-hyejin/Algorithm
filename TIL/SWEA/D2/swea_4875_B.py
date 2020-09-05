# BFS - QUEUE
def isWall(y, x):
    if x >= 0 and x < N and y >= 0 and y < N and (maze[y][x] == 0 or maze[y][x] == 3):
        return True
    return False

def BFS(startY, startX):
    global result
    Q = []
    Q.append((startY, startX))
    visited.append((startY, startX))
    while Q:
        y, x = Q.pop(0)
        for d in range(4):
            newY = y + dy[d]
            newX = x + dx[d]
            if isWall(newY, newX) and (newY, newX) not in visited:
                Q.append((newY, newX))
                visited.append((newY, newX))
                if maze[newY][newX] == 3:
                    result = 1
                    return
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
                startX = x
                startY = y
    BFS(startY, startX)
    print('#{} {}'.format(tc, result))