import math

A = float(input('Digite o valor de A: '))
B = float(input('Digite o valor de B: '))
C = float(input('Digite o valor de C: '))

if A == 0:
    print('O valor de A deve ser diferente de zero.')
else:
    delta = B ** 2 - 4 * A * C

    if delta < 0:
        print('Não existem raízes reais para essa equação.')
    elif delta == 0:
        x = -B / (2 * A)
        print(f'A equação possui uma raiz real: {x:.2f}')
    else:
        x1 = (-B + math.sqrt(delta)) / (2 * A)
        x2 = (-B - math.sqrt(delta)) / (2 * A)

        print(f'A primeira raiz é: {x1:.2f}')
        print(f'A segunda raiz é: {x2:.2f}')