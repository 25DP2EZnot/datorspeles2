a = [['0' for kolona in range(2)] for rinda in range(2)]

print("--- KUĢU IZVIETOŠANA ---")

for m in range(2):
    i = int(input(f"Pirmais spēlētāj, ievadi {m + 1}. kuģa x koordinātu (0 vai 1): "))
    j = int(input("Ievadi y koordinātu (0 vai 1): "))
    a[i][j] = "k"

for attirit in range(100):
    print()

print("--- ŠAUŠANAS FAZE ---")
trap = 0

for m in range(2):
    i = int(input(f"Otrais spēlētāj, ievadi {m + 1}. šāviena x koordinātu (0 vai 1): "))
    j = int(input("Ievadi y koordinātu (0 vai 1): "))

    if a[i][j] == "k":
        trap += 1
        a[i][j] = "x"
    else:
        a[i][j] = "m"

print("\n--- REZULTĀTI ---")

for i in range(2):
    for j in range(2):
        print(a[i][j], end=" ")
    print()

print()

print(f"Iznīcināti {trap} kuģi!")