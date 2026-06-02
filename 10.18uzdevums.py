a = [['0' for kolona in range(3)] for rinda in range(3)]

print("--- KUĢU IZVIETOŠANA ---")

for m in range(3):
    i = int(input(f"Pirmais spēlētāj, ievadi {m + 1}. kuģa x koordinātu (0 līdz 2): "))
    j = int(input("Ievadi y koordinātu (0 līdz 2): "))
    a[i][j] = "k"

for attirit in range(100):
    print()

print("--- ŠAUŠANAS FAZE ---")
trap = 0

for m in range(3):
    i = int(input(f"Otrais spēlētāj, ievadi {m + 1}. šāviena x koordinātu (0 līdz 2): "))
    j = int(input("Ievadi y koordinātu (0 līdz 2): "))

    if a[i][j] == "k":
        trap += 1
        a[i][j] = "x"
    else:
        a[i][j] = "m"

print("\n--- REZULTĀTI ---")

for i in range(3):
    for j in range(3):
        print(a[i][j], end=" ")
    print()

print()

print(f"Iznīcināti {trap} kuģi!") 