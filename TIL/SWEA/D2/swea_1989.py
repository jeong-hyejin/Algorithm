import sys
sys.stdin = open('input_1989.txt')
T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc), end=" ")
    words = input()
    while len(words) > 0:
        if words[0] == words[len(words)-1]:
            words = words[1:len(words)-1]
            if len(words) == 1 or len(words) == 0:
                print(1)
                break
        else:
            print(0)
            break
