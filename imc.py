def imcc(peso, altura):
    res = peso / altura **2
    
    if res <= 18.5:
        imc_situa = "peso abaixo do esperado"
    elif res > 18.5 and res <= 24.9:
        imc_situa = "o peso normal"
    elif res > 24.9 and res <= 29.9:
        imc_situa = "sobrepeso"
    elif res > 29.9 and res <= 34.9:
        imc_situa = "obesidade grau I"
    elif res > 34.9 and res <= 39.9:
        imc_situa = "obesidade grau II"
    else:
        imc_situa = "obesidade grau III"
    return res, imc_situa