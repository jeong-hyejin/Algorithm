T = int(input())
for tc in  range(1, T+1):
    str1 = input()
    str2 = input()

    # str1이 str2에 몇개씩 들어가있는지 확인하기위해 딕셔너리를 사용한다.
    result = {}
    # str1의 문자를 key로 만들고 str2에 나온 횟수를 value로 만든다.
    # str1의 key를 순회하면서,
    for i in str1:
        cnt = 0
        # str2를 순회하면서 key를 비교한다.
        for j in str2:
        # str2의 key값과 같다면(str1의 key가 str2에 들어있다면)
            if i == j:
                # key에 해당하는 value값을 1씩 증가시킨다.
                cnt += 1
                # result 넣어준다.
                result[i] = cnt
    # 최댓값을 초기화시켜놓고,
    max_value = 0
    # result의 value 값들만 순회하면서
    for i in result.values():
        # 최댓값을 구해준다.
        if i > max_value:
            max_value = i
    # value의 최댓값을 출력한다.
    print('#{} {}'.format(tc, max_value))