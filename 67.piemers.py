from random import randint

mas = [[0.0, 0.0, 0.0, 0.0],
       [0.0, 0.0, 0.0, 0.0],
       [0.0, 0.0, 0.0, 0.0]]  

for x in range(3):
    for y in range(4):
        mas[x][y] = randint(0,20)
        print (f'{mas[x][y]:5.1f}', end='')
    print()

print() 

for x in range(3):
    for y in range(4):
        mas[x][y] = mas[x][y] / 2
        print (f'{mas[x][y]:5.1f}', end='')
print() 