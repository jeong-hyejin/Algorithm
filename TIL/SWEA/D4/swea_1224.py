isp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0} # 연산자 스택 우선순위
icp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 3} # 식에 있을 때 우선순위

for test_case in range(1, 11):
    N = int(input())
    data = []  # 후위 표기법
    calc = []  # 연산자
    # 중위 연산 -> 후위 연산
    for d in input():
        if d.isdigit():  # 숫자는 data로
            data.append(d)
        elif d == ')':
            # '(' 만날때 까지 data로 보내고 '(' 버림
            while data[-1] != '(':
                data.append(calc.pop())
            data.pop()
        else:
            # 스택안 연산자의 우낮선순위가 거나 같으면 pop해서 data로 보냄
            # 연산자 스택의 맨 위에 있는 연산자보다 들어갈 연산자의 우선순위가 더 작다면
            # 스택 안에 우선순위가 높은 연산자를 push해서 data 리스트에 append
            while calc and not icp[d] > isp[calc[-1]]:
                data.append(calc.pop())
            calc.append(d)
    while calc:  # 남은 연산자 data로
        data.append(calc.pop())

    # 후위 연산 계산
    stack = []
    for d in data:
        if d.isdigit():
            stack.append(int(d))
        elif d == '+':
            stack.append(stack.pop() + stack.pop())
        elif d == '*':
            stack.append(stack.pop() * stack.pop())

    # 결과
    print('#{} {}'.format(test_case, stack[0]))