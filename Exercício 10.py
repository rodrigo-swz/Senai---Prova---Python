import os
os.system("cls")

NomeFuncionario = input("Qual o nome do funcionário?")
ValorHora = float(input("Quanto o funcionário recebe por hora trabalhada?"))
HorasTrabalhadas = float(input("Quantas horas o funcionário trabalhou?"))
ValorPagamento = HorasTrabalhadas * ValorHora

print(f"O funcionário {NomeFuncionario}, recebe R$ {ValorHora:.2f} por hora trabalhada, ele trabalhou o total de {HorasTrabalhadas} horas, logo o pagamento devido é de R$: {ValorPagamento:.2f}!")