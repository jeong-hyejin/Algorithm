T = int(input())
for tc in range(1, T+1):
    numbers = list(map(int, input().split()))
    numbers_sum = sum(numbers)
    print(f'#{tc} {round(numbers_sum / len(numbers))}')