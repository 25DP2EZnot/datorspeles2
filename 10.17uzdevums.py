t = [[-2,-1, 0, 5],
     [ 5, 2, 5, 7],
     [ 3, 1, 4, 6]]

min = 0
max = 0

for x in range(0, 3):
    for y in range(0, 4):
        if min > t[x][y]:
            min = t[x][y]
        else:
            if max < t[x][y]:
                max = t[x][y]

print("lielākās un mazākās tempertūras starpība ir", max-min, "grādi.")