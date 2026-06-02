import os
import time

C = "Elgars"

while C != "c":
    os.system('cls')

    a = [[0] * 3 for _ in range(3)]

    for x in range(0, 3):
        for y in range(0, 3):
            print (str(int(a[x][y]))+' ', end="")
        print()
    time.sleep(0.5)


    for x in range(0, 3):
        for y in range(0, 3):
            time.sleep(0.5)
            os.system('cls')
            
            for i in range(0, 3):
                for j in range(0, 3):
                    print (str(int(a[i][j]))+' ', end="")
                print()
            
            print("ieraksti skaitli, šūnā (", x, ",", y,"):", sep="")
            a[x][y] = int(input("vērtība: "))

    time.sleep(0.5)
    os.system('cls')

    all = 0

    for i in range(0, 3):
        for j in range(0, 3):
            print (str(int(a[i][j]))+' ', end="")
            all += a[i][j]
        print()

    print("Visu skaitļu summa ir ", all)
    C = str(input("Nospiec 'c', lai apstādinātu programmu: "))