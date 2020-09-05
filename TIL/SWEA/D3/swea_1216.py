'''
100 * 100 table에서 행과 열에서 가장 긴 회문을 찾고 회문의 길이를 출력하는 문제.
회문의 길이가 정해져있지않아 1개부터 100개가지 반복을 돌며 회문을 찾고,
딕셔너리에 key에는 회문을 value에는 회문의 길이를 넣어
value값만 순회하며 최댓값을 찾아냈다.
'''

T = 10
for tc in range(1, T+1):
    print('#{}'.format(tc), end=" ")

    number = int(input())
    arr = list(input() for _ in range(100))
    # 회문과 회문의 길이를 담을 딕셔너리를 만든다.
    result = {}

    # 행 탐색
    # 100 * 100 table이기 때문에 범위를 100으로 주면서 완전탐색한다.
    for i in range(100):
        for j in range(100):
            # 회문의 길이가 1부터 100까지 가능하기때문에 슬라이싱 범위에 사용될 k를 2~101까지 반복을 돌린다.
            for k in range(2, 102):
                # i = 0, j = 0, k = 2라면,
                # arr[0][0:2]까지 슬라이싱한 후 회문인지 판단한다.(k=2 -> 회문의 길이 == 1)
                if arr[i][j:j+k] == arr[i][j:j+k][::-1]:
                    # 회문이라면, 회문의 길이를 구하고
                    length = len(arr[i][j:j+k])
                    # result에 key=회문, value=회문 길이로 넣어준다.
                    result[arr[i][j:j+k]] = length
    # 열 탐색
    # 열은 슬라이싱을 사용할 수 없다.
    # 그러므로 열 값을 따로 담은 리스트를 새로 만들자.

    # 2차원 리스트 변수를 만든다.
    column = []
    # 완전탐색으로 열을 c_lst에 담는다.
    for i in range(100):
        c_lst = []
        for j in range(100):
            c_lst.append(arr[j][i])
        # c_lst를 column리스트에 담아준다.
        # [ [""], [""], [""].... ]
        column.append(c_lst)

    # 행과 같은 방법으로 회문을 찾는다.
    for i in range(100):
        for j in range(100):
            for k in range(2, 102):
                if column[i][j:j+k] == column[i][j:j+k][::-1]:
                    length = len(column[i][j:j+k])
                    result["".join(column[i][j:j+k])] = length
    # result의 value 값을 순회하면서 초댓값을 찾아준다.
    max_value = 0
    for key, value in result.items():
        if max_value < value:
            max_value = value
    # 최댓값을 출력한다.
    print(max_value)