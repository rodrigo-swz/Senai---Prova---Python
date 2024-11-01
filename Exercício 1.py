import os
os.system("cls")

Nome1 = input("Qual o nome da primeira pessoa?")
Nome2 = input("Qual o nome da segunda pessoa?")
Idade1 = int(input("Qual a idade da primeira pessoa?"))
Idade2 = int(input("Qual a idade da segunda pessoa?"))
Media = Idade1 + Idade2
print(f"A idade media de {Nome1} e {Nome2} é de {Media:.1f}")

