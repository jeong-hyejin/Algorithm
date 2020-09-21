N = int(input())
field = []
large_width = 0
large_height = 0
small_width = 0
small_height = 0
for i in range(6):
    idx, length = map(int, input().split())
    field.append(length)

for i in range(6):
    if i % 2:
        if field[i] > large_width:
            large_width = field[i]

    else:
        if field[i] > large_height:
            large_height = field[i]

for i in range(6):
    if i % 2 == 0:
        if large_width == field[(i+5)%6] + field[(i+1)%6]:
            small_height = field[i]
    else:
        if large_height == field[(i+5)%6] + field[(i+1)%6]:
            small_width = field[i]
area = (large_width * large_height) - (small_width * small_height)
print(area*N)
