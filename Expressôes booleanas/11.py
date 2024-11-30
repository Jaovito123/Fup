from re import fullmatch


def funcao(data):
    if data[2] == "/" and data[5] == "/":
        dia, mes, ano = data.split("/")
        if fullmatch(r'-?\d+', dia) and fullmatch(r'-?\d+', mes) and fullmatch(r'-?\d+', ano):
            dia = int(dia)
            mes = int(mes)
            ano = int(ano)
        else:
            dia = 0
            mes = 0
            ano = 0
    else:
        dia, mes, ano = 0, 0, 0
    return dia, mes, ano
