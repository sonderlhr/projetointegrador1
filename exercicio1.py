import math

NumLados = int(input('Digite o número de lados: '))
MedLado = float(input('Digite a medida do lado: '))

if NumLados < 3:
    print('NÃO É UM POLÍGONO')

elif NumLados == 3:
    print('TRIÂNGULO')

    s = (MedLado + MedLado + MedLado) / 2
    area = math.sqrt(s * (s - MedLado) * (s - MedLado) * (s - MedLado))

    print(f'A área do triângulo é: {area:.2f}')

elif NumLados == 4:
    print('QUADRADO')

    area = MedLado ** 2

    print(f'A área do quadrado é: {area:.2f}')

elif NumLados == 5:
    print('PENTÁGONO')

    area = (math.sqrt(5 * (5 + 2 * math.sqrt(5))) * MedLado ** 2) / 4

    print(f'A área do pentágono é: {area:.2f}')

else:
    print('POLÍGONO NÃO IDENTIFICADO')