tmp = [[1, 2, 3], [4, 5], [9, 8, 7]]
tmp.append([6, 9, 2])

# i[0] [1, 2, 3]
# i[1] [4, 5]
# i[2] [9, 8, 7]...

print(tmp[1][1])

for i in tmp:
    print(*i)


# То что будет в задаче (скорее всего)
def pl(t):
    for i in t:
        print(*i)

n = int(input())
tmp = []

for i in range(n):
    a = list(map(int, input().split()))
    tmp.append(a)

pl(tmp)


#
tmpp = [[1 for i in range(7)] for i in range(5)]
pl(tmpp)


# Задача
x = int(input())
y = int(input())

house = [[0 for i in range(y)] for i in range(x)]
cnt = 1

for i in range(-1, -x - 1, -1):
    if i % 2 == 1:
        for j in range(y):
            house[i][j] = cnt
            cnt += 1
    else:
        for j in range(-1, -y - 1, -1):
            house[i][j] = cnt
            cnt += 1

pl(house)