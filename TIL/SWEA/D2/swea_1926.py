N = int(input())
lst = ['3', '6', '9']
for i in range(1, N+1):
    for j in str(i):
        if j in lst:
            if lst.count(j) == 1:
                i = '-'
            elif lst.count(j) == 2:
                i = '--'
            elif lst.count(j) == 3:
                i = '---'
            # print('-', end=" ")

    print(i, end=" ")