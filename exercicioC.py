import math
# Exercício C - Tempo de Queda
# Constante
G = 9.8
# Entrada de dados
altura = float(input("Digite o valor da altura: "))
# Processamento
tq = math.sqrt((2 * altura) / G)
# Saída de dados
print(f"O Tempo de Queda (TQ) é: {tq:.2f} segundos")