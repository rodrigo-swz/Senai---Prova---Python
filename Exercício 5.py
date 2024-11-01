import os
os.system("cls")

Materia1 = input("Qual a primeira matéria?")
Nota11 = float(input("Digite a primeira nota da primeira matéria:"))
Nota12 = float(input("Digite a segunda nota da primeira matéria:"))
Nota13 = float(input("Digite a terceira nota da primeira matéria:"))

Materia2 = input("Qual a segunda matéria?")
Nota21 = float(input("Digite a primeira nota da segunda matéria:"))
Nota22 = float(input("Digite a segunda nota da segunda matéria:"))
Nota23 = float(input("Digite a terceira nota da segunda matéria:"))

Materia3 = input("Qual a terceira matéria?")
Nota31 = float(input("Digite a primeira nota da terceira matéria:"))
Nota32 = float(input("Digite a segunda nota da terceira matéria:"))
Nota33 = float(input("Digite a terceira nota da terceira matéria:"))

Media1 = (Nota11 + Nota12 + Nota13) /3
Media2 = (Nota21 + Nota22 + Nota23) /3
Media3 = (Nota31 + Nota32 + Nota33) /3

Status1 = str
Status2 = str
Status3 = str

if Media1 >= 7:
    Status1 = "Aluno aprovado!"
else:
    Status1 = "Aluno de recuperação!"

if Media2 >= 7:
    Status2 = "Aluno aprovado!"
else:
    Status2 = "Aluno de recuperação!"

if Media3 >= 7:
    Status3 = "Aluno aprovado!"
else:
    Status3 = "Aluno de recuperação!"

print(f"Média da Matéria {Materia1}: {Media1:.2f}, Status do aluno: {Status1}!")
print(f"Média da Matéria {Materia2}: {Media2:.2f}, Status do aluno: {Status2}!")
print(f"Média da Matéria {Materia3}: {Media3:.2f}, Status do aluno: {Status3}!")


