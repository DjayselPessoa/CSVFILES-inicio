import csv
from csv import writer


active = True
while active:
    try:
        nome = []
        idade = []
        valor = []
        di = []

        for d in csv.DictReader(open('PYTHON\projetos\PFNoobs\Opening\SAVE.csv'), delimiter=','):
            nome.append(d["NOME"])
            idade.append(d["IDADE"])
            valor.append(d["VALOR"])
            di.append(d["ID"])

        nomeSTR = str
        idadeSTR = str
        diSTR = str
        valorSTR = str

        cod = 0
        cont1 = 0
        lugar1 = 0

        entradaNome = str(input("Informe nome: "))
        entradaId = str(input("Informe id: "))
        entradaCriar = str(input("Entrar - Criar - Sair - Printar -> "))
        valorInicial = "0.0"
        lugar = 0

        if entradaCriar in "criar":
            position = "#" + str((len(di)) + 1)
            print(position)
            criandoIdade = str(input("Informe sua idade: "))
            with open('PYTHON\projetos\PFNoobs\Opening\SAVE.csv', 'a+', newline='\n') as escreverFile:
                data = [(entradaNome), (criandoIdade), (position), (valorInicial)]
                print(data)
                d2 = writer(escreverFile)
                d2.writerow(data)
            escreverFile.close()
            print("PROFILE CRIADO!")
        elif entradaCriar in "entrar":
            for i in nome:
                testeNome = nome[cont1]
                # print("testeNome", testeNome)
                if testeNome == entradaNome:
                    lugar1 = cont1
                    print("Nome encontrado!")
                    if di[lugar1] == entradaId:
                        print("ID encontrada!")
                        print("Sua entrada foi permitida!")
                        nomeSTR = nome[lugar1]
                        idadeSTR = idade[lugar1]
                        valorSTR = valor[lugar1]
                        print(f"{nomeSTR} - Sua entrada foi permitida! Você tem {idadeSTR} anos e {valorSTR} reais")
                        raise ValueError("REINICIANDO!")
                    else:
                        cont1 += 1
                        continue
                else:
                    cont1 += 1
                    continue
            if cont1 == len(nome):
                        print("Entrada não permitida!")
                        raise ValueError("REINICIANDO!")
        elif entradaCriar in "sair":
            print("Seus dados estão salvos!")
            active = False
            raise ValueError("DESLIGANDO!")

        elif entradaCriar in "printar":
            # ainda n sei o motivo de não mostrar a ultima atualização sem ter de recomeçar o codigo
            print("NOME = ", nome)
            print("IDADE = ", idade)
            print("VALOR = ", valor)
            print("ID = ", di)

    except ValueError as e:
        print("LOG: -> ", e)
