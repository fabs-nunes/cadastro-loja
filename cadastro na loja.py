clientes = []

def cadastrar(lista):
    login = str(input('digite seu login: '))
    for i in clientes:
        if login.strip == i:
            print('login invalido')
    usuario = { 'login' : login,
                'nome' : input('digite seu nome completo'),
                'senha' : input('digite sua senha'),
                'email' : input('digite seu email'),
                'nascimento' : input('digite sua data de nascimento'),
                'celular' : input('digite seu numero de celular'),
                'rua' : input('digite sua rua'),
                'casa' : input('digite o numero de sua casa'),
                'bairro' : input('digite seu bairro'),
                'cidade' : input('digite sua cidade') 
    }
    lista.append(usuario)

def buscar(lista):
    entrada = str(input('digite seu login'))
    for i in range(len(lista)):
        if lista[i]['login'] == entrada:
            chave = str(input('digite sua senha'))
            if chave == lista[1]['senha']:
                print(f"login: {lista[i]['login']}")
                print(f"nome: {lista[i]['nome']}")
    print('busca encerrada, se nenhum usuario foi exibido é porque esse usuario naão foi cadastrado')

def mostrar(lista):
    for i in range(len(lista)):
        print(f"login: {lista[i]['login']}")
        print(f"nome: {lista[i]['nome']}")

def relatorio(lista):
    arq = open("relatorio.txt", "w")
    loja = str(input('digite o nome da loja: '))
    nclientes = len(lista)
    dia = int(input('digite o dia de hoje: '))
    mes = str(input('digite o mes de hoje: '))
    ano = int(input('digite o ano atual: '))
    arq.write(f"relatorio de clientes \n a loja{loja} possui {nclientes} clientes listados abaixo: \n")
    for i in range(len(lista)):
        arq.write(f"{lista[i]['nome']}\n")
    arq.write(f"russas {dia} de {mes} de {ano}")

while True:
    opcao = int(input('''
    Menu
    escolha uma das opções abaixo:
    [1]cadastrar cliente
    [2]buscar cliente
    [3]mostrar clientes
    [4]gerar relatorio
    [0]sair   
    '''))
    if opcao == 1:
        cadastrar(clientes)
    elif opcao == 2:
        buscar(clientes)
    elif opcao == 3:
        mostrar(clientes)
    elif opcao == 4:
        relatorio(clientes)
    if opcao == 0:
        break
    else:
        print("opção invalida")