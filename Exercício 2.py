import os
os.system("cls")

Base = float(input("Qual a base do retângulo?"))
Altura = float(input("Qual a altura do retângulo?"))

Area = Base * Altura
Perimetro = 2*Base + 2*Altura
Diagonal = (Base**2 + Altura**2) ** 0.5 #Utilizei a exponenciação por 0.5 ao invés de importar o math, achei mais simples.

print(f"Perímetro: {Perimetro:.2f} metros, Área: {Area:.2f} metros², e Diagonal de {Diagonal:.2f}!")