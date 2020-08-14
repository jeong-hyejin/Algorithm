T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    new_lst = []
    for i in range(0, len(arr)):
        lst = []
        for j in range(0, len(arr)):
            lst.append(arr[j][i])
            
        new_lst.append(lst)
        
    num_list = []
    for i in new_lst:
        num_list.append(i[::-1])

    new_lst2 = []
    for k in range(0, N):
        lst2 = []
        for l in range(0, N):
            lst2.append(num_list[l][k])
        new_lst2.append(lst2)

    num_list2 = []
    for i in new_lst2:
        num_list2.append(i[::-1])
        num_list.append(i[::-1])

    new_lst3 = []
    for k in range(0, N):
        lst3 = []
        for l in range(0, N):
            lst3.append(num_list2[l][k])
        new_lst3.append(lst3)

    num_list3 = []
    for i in new_lst3:
        num_list3.append(i[::-1])
        num_list.append(i[::-1])

    print('#{}'.format(tc))
    for i in range(0, N):
        for j in num_list[i:len(num_list):N]:
            j.append(" ")
            for k in j:
                print(k, end='')
        print()