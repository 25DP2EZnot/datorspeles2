a = [[0] * 5 for _ in range(4)]

for x in range(0, 4):
    for y in range(0, 5):
        print("Ievadiet ", x+1,". veikala ", y+1,". dienas,", sep="")
        a[x][y] = float(input("nopelnītās peļņas summu Euro: "))

print()
print("Pirmā līdz piektā dienas")

for i in range(0, 4):
    print(i+1, ". veikals: ", sep="", end="")
    for j in range(0, 5):
        print (str(int(a[i][j]))+' ', end="")
    print()

print()

sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0

for y in range(0, 5):
    sum1 += a[0][y]
    sum2 += a[1][y]
    sum3 += a[2][y]
    sum4 += a[3][y]

print("1. veikals vidēji nopelnīja peļņas: ", sum1/5,"Euro", sep="")
print("2. veikals vidēji nopelnīja peļņas: ", sum2/5,"Euro", sep="")
print("3. veikals vidēji nopelnīja peļņas: ", sum3/5,"Euro", sep="")
print("4. veikals vidēji nopelnīja peļņas: ", sum4/5,"Euro", sep="")
print()