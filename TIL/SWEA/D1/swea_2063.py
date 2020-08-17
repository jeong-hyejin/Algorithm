N = int(input())
numbers = list(map(int, input().split()))
numbers_median = sorted(numbers)[len(numbers)//2]
print(numbers_median)
