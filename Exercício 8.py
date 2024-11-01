import os
os.system("cls")

Altura = float(input("Digite sua altura:"))
Sexo = input("Qual o seu sexo? Digite M para masculino e F para feminino.")
PesoM = (72.7 * Altura) - 52
PesoF = (62.1 * Altura) - 38

if Sexo == "M" or Sexo == "m": #Tentei usar o OR para colocar a opção de minísculo, pra testes.
    Sexo = "Masculino"
    print(f"O peso ideal para sua altura de {Altura}, Sexo {Sexo} é : {PesoM} Kgs!")
elif Sexo == "F" or Sexo=="f": #Tentei usar o OR para colocar a opção de minísculo, pra testes.
    Sexo = "Feminino"
    print(f"O peso ideal para sua altura de {Altura}, Sexo {Sexo} é : {PesoF} Kgs!")
else:
    print("Sexo inválido, tente novamente!")