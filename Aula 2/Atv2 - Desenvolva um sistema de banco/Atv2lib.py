import random

class Conta():
    def __init__(self, numConta):
        self.numero = numConta
        self.saldo = 0

    def deposite(self, valor):
        self.saldo = self.saldo + valor - (valor * 0.001)

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo = self.saldo - valor
            return True
        else:
            return False

class Poupanca(Conta):

    def render(self):
        self.saldo = self.saldo + self.saldo * 0.01

class Bonificada(Conta):

    def __init__(self, numConta):
        super().__init__(numConta)
        self.bonus = 0
    
    def renderBonus(self):
        self.saldo += self.bonus
        self.bonus = 0
    
    def deposite(self, valor):
        self.bonus += valor * 0.001
        super().deposite(valor)
    

class Banco():
    def __init__(self, nome):
        self.nome = nome
        self.contas = []

    def getNome(self):
        return self.nome

    def criarConta(self):
        num = random.randint(1, 1000)
        verificar = self.buscarConta(num)
        while verificar == False:
            c = Conta(num)
            self.contas.append(c)
            return num

    def criarPoupanca(self):
        num = random.randint(1001, 2000)
        verificar = self.buscarConta(num)
        while verificar == False:
            p = Poupanca(num)
            self.contas.append(p)
            return num
    
    def criarBonificada(self):
        num = random.randint(2001, 3000)
        verificar = self.buscarConta(num)
        while verificar == False:
            b = Bonificada(num)
            self.contas.append(b)
            return num

    def consultaSaldo(self, numConta):
        for i in self.contas:
            if i.numero == numConta:
                return i.saldo
        return False

    def depositar(self, numConta, valor):
        for i in self.contas:
            if i.numero == numConta:
                return i.deposite(valor)
        return False
    def sacar(self, numConta, valor):
        for i in self.contas:
            if i.numero == numConta:
                return i.sacar(valor)
        return False
    def renderPoupanca(self, numConta):
        for i in self.contas:
            if i.numero == numConta and isinstance(i, Poupanca):
                i.render()
                return True
        return False
    
    def renderBonus(self, numConta):
        for i in self.contas:
            if i.numero == numConta and isinstance(i, Bonificada):
                i.renderBonus()
                return True
        return False

    def buscarConta(self, numConta):
        for i in self.contas:
            if i.numero == numConta:
                return True
        else:
            return False