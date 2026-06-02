from random import randrange

n = int(input("Ievadi rindu skaitu: "))
m = int(input("Ievadi kolonnu skaitu: "))

divdimensiju_masivs_A = [[randrange(100) for _ in range(m)] for _ in range(n)]

print("\nMasīva izvade tabulas veidā:")

for i in range(n):
    for j in range(m):
        print(f"{divdimensiju_masivs_A[i][j]:4d}", end="")
    print()