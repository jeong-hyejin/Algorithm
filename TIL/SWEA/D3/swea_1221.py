arr = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc))
    No, N = input().split()
    s = input().split()
    # 2번째 방법
    # arr을 순회하면서 s에 몇개있는지 count를 센 후, count만큼 출력한다.
    for i in arr:
        print((i+' ')*s.count(i), end=" ")