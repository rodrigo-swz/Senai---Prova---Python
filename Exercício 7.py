import os
os.system("cls")

Nome = input("Qual o nome do cliente?")
CPF = input("Qual o CPF do cliente?")
Endereco = input("Qual o endereço do cliente?")
NumeroTelefone = input("Qual o telefone do cliente?")
NumeroPneu = float(input("Qual o número do pneu?"))
Marca = input("Qual a marca do pneu?")
Quantidade = int(input("Qual a quantidade de pneus comprada?"))
ValorUnidade = float(input("Qual o valor de cada pneu?"))
ValorCompra = Quantidade * ValorUnidade
Desconto = ValorCompra * 0.10 #Aqui eu poderia usar uma variável só pra JUROS e Desconto, mas achei mais didático assim pra organização.
Juros = ValorCompra * 0.10
ValorFinal = float
FormaPagamento = input("Qual a forma de pagamento? Digite 1 para À VISTA e 2 para PARCELADO (Compras à vista recebem 10% de desconto, e parcelado recebem 10% de juros.)")
QuantidadeParcela = int
if FormaPagamento =="1":
    FormaPagamento = "À vista"
    ValorFinal = ValorCompra - Desconto
    print(f"Dados do cliente: Cliente: {Nome}, CPF: {CPF}, endereço: {Endereco}, Número de telefone: {NumeroTelefone};")
    print(f"Dados da compra: Marca do(s) pneu(s): {Marca}, tamanho do(s) pneu(s): {NumeroPneu}, Quantidade: {Quantidade}, Valor por unidade: {ValorUnidade};")
    print(f"Dados sobre o pagamento: ValorCompra = R$ {ValorCompra}, Forma de pagamento: {FormaPagamento}, Desconto: R$ {Desconto}, valor final de pagamento devido: R$ {ValorFinal}. Agradecemos a preferência!")
elif FormaPagamento =="2":
    FormaPagamento = "Parcelado"
    QuantidadeParcela = int(input("Em quantas parcelas deseja pagar?(Máximo de 5)"))
    ValorFinal = ValorCompra + Juros
    ValorParcela = ValorFinal / QuantidadeParcela
    print(f"Dados do cliente: Cliente: {Nome}, CPF: {CPF}, endereço: {Endereco}, Número de telefone: {NumeroTelefone};")
    print(f"Dados da compra: Marca do(s) pneu(s): {Marca}, tamanho do(s) pneu(s): {NumeroPneu}, Quantidade: {Quantidade}, Valor por unidade: {ValorUnidade};")
    print(f"Dados sobre o pagamento: ValorCompra = R$ {ValorCompra:.2f}, Forma de pagamento: {FormaPagamento}, Quantidade de parcelas: {QuantidadeParcela}, Valor da parcela: R$ {ValorParcela:.2f} Juros: R$ {Juros:.2f}, valor final de pagamento devido: R$ {ValorFinal:.2f}. Agradecemos a preferência!")

else:
    print("Forma de pagamento inválida, tente novamente!")