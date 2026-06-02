a = [[0] * 5 for _ in range(4)]

for x in range(0, 4):
    for y in range(0, 5):
        print("Ievadiet ", x+1,". šofera ", y+1,". dienas,", sep="")
        a[x][y] = float(input("nobrauktos kilametrus, aiz komata, vai pilnos: "))

print()
print("Pirmā līdz piektā dienas")

for i in range(0, 4):
    print(i+1, ". šoferis: ", sep="", end="")
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

print("1. šoferis nobrauca vidēji: ", sum1/5,"km", sep="")
print("2. šoferis nobrauca vidēji: ", sum2/5,"km", sep="")
print("3. šoferis nobrauca vidēji: ", sum3/5,"km", sep="")
print("4. šoferis nobrauca vidēji: ", sum4/5,"km", sep="")
print()