def menu():
    print("1: Inserir uma pessoa")
    print("2: Buscar por primeiro nome")
    print("3: Buscar por mes de nascimento")
    print("4: Buscar por dia e mes de nascimento")
    print("5: Imprimir agenda")
    print("0: Sair")
    
    escolha = int(input("Opcao: "))
    return escolha


def inserir_pessoa(lista):
    pessoa = {"nome": None, "email": None, "endereco": None, "telefone": None, 
              "aniversario": None, "observacao": None}
    endereco = {"rua": None, "numero": None, "complemento": None, "bairro": None, "cep": None, 
                "cidade": None, "estado": None, "pais": None}
    telefone = {"ddd": None, "numero": None}
    aniversario = {"dia": None, "mes": None, "ano": None}

    pessoa["Nome"] = input("Nome: ")
    pessoa["E-mail"] = input("E-mail: ")
    endereco["Rua"] = input("Rua: ")
    endereco["Numero"] = input("Numero: ")
    endereco["Complemento"] = input("Complemento: ")
    endereco["Bairro"] = input("Bairro: ")
    endereco["Cep"] = input("Cep: ")
    endereco["Cidade"] = input("Cidade: ")
    endereco["Estado"] = input("Estado: ")
    endereco["Pais"] = input("Pais: ")
    telefone["DDD"] = int(input("DDD: "))
    telefone["Numero"] = input("Numero: ")
    aniversario["Dia"] = int(input("Dia do nascimento: "))
    aniversario["Mes"] = int(input("Mes do nascimento: "))
    aniversario["Ano"] = int(input("Ano do nascimento: "))
    pessoa["Observacao"] = input("Observacao: ")

    pessoa["Endereco"] = endereco
    pessoa["Telefone"] = telefone
    pessoa["Aniversario"] = aniversario

    lista.append(pessoa)
    return lista


def verificar_nome(nome, lista):
    for pessoa in lista:
        if nome.lower() in pessoa["Nome"].lower():
            return pessoa
    return


def verificar_aniversario(mes, lista):
    for pessoa in lista:
        if mes == pessoa["Aniversario"]["Mes"]:
            return pessoa
    return


def verificar_aniversario_mes_dia(dia, mes, lista):
    for pessoa in lista:
        if dia == pessoa["Aniversario"]["Dia"] and mes == pessoa["Aniversario"]["Mes"]:
            return pessoa
    return


def menu_agenda():
    print("1: Imprimir nome, telefone e E-mail")
    print("2: Imprimir todos os dados")

    escolha = int(input())
    return escolha


lista = [] 

iniciar = menu()
while iniciar != 0:
    if iniciar > 5 or iniciar < 0:
        print("Opcao invalida")
    elif iniciar == 1:
        lista = inserir_pessoa(lista)
    elif iniciar == 2:
        nome = input("Primeiro nome: ")
        resultado = verificar_nome(nome, lista)
        if resultado: 
            print(resultado)
    elif iniciar == 3:
        mes = int(input("Mes de aniversario: "))
        resultado = verificar_aniversario(mes, lista)
        if resultado: 
            print(resultado)
    elif iniciar == 4:
        dia = int(input("Dia do aniversario: "))
        mes = int(input("Mes do aniversario: "))
        resultado = verificar_aniversario_mes_dia(dia, mes, lista)
        if resultado: 
            print(resultado)
    elif iniciar == 5:
        escolha = menu_agenda()
        if escolha == 1:
            for pessoa in lista:
                nome = pessoa["Nome"]
                telefone = pessoa["Telefone"]["Numero"]
                email = pessoa["E-mail"]
                print(f"Nome: {nome}, Telefone: {telefone}, E-mail: {email}")
        elif escolha == 2:
            for pessoa in lista:
                print(pessoa)

    iniciar = menu()
