# Exercício B - Distância de um Raio
# Definição de constante
VELOCIDADE_SOM = 340  # m/s
# Entrada de dados
tempo = float(input("Digite o tempo decorrido em segundos entre o raio e o som: "))
# Processamento
distancia = tempo * VELOCIDADE_SOM
# Saída de dados
print(f"A distância aproximada do raio é: {distancia:.2f} metros")