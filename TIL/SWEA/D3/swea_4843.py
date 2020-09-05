T = int(input())
for tc in range(1, T+1):


    N = int(input())
    numbers = list(map(int, input().split()))

    for i in range(N):
        if i % 2 == 0:       # 0, 2, 4, 6, 8
            max = i
            for j in range(i+1, N):
                if numbers[max] < numbers[j]:
                    max = j

            numbers[i], numbers[max] = numbers[max], numbers[i]

        else:                # 1, 3, 5, 7, 9
            min = i
            for k in range(i+1, N):
                if numbers[min] > numbers[k]:
                    min = k
            numbers[i], numbers[min] = numbers[min], numbers[i]

    print('#{}'.format(tc), end=" ")
    for i in numbers[0:10]:
        print(i, end=" ")
    print()
