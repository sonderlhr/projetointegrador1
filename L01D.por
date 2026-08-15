Algoritmo "L01D"

Var
   TEMPO, VELOCIDADE, DISTANCIA, LITROS_USADOS: Real

Inicio
   Escreva("Digite o tempo da viagem: ")
   Leia(TEMPO)

   Escreva("Digite a velocidade média: ")
   Leia(VELOCIDADE)

   DISTANCIA <- TEMPO * VELOCIDADE
   LITROS_USADOS <- DISTANCIA / 12

   Escreval("Velocidade média: ", VELOCIDADE)
   Escreval("Tempo gasto: ", TEMPO)
   Escreval("Distância percorrida: ", DISTANCIA)
   Escreval("Litros utilizados: ", LITROS_USADOS)
Fimalgoritmo