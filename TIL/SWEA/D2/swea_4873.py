'''
input값을 순회하면서 맨 처음 값은 stack에 push하고
그 다음 값이 stack에 들어있는 값이라면 현재 stack에 들어있는 값을 pop하고
아니라면 push한다.
'''
T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc), end=" ")
    def delete(s):
        # 빈 stack을 만들어주고
        stack = []
        # input값을 순회하면서 한 글자씩 중복된 값인지 확인
        for i in s:
            # 맨 처음 값은 무조건 stack에 넣고
            if len(stack) == 0:
                stack.append(i)
                continue
            # 그 다음 값부터 stack에 들어있는 값과 중복된 값인지 확인.
            # 연속된 값이 중복인지 확인해야하므로 stack의 맨 마지막값과 비교한다.
            else:
                # 글자가 stack의 맨 마지막값과 같다면
                # stack의 마지막 값을 pop하고
                if i == stack[-1]:
                    stack.pop()
                    continue

                # 아니라면 stack에 push한다.
                else:
                    stack.append(i)
                    continue
        # stack이 비어있지않다면 stack의 길이를 리턴하고
        if stack:
            return len(stack)
        # stack이 비어있다면 0을 리턴한다.
        else:
            return 0

    s = input()
    print(delete(s))