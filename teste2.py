import csv

nome = []
idade = []
valor = []

for d in csv.DictReader(open('PYTHON\projetos\PFNoobs\Opening\SAVE.csv'), delimiter=','):
    nome.append(d["NOME"])
    idade.append(d["IDADE"])
    valor.append(d["VALOR"])

print("NOME = ", nome)
print("IDADE = ", idade)
print("VALOR = ", valor)
nomeSTR = nome[0]
idadeSTR = idade[0]
valorSTR = valor[0]
print(f"{nomeSTR} - Sua entrada foi permitida! Você tem {idadeSTR} anos e {valorSTR} reais")
