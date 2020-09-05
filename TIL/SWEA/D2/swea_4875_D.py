# DFS - STACK
def isWall(y, x):
    if x >= 0 and x < N and y >= 0 and y < N and (maze[y][x] == 0 or maze[y][x] == 3):
        return True

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
    result = 0
    stack = []
    stack.append((startY, startX))
    visited.append((startY, startX))
    while stack:
        y, x = stack.pop()
        for d in range(4):
            newY = y + dy[d]
            newX = x + dx[d]
            if isWall(newY, newX) and (newY, newX) not in visited:
                stack.append((newY, newX))
                visited.append((newY, newX))
                if maze[newY][newX] == 3:
                    result = 1
    print('#{} {}'.format(tc, result))