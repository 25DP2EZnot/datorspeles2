t = [[-2,-1, 0, 5],
     [ 5, 2, 5, 7],
     [ 3, 1, 4, 6]] 

print ('Riga 4. diena bija',t[1][3],'gradi')
print ('Liepaja 1. diena bija',t[2][0],'gradi')
print ()

for indekss in range(3):
    print ('Otraja diena', indekss + 1,'. stacija temperatura bija',t[indekss][1])
print ()

summa = 0
for j in range(4):
    summa += t[2][j]

print (f'Videja temperatura Liepaja ir {summa/4:0.3f} gradi.')
print ()

for rinda in range(3):
    for kolonna in range(4):
        if t[rinda][kolonna] >= -2 and t[rinda][kolonna] <= 2:
            print ('Stacija Nr.', rinda + 1, 'tada temperatura bija', kolonna + 1,'. diena.')
print () 

for rinda in range(3):
    for kolona in range(4):
        print (f'{t [rinda][kolonna]:3d}', end='')
print ()