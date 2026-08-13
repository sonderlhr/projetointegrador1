tempo = float(input("Digite o tempo gasto na viagem (horas): "))
velocidade = float(input("Digite a velocidade média (km/h): "))

distancia = tempo * velocidade
litros_usados = distancia / 12

print(f"Velocidade Média: {velocidade} km/h")
print(f"Tempo Gasto: {tempo} horas")
print(f"Distância Percorrida: {distancia} km")
print(f"Litros Utilizados: {litros_usados}")