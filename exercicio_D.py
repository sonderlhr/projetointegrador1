valor = float(input("Digite o valor original da prestação: "))
taxa = float(input("Digite a taxa de juros mensal (%): "))
unidade = input("O tempo está em dias (D) ou meses (M)? ").upper()

tempo = float(input("Digite o tempo de atraso: "))

if unidade == "D":
    tempo = tempo / 30

prestacao = valor + (valor * (taxa / 100) * tempo)

print(f"O valor atualizado da prestação é: R$ {prestacao:.2f}")