# 1
number = int(input())
result = 0
for num in range(1, number+2):
    if num == 1:
        result = 1

    else:
        result = result * 2
    print(result, end=' ')

# 2
number = int(input())
for num in range(number+1):
    print(2 ** num, end=' ')