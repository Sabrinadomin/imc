from datetime import date
import imc

def sys():
    print("Olá! Este programa vai te pedir algumas informações para saber qual sua idade e qual seu IMC!")  

    
    nome = str(input("Qual seu nome?"))
    data_nas = []
    nas = input("Qual ano que você nasceu? (Exemplo: 2001)")
    data_nas.append(nas)
    nas = input("Qual mês você nasceu? (Exemplo:03) ")
    data_nas.append(nas)
    altura = float(input("Qual sua altura? (Exemplo:1.80)"))
    peso = float(input("Qual seu peso?(Exemplo:68.5)"))
    
    data_hoje = []
    data = str(date.today())
    data_hoje = data
    data_hoje = data_hoje.split("-")

    fecha_ano = int(data_hoje[1]) - int(data_nas[1])
    ano_bruto = int(data_hoje[0]) - int(data_nas[0])

    if fecha_ano < 0:
        ano_bruto = ano_bruto - 1

    imcdone = imc.imcc(peso, altura)
    listreturn = list(imcdone)

    print(f"{nome} tem {ano_bruto} anos e seu IMC é {listreturn[0]:.2f} o que significa que você está com {listreturn[1]}. ")
    
while True:
    sys()