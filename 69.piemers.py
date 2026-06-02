from random import randrange

n = int(input("Ievadi rindu skaitu: "))
m = int(input("Ievadi kolonnu skaitu: "))

divdimensiju_masivs_A = [[randrange(100) for _ in range(m)] for _ in range(n)]

print("\nMasīva izvade tabulas veidā:")

for i in range(n):
    for j in range(m):
        print(f"{divdimensiju_masivs_A[i][j]:4d}", end="")
    print()

visi_skaitli = [skaitlis for rinda in divdimensiju_masivs_A for skaitlis in rinda]

Kopeja_summa = sum(visi_skaitli)
videja_vertiba = Kopeja_summa / len(visi_skaitli)
max_skaitlis = max(visi_skaitli)
min_skaitlis = min(visi_skaitli)

print("\nStatistikas rādītāji:")
print(f"Kopējā elementu summa: {Kopeja_summa}")
print(f"Vidējā vērtība: {videja_vertiba:.2f}")
print(f"Lielākais skaitlis (Max): {max_skaitlis}")
print(f"Mazākais skaitlis (Min): {min_skaitlis}")