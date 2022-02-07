#백준 1002

t = int(input())
lists = [list(map(int, input().split())) for _ in range(t)]

for i in lists:
    x1 = i[0]
    y1 = i[1]
    r1 = i[2]
    x2 = i[3]
    y2 = i[4]
    r2 = i[5]
    if x1 == x2 and y1 == y2 and r1 != r2:
        print(0)
    elif x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    elif ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2) == (r1 + r2):
        print(1)
    elif ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2) == abs(r1 - r2):
        print(1)
    elif ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2) > (r1 + r2):
        print(0)
    elif ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)  < abs(r1 - r2):
        print(0)
    else:
        print(2)
