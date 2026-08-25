# Exercício D - Raio e Área do Círculo
# Constante
PI = 3.14
# Entrada de dados
perimetro = float(input("Digite o valor do perímetro: "))
# Processamento
diametro = perimetro / PI
raio = diametro / 2
area = raio * raio * PI
# Saída de dados
print(f"A área é: {area:.2f}")
