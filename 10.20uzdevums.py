N = 2
M = 2

a = [ [0 for kolona in range(M)] for rinda in range(N) ]

print ('Ievadi masīva vērtības:')

for i in range(N):
    print ('Ievadi rindas vērtības:')
    for j in range(M):
        a[i][j] = int(input('indeksi ' + str(i) + ',' + str(j) + ' '))

print () 

print (' Tabula')

for i in range(N):
    for j in range(M):
        print (f'{a[i][j]:6d} ', end = '')
    print()

print("y vērtība, kur y = a*b-b*c, ir", a[0][0]*a[0][1]-a[0][1]*a[1][0])