from Atv2lib import Banco


def imprimirMenu():
    print("Menu")
    print("0 - Sair")
    print("1 - Criar uma Nova Conta")
    print("2 - Consultar Saldo Conta")
    print("3 - Depositar na Conta")
    print("4 - Sacar na Conta")
    print("5 - Excluir Conta")
    choice = int(input("digite a opção desejada:"))
    return choice

print("Bem-vindo")

bancoLacross = Banco("Lacross")
#bancoLacross.resetarBanco()
entradaDeDados = bancoLacross.carregarContasDoBanco()
#print(bancoLacross.getContas())
if entradaDeDados:
    print("Dados carregados.")
else:
    print("Não foi possível sobrescrever os dados atuais.")
escolha = imprimirMenu()

while escolha > 0 or escolha < 0:

    if escolha == 1:
        # criar uma conta
        print("Criando Conta...")
        numConta = bancoLacross.criarConta()
        print("Conta criada:", numConta,".")

    elif escolha == 2:
        # consultar saldo
        print("Consultando Saldo...")
        numConta = int(input("digite o numero da conta:"))
        saldo = bancoLacross.consultaSaldo(numConta)
        if saldo == -1:
            print("Conta não encontrada.")
        else:
            print("o saldo da conta", numConta, "é", saldo, "R$.")
    elif escolha == 3:
        # depositar para uma conta
        print("Depositando Conta...")
        numConta = int(input("digite o numero da conta:"))
        valor = int(input("digite o valor que deseja depositar:"))
        saldo = bancoLacross.depositar(numConta, valor)
        if saldo == False:
            print("Conta não encontrada.")
        else:
            print("Valor Depositado.")
    elif escolha == 4:
        # sacar de uma conta
        print("Sacando da Conta...")
        numConta = int(input("digite o numero da conta:"))
        valor = int(input("digite o valor que deseja sacar:"))
        resp = bancoLacross.sacar(numConta, valor)
        if resp:  # significa resp == True
            print("Valor Sacado")
        else:
            print("Saldo Insuficiente")
    elif escolha == 5:
        # Excluir conta
        print("Iniciando exclusão...")
        numConta = int(input("digite o numero da conta:"))
        resp = bancoLacross.excluirConta(numConta)
        if resp:
            print("A conta foi excluída com sucesso.")
        else:
            print("A conta não existe.")       
    else:
        print("Escolha inválida")
    
    enviarDados = bancoLacross.completarServiço()
    if enviarDados:
        print("Banco funcionou.")
    else:
        print("O trânsito de dados falhou.")
    escolha = imprimirMenu()

fecharBanco = bancoLacross.finalizarServiço()
if fecharBanco:
    print("Serviço finalizado.")
else:
    print("Error.")