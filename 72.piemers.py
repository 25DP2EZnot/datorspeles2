N = 2
M = 3

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