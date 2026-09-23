import math

A = float(input('Digite o valor de A: '))
B = float(input('Digite o valor de B: '))
C = float(input('Digite o valor de C: '))

if A == 0:
    print('O valor de A deve ser diferente de zero.')

else:
    delta = B * B - 4 * A * C

    print(f'A = {A}')
    print(f'B = {B}')
    print(f'C = {C}')
    print(f'Delta = {delta}')

    if delta >= 0:
        X1 = (-B + math.sqrt(delta)) / (2 * A)
        X2 = (-B - math.sqrt(delta)) / (2 * A)

        print(f'X1 = {X1:.2f}')
        print(f'X2 = {X2:.2f}')

    else:
        print('Sem solução no conjunto dos números Reais!')