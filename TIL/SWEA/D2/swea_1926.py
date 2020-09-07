N = int(input())
lst = []
while N != 0:
    if N // 10 == 3 or N // 10 == 6 or N // 10 == 9:
        if N % 10 == 3 or N % 10 == 6 or N % 10 == 9:
            lst.append('-'*2)
        else:
            lst.append('-')
        N -= 1
    elif N % 10 == 3 or N % 10 == 6 or N % 10 == 9:
        lst.append('-')
        N -= 1
    else:
        lst.append((N // 10)* 10 + (N % 10))
        N -= 1
for i in lst[::-1]:
    print(i,end=" ")