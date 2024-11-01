import os
os.system("cls")


NA = input("Qual o nome do aluno?")
NB = float(input("Qual a nota do aluno?"))
Nmat = input("Qual o nome da matéria?")
Sx = input("Qual o sexo do aluno? Digite M para masculino e F para feminino.")

if Sx == "M":
        Sx = "Masculino"
elif Sx == "F":
        Sx = "Feminino"
else:
        Sx = "Sexo inválido"

print(f"Aluno: {NA}, Nota: {NB}, Matéria: {Nmat}, Sexo: {Sx}.")