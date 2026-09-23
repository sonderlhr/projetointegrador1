A = int(input('Digite o primeiro valor: '))
B = int(input('Digite o segundo valor: '))
C = int(input('Digite o terceiro valor: '))

maior = A

maior = max(maior, B)

maior = max(maior, C)

print(f'O maior valor é: {maior}')