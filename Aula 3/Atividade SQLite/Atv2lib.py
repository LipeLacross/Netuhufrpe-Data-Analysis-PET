import random
from SQLite import Database

class Conta():
    def __init__(self, numConta, saldo = 0):
        self.numero = numConta
        self.saldo = saldo

    def deposite(self, valor):
        self.saldo = self.saldo + valor - (valor * 0.001)

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo = self.saldo - valor
            return True
        else:
            return False

class Banco():
    def __init__(self, nome):
        self.nome = nome
        self.contas = []
        self.dados = Database()
        self.dados.createTable()
    
    def carregarContasDoBanco(self):
        clientes = self.dados.loadAccounts()
        if clientes != None:
            for customers in clientes:
                self.contas.append(Conta(customers['NUMCONTA'], customers['SALDO']))
            return True
        return False

    def resetarBanco(self):
        self.dados.excludeTables()
        return True
    
    def completarServiço(self):
        self.dados.putAccounts(self.contas)
        return True
    
    def finalizarServiço(self):
        self.dados.endConnection()
        return True
    
    def getNome(self):
        return self.nome

    def getContas(self):
        return self.dados.loadAccounts()
    
    def criarConta(self):
        num = random.randint(1, 1000)
        verificar = self.buscarConta(num)
        while verificar == True:
            num = random.randint(1, 1000)
            verificar = self.buscarConta(num)
        if verificar == False:
            c = Conta(num)
            self.contas.append(c)
            return num

    def consultaSaldo(self, numConta):
        for i in self.contas:
            if i.numero == numConta:
                return i.saldo
        return -1

    def depositar(self, numConta, valor):
        for i in self.contas:
            if i.numero == numConta:
                return i.deposite(valor)
        return False
    
    def saque(self, numConta, valor):
        for i in self.contas:
            if i.numero == numConta:
                return i.sacar(valor)
        return False

    def buscarConta(self, numConta):
        for i in self.contas:
            if i.numero == numConta:
                return True
        return False
    
    def excluirConta(self, numConta):
        for i in self.contas:
            if i.numero == numConta:
                i = None
                return True
        return False
