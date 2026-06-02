komp = [[0.0 for kolona in range(3)] for rinda in range(3)]
vid = [0.0] * 3

paralelklases = ['a', 'b', 'c']
klasu_grupas = ['10.', '11.', '12.']

for i in range(3):
    print()
    print(f'Vērtējumi {klasu_grupas[i]} klasēm:')
    for j in range(3):
        print(f'{klasu_grupas[i]}{paralelklases[j]} klases vidējā atzīme: ', end='')
        komp[i][j] = float(input())

for i in range(3):
    summa = 0
    for j in range(3):
        summa += komp[i][j]
    vid[i] = summa/3

print()
print('Klašu grupu vidējā atzīme:')
for i in range(3):
    print(f'{klasu_grupas[i]:>4} klases: {vid[i]:6.2f}')

print()