import os
os.system("cls")

AnoNascimento = int(input("Digite a sua data de nascimento:"))
AnoAtual = int(input("Digite qual ano atual:"))
Idade = AnoAtual - AnoNascimento

if Idade >= 18:
    print(f"Você tem {Idade} anos! Já pode tirar a CNH e Votar!")
elif Idade >=16 and Idade == 17:
    print(f"Você tem {Idade} anos! Já pode Votar, mas ainda não pode tirar a CNH!")
else:
    print(f"Você não tem idade suficiente pra votar ou tirar CNH!")