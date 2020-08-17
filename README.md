# Algorithm 문제 풀이 및 정리

> 첫 알고리즘 수업 시간에 느꼈던 점은 너무 너무 어렵다,,그저 어렵다,,였다. 문제를 풀기 위한 알고리즘을 생각하는 것도 부족하고 배웠던 Python 문법을 적용시켜 구현하는 것은 더욱 어려웠다.

> 때문에!!!! Algorithm 수업 시간에 배운 이론 내용과 풀었던 문제를 다시 정리하고 swea 문제들을 풀어보며 내 것으로 만들기위해 레포지를 만들었다!!

> 문제를 못 풀수도 있고 풀었다하더라도 코드의 길이가 길고 실행시간이 오래 걸리는 등 아직 많이 부족하기 때문에 두번, 세번 풀어보며 코드를 간소화해보자.

> 또한, 함께 수업을 듣는 사람들과 소통하며 다양한 코드 구현 방식을 익혀보자! 화이팅!! 😊😊



> ▶ 사용할 언어: Python 
>
> ▶ SW 역량테스트 IM 도저언!
>
> ▶ 1일 1 커밋하기!
>
> ▶ SWEA : 문제 난이도 > swea_문제번호 
>
> ▶ Algorithm: 난이도 > 문제 유형 > 문제번호_문제제목



---



[toc]

---



## SWEA

### D1



### D2

- **swea_1966 (숫자를 정렬하자)**

주어진 N의 길이의 숫자열을 오름차순으로 정렬하여 출력하는 문제.

수업시간에 배웠던 선택정렬을 사용!

```python
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    for i in range(N): # 주어진 N의 범위만큼 순회
        min = i # i가 0부터 시작하므로 최솟값을 찾기 위한 인덱스 min을 i로 설정
        for j in range(i+1, N): # 0 다음인 1 인덱스부터 차례대로 순회
            if lst[min] > lst[j]: # 0번째 값보다 작은 인덱스 값(j)이 나온다면
                min = j # 최소 인덱스 값을 j로 바꿔준다.
        lst[i], lst[min] = lst[min], lst[i] # 현재 인덱스와 최소 인덱스 자리를 swap!
    
    print('#{}'.format(tc), end=' ')
    for i in lst: 
        print(i, end=' ')
    print()
```



- **swea_1948 (날짜 계산기)**

월 일로 이루어진 날짜를 2개 입력 받아, 두 번째 날짜가 첫 번째 날짜의 며칠째인지 출력하는 문제.

나는 날짜 계산법의 정석대로 그냥 풀었다..

```python
T = int(input())
for tc in range(1, T+1):

    lst = list(map(int, input().split())) # 3 22 5 10
	# 각 월마다 날짜 수를 리스트로 만들어준다.
    # 3월 22일에서 5월 10일까지의 날짜를 계산하려면
    # 3월 22일~3월 31일/ 4월 / 5월 1일~5월 10일의 일 수를 다 더해준다.
    num = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total = 0
    # 먼저 통으로 계산되는 월을 구해서 total에 더해주고 (4월)
    for i in num[lst[0]:lst[2]-1]:
        total += i
	# 두 날짜의 월이 같다면 두 날짜의 일을 뺀 값을 더해주고
    if lst[0] == lst[2]:
        total += (lst[3] - lst[1])
    # 같지않다면
    # 첫번째 날짜의 경우, 해당 월의 총 일수에서 현 날짜를 빼준다(첫번째 날짜가 3월 22일이라면       3월의 총 일수인 31에서 현 일수인 22일을 빼 8이 얻어진다.)
    # 두번째 날짜의 경우, 그냥 현 일수인 lst[3]의 값을 더해주면 된다.(5월 10일이라면 그냥         10만 더해준다.)
    else: 
        total += (num[lst[0]-1] - lst[1]) + lst[3]
        #두번째 날짜가 첫번째 날짜의 며칠째인지 묻고 있으므로 총 total에 1을 더해준다.
    print('#{} {}'.format(tc, total+1))
```



- **swea_1961 (숫자 배열 회전)**

N x N 행렬이 주어질 때,

시계 방향으로 90도, 180도, 270도 회전한 모양을 출력하는 문제.

나는 행 순서가 아니라 열 순서대로 숫자들을 거꾸로 새로운 리스트에 담는 방법을 사용했다.



만일 N이 3이라면,

new_arr = [ 

[arr[2] [0], arr[1] [0], arr[0] [0]], 

[arr[2] [1], arr[1] [1], arr[0] [1]], 

[arr[2] [2], arr[1] [2], arr[0] [2]]

]



이렇게 일일이 하니 시간이 너무 오래 걸렸고 코드가 엄청 길어졌다..

코드를 줄이는 방법을 다시 생각해야겠다,,

```python
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    new_lst = []
    for i in range(0, len(arr)):
        lst = []
        for j in range(0, len(arr)):
            lst.append(arr[j][i])
            
        new_lst.append(lst)
        
    num_list = []
    for i in new_lst:
        num_list.append(i[::-1])

    new_lst2 = []
    for k in range(0, N):
        lst2 = []
        for l in range(0, N):
            lst2.append(num_list[l][k])
        new_lst2.append(lst2)

    num_list2 = []
    for i in new_lst2:
        num_list2.append(i[::-1])
        num_list.append(i[::-1])

    new_lst3 = []
    for k in range(0, N):
        lst3 = []
        for l in range(0, N):
            lst3.append(num_list2[l][k])
        new_lst3.append(lst3)

    num_list3 = []
    for i in new_lst3:
        num_list3.append(i[::-1])
        num_list.append(i[::-1])

    print('#{}'.format(tc))
    for i in range(0, N):
        for j in num_list[i:len(num_list):N]:
            j.append(" ")
            for k in j:
                print(k, end='')
        print()
```



- **swea_1979 (어디에 단어가 들어갈 수 있을까)**

처음엔 행과 열 모두 체크하면서 연속된 1의 값을 cnt로 체크해주고 cnt가 K-1번 나왔다면 result에 +1을 해주자! 라고 생각하고 코드를 짰다.

```python
N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

result = 0
# 행 체크
for i in range(0, N):
    cnt = 0
    for j in range(0, N-1):
        if arr[i][j] == 0:
            continue
        else:
            if arr[i][j] == arr[i][j+1]:
                cnt += 1
if cnt == K-1:
    result += 1
# 열 체크
for i in range(0, N-1):
    cnt1 = 0
    for j in range(0, N):
        if arr[j][i] == 0:
            continue
        if arr[j][i] == arr[j][i+1]:
            cnt1 += 1
if cnt1 == K-1:
    result += 1
print(result)
```

여기서 가장 쉽게 발견할 수 있었던 오류는 cnt와 K-1의 if문의 들여쓰기 였다.

그래서 일일이 if문 들여쓰기를 해보았다.



```python
N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

result = 0

for i in range(0, N):
    cnt = 0
    for j in range(0, N-1):
        if arr[i][j] == 0:
            cnt = 0
            continue
        if arr[i][j] == arr[i][j+1]:
            cnt += 1
    if cnt == K-1:
    	result += 1
                
for i in range(0, N-1):
    cnt1 = 0
    for j in range(0, N):
        if arr[j][i] == 0:
            cnt1 = 0
            continue         
        if arr[j][i] == arr[j][i+1]:
            cnt1 += 1
    if cnt1 == K-1:
    	result += 1

print(result)
```

연속된 값으로 찾으려고 했는데 답이 안나와서 그냥 요소가 1인것들을 세기로 했다.

```python
N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

result = 0
for i in range(0, N):
    cnt = 0
    for j in range(0, N):
        if arr[i][j] == 0:
            cnt = 0
            continue
        if arr[i][j] == 1:
            cnt += 1
    if cnt == K:
        result += 1    

for i in range(0, N):
	cnt1 = 0
	for j in range(0, N):
		if arr[j][i] == 0:
			cnt1 = 0
			continue
		if arr[j][i] == 1:
			cnt1 += 1
	if cnt1 == K:
		result += 1
```

이렇게 하면 행 또는 열 안에 1이 연속되게 K번 나온 후 0이 나온다면 cnt를 0으로 초기화했기 때문에 값이 나오지 않았다. 그래서 요소가 0일 때도 cnt가 K와 같은지 확인해야 한다!

> 최종코드

```python
import sys
sys.stdin = open('input_1979.txt')

T = int(input())
for tc in range(1, T+1):

    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    # cnt = 0
    for i in range(0, N):
        cnt = 0
        for j in range(0, N):
            if arr[i][j] == 0:
                if cnt == K:
                    result += 1
                cnt = 0
                continue
            else:
                cnt += 1
        if cnt == K:
            result += 1

    for i in range(0, N):
        cnt = 0
        for j in range(0, N):
            if arr[j][i] == 0:
                if cnt == K:
                    result += 1
                cnt = 0
                continue
            else:
                cnt += 1
        if cnt == K:
            result += 1

    print('#{} {}'.format(tc, result))
```



- **swea_1976 (시각 덧셈)**

시 분으로 이루어진 시각을 2개 입력 받아, 더한 값을 시 분으로 출력하는 문제.

```python
T = int(input())
for tc in range(1, T+1):

    lst = list(map(int, input().split()))

	# 시 끼리 먼저 더해주고 더한 값이 12보다 크면 값에서 12를 빼준다.
    if lst[0] + lst[2] > 12:
        h = (lst[0] + lst[2]) - 12

    else:
        h = lst[0] + lst[2]
	# 분 끼리 더해주고 더한 값이 60보다 크면 값에서 60을 빼주고 시에 + 1를 해준다.
    if lst[1] + lst[3] > 60:
        h += 1
        m = (lst[1] + lst[3]) - 60

    else:
        m = lst[1] + lst[3]

    print('#{} {} {}'.format(tc,h, m))
```



- **swea_1954 (달팽이 숫자)**

1부터 N*N 까지의 숫자를 시계방향으로 이루어진 달팽이 모양으로 출력하는 문제.

```python
T = int(input())
for tc in range(1, T+1):

    # lst에서 최소값을 구한다.
    def getMin(curV):
        minV = 1000
        for i in lst:
            if minV > i and i > curV:
                minV = i
        return minV

    # 벽을 만났을 때,
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
    
	# 방향 설정
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    dir = 0

    # 현재 위치 설정
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
```



- **swea_2005 (파스칼의 삼각형)**

![swea_2005](README.assets/swea_2005.PNG)

```python
T = int(input())
for tc in range(1, T+1):
    
    N = int(input())
    # N행의 빈 2차원 리스트를 만들어준다.
    arr = [ [] for _ in range(N)]

    # 1행은 [1] 2행은 [1, 1]을 먼저 넣어준다.
    arr[0].append(1)
    if len(arr) > 1:
        arr[1].append(1)
        arr[1].append(1)

	# 2행부터 순회하며 연속된 두개의 값을 더해 그 다음 행에 넣어주고,
    for i in range(1, N-1):
        for j in range(0, len(arr[i])-1):
            x = arr[i][j] + arr[i][j+1]
            arr[i+1].append(x)
        # 행의 앞, 뒤로 1를 넣어준다.
        arr[i+1].insert(0, 1)
        arr[i+1].insert(len(arr[i+1]), 1)

    print('#{}'.format(tc))
    for i in range(N):
        for j in range(0, len(arr[i])):
            print(arr[i][j], end=" ")
        print()
```



### D3





---



## Algorithm

### 이론



### Intermediate



### Advanced





