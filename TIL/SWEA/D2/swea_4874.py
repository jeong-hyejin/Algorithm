T = int(input())
for tc in range(1, T+1):
    data = list(input().split())
    stack = []
    # 예외처리를 위한 변수
    ans = 0
    # 마침표 제외하려고 data길이의 -1까지 반복
    for d in range(len(data)-1):
        # 숫자(피연산자)면 stack에 push
        # '0' <= data[d] <= '9'
        if data[d].isdigit():
            stack.append(data[d])
        # 연산자라면
        else:
            try:
                # stack에서 2개를 pop하고 연산자 계산 후 stack에 push
                num1, num2 = int(stack.pop()), int(stack.pop())
                if data[d] == '+':
                    stack.append(num1 + num2)
                elif data[d] == '-':
                    stack.append(num2 - num1)
                elif data[d] == '*':
                    stack.append(num1 * num2)
                elif data[d] == '/':
                    stack.append(num2 // num1)
            # 예외처리
            # 숫자 + 연산자 + 연산자
            except:
                ans = -1
        # 만약 ans가 -1 이거나 stack의 길이가 1보다 큰 경우 error 출력
    if ans == -1 or len(stack) >=2:
        print('#{} {}'.format(tc, 'error'))
    # 아니라면 stack[0] 출력
    else:
        print('#{} {}'.format(tc, stack[0]))
