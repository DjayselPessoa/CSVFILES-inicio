import csv
from os import close

nome = []
idade = []
valor = []
di = []
usuarios = ["DJ", "EF"]

for d in csv.DictReader(open('PYTHON\projetos\PFNoobs\Opening\SAVE.csv'), delimiter=','):
    nome.append(d["NOME"])
    idade.append(d["IDADE"])
    valor.append(d["VALOR"])
    di.append(d["ID"])

print("NOME = ", nome)
print("IDADE = ", idade)
print("VALOR = ", valor)
print("ID = ", di)

nomeSTR1 = nome[0]
idadeSTR1 = idade[0]
valorSTR1 = valor[0]
diSTR1 = di[0]
nomeSTR2 = nome[1]
idadeSTR2 = idade[1]
valorSTR2 = valor[1]
diSTR2 = di[1]

cod = 0

entradaNome = str(input("Informe nome: "))
entradaId = str(input("Informe id: "))

for i in nome:
    if cod == 1 or cod == 2:
        print("Saindo!")
        break
    if entradaNome == nomeSTR1:
        print("Nome 1 confirmado!")
        for i in di:
            if entradaId == diSTR1:
                print("Id confirmada!")
                if diSTR1 == "#01":
                    cod = 1
                    break
            if i == len(di):
                print("Sua id não foi confirmada!")
                break
    elif entradaNome == nomeSTR2:
        print("Nome 2 confirmado!")
        for i in di:
            if entradaId == diSTR2:
                print("Id confirmada!")
                if diSTR2 == "#02":
                    cod = 2
                    break
            if i == len(di):
                print("Sua id não foi confirmada!")
                break
    if i == len(nome):
        print("Seu nome não foi confirmado!")
        break
if cod == 1:
    print(f"{nomeSTR1} - Sua entrada foi permitida! Você tem {idadeSTR1} anos e {valorSTR1} reais")
elif cod == 2:
    print(f"{nomeSTR2} - Sua entrada foi permitida! Você tem {idadeSTR2} anos e {valorSTR2} reais")
