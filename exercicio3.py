A = int(input('Digite o lado A: '))
B = int(input('Digite o lado B: '))
C = int(input('Digite o lado C: '))

if A >= (B + C) or B >= (A + C) or C >= (A + B):
    print('NÃO É UM TRIÂNGULO')

elif A == B and B == C:
    print('EQUILÁTERO')

elif A == B or A == C or B == C:
    print('ISÓSCELES')

else:
    print('ESCALENO')