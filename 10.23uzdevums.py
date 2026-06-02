from random import randint

M = [[0] * 10 for _ in range(10)]

cx = 0
co = 0

while cx < 10 or co < 10:
    x = randint(0, 9)
    y = randint(0, 9)

    if M[x][y] == 0:
        if cx < 10:
            M[x][y] = 1
            cx += 1
        elif co < 10:
            M[x][y] = 2
            co += 1

for x in range(10):
    for y in range(10):
        if M[x][y] == 0:
            print(".", end=" ")
        elif M[x][y] == 1:
            print("X", end=" ")
        else:
            print("O", end=" ")
    print()

print()

x = int(input("no augsas uz leju (0-9): "))
y = int(input("no kreisās uz labo (0-9): "))

if M[x][y] == 0:
    print("Tukša")
elif M[x][y] == 1:
    print("X")
else:
    print("O")

cxn = 0
con = 0

for i in range(x-1, x+2):
    for j in range(y-1, y+2):
        if 0 <= i < 10 and 0 <= j < 10:
            if not (i == x and j == y):
                if M[i][j] == 1:
                    cxn += 1
                elif M[i][j] == 2:
                    con += 1

print("Blakus X:", cxn)
print("Blakus O:", con)
print()