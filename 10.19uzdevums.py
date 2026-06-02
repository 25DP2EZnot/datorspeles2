a = [['0' for kolona in range(10)] for rinda in range(10)]

print("--- KUĢU IZVIETOŠANA ---")

for m in range(10):
    i = int(input(f"Pirmais spēlētāj, ievadi {m + 1}. kuģa x koordinātu (0 līdz 9): "))
    j = int(input("Ievadi y koordinātu (0 līdz 9): "))
    a[i][j] = "k"

for attirit in range(100):
    print()

print("--- ŠAUŠANAS FAZE ---")
trap = 0

for m in range(10):
    i = int(input(f"Otrais spēlētāj, ievadi {m + 1}. šāviena x koordinātu (0 līdz 9): "))
    j = int(input("Ievadi y koordinātu (0 līdz 9): "))

    if a[i][j] == "k":
        trap += 1
        a[i][j] = "x"
    else:
        a[i][j] = "m"

print("\n--- REZULTĀTI ---")

for i in range(10):
    for j in range(10):
        print(a[i][j], end=" ")
    print()

print()

print(f"Iznīcināti {trap} kuģi!") 