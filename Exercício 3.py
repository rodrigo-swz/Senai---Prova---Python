import os
os.system("cls")

Largura = float(input("Qual a largura do retângulo?"))
Comprimento = float(input("Qual o comprimento do retângulo?"))
ValorMetro = float(input("Qual o valor do metro² do terreno?"))

Area = Largura * Comprimento
ValorTotal = Area * ValorMetro

print(f"O valor total do terreno é R$ {ValorTotal:.2f}. Largura: {Largura:.1f} metros, Comprimento: {Comprimento:.1f} metros, Área total: {Area:.1f} metros², Valor do metro²: R$ {ValorMetro:.2f}.")