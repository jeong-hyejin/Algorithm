N, K = map(int, input().split())
info = [[] for _ in range(7)]
for i in range(N):
    student, grade = map(int, input().split())
    # grade를 인덱스로 활용
    info[grade].append(student)

total_room = 0
# G -> grade
# S -> student
for G in range(1, 7):
    cnt_m = 0
    cnt_f = 0
    for S in info[G]:
        # 남학생이면 cnt_m 증가
        if S == 1:
            cnt_m += 1
        # 여학생이면 cnt_f 증가
        else:
            cnt_f += 1
    # 각 각 구한 cnt에서 K를 빼주면서 total값 1씩 증가
    while cnt_m > 0:
        total_room += 1
        cnt_m = cnt_m - K
    while cnt_f > 0:
        total_room += 1
        cnt_f = cnt_f - K
print(total_room)