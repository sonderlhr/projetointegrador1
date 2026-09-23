import math

A = float(input('Digite o lado A: '))
B = float(input('Digite o lado B: '))
C = float(input('Digite o lado C: '))

s = (A + B + C) / 2

area = math.sqrt(s * (s - A) * (s - B) * (s - C))

print(f'Semiperímetro: {s:.2f}')
print(f'Área do triângulo: {area:.2f}')