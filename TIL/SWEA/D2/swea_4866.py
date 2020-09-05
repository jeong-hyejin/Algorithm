'''
input을 순호하면서 '('과 '{'이면 stack에 push
')'과 '}'이면 1. 스택이 비어 있지 않고 2. stack의 마지막 값이 짝이 맞다면 pop!
stack이 비어있지 않으면 0을 리턴하고 비어있다면 1을 리턴
'''

T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc), end=" ")
    def check(arr):
        stack = []
        for i in arr:
            # if i == '(' or c == '{':
            # stack.append(i)
            if i == '(':
                stack.append(i)
            elif i == '{':
                stack.append(i)

            elif i == ')':
                if stack:
                    if stack[-1] == '(':
                        stack.pop(-1)
                        continue
                    if stack[-1] == '{':
                        return 0
                else:
                    return 0
            elif i == '}':
                if stack:
                    if stack[-1] == '{':
                        stack.pop(-1)
                        continue
                    if stack[-1] == '(':
                        return 0
            else:
                continue
        if stack:
            return 0
        else:
            return 1

    arr = input()
    print(check(arr))