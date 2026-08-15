Algoritmo "L01E"

Var
   VALOR, TAXA, TEMPO, PRESTACAO: Real

Inicio
   Escreva("Digite o valor da prestação: ")
   Leia(VALOR)

   Escreva("Digite a taxa (%): ")
   Leia(TAXA)

   Escreva("Digite o tempo de atraso: ")
   Leia(TEMPO)

   PRESTACAO <- VALOR + (VALOR * TAXA / 100 * TEMPO)

   Escreval("Valor da prestação: ", PRESTACAO)
Fimalgoritmo