import sys
sys.stdin = open('input_4047.txt')
T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc), end=" ")

    cards = input()
    cnt = [[0] * 13 for _ in range(4)]
    cardType = {'S':0, 'D':1, 'H':2, 'C':3}
    for i in range(0, len(cards), 3):
        if cards[i] == 'S':
            cnt[cardType[cards[i]]][int(cards[i + 1:i + 3])-1] += 1
        if cards[i] == 'D':
            cnt[cardType[cards[i]]][int(cards[i + 1:i + 3])-1] += 1
        if cards[i] == 'H':
            cnt[cardType[cards[i]]][int(cards[i + 1:i + 3])-1] += 1
        if cards[i] == 'C':
            cnt[cardType[cards[i]]][int(cards[i + 1:i + 3])-1] += 1

    ans = 0
    sum_list = []
    for i in cnt:
        sumV = 0
        for j in i:
            if j == 0:
                sumV += 1
            if j > 1:
                ans = 1
                break
        if ans == 1:
            break
        sum_list.append(sumV)
    if len(sum_list) != 4:
        print('ERROR')
    else:
        for i in sum_list:
            print(i, end=" ")
        print()