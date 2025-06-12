from datetime import datetime

class Conta:
    def __init__(self, agencia, numero, saldo=0):
        self.agencia = agencia
        self.numero = numero
        self.saldo = saldo
        self.extrato = []
        self.saques_restantes = 3

    def sacar(self, valor):
        if valor > self.saldo:
            print("Erro! Operação não realizada, saldo insuficiente!")
        elif valor <= 0 or valor > 500:
            print("Erro! Valor inválido! Saques devem ser entre R$0.01 e R$500.")
        elif self.saques_restantes == 0:
            print("Erro! Limite de saques diários atingido.")
        else:
            self.saldo -= valor
            self.saques_restantes -= 1
            self.extrato.append(f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] Saque: -R${valor:.2f}")
            print(f"Saque de R${valor:.2f} realizado com sucesso.")

    def depositar(self, valor):
        if valor <= 0:
            print("Erro! Valor inválido para depósito.")
        else:
            self.saldo += valor
            self.extrato.append(f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] Depósito: +R${valor:.2f}")
            print(f"O Depósito de R${valor:.2f} realizado com sucesso.")

    def mostrar_extrato(self):
        print("\n=== Extrato ===")
        if not self.extrato:
            print("Nenhuma movimentação registrada.")
        else:
            for item in self.extrato:
                print(item)
        print(f"\nSaldo atual: R${self.saldo:.2f}")
        print(f"Saques restantes hoje: {self.saques_restantes}")
        print("====================\n")


class Cliente:
    def __init__(self, nome, cpf, agencia, numero_conta):
        self.nome = nome
        self.cpf = cpf
        self.conta = Conta(agencia, numero_conta)


class Banco:
    def __init__(self):
        self.clientes = {}

    def cadastrar_cliente(self, nome, cpf, agencia, numero_conta):
        if cpf in self.clientes:
            print("Erro! Cliente já cadastrado!")
        else:
            self.clientes[cpf] = Cliente(nome, cpf, agencia, numero_conta)
            print(f"O Cliente {nome} cadastrado com sucesso.")

    def buscar_cliente(self, cpf):
        return self.clientes.get(cpf)

    def realizar_saque(self, cpf, valor):
        cliente = self.buscar_cliente(cpf)
        if cliente:
            cliente.conta.sacar(valor)
        else:
            print("Erro! Cliente não encontrado.")

    def realizar_deposito(self, cpf, valor):
        cliente = self.buscar_cliente(cpf)
        if cliente:
            cliente.conta.depositar(valor)
        else:
            print("Erro! Cliente não encontrado.")

    def mostrar_extrato(self, cpf):
        cliente = self.buscar_cliente(cpf)
        if cliente:
            print(f"\nExtrato do cliente {cliente.nome} (CPF: {cpf})")
            cliente.conta.mostrar_extrato()
        else:
            print("Erro! Cliente não encontrado.")

    def listar_clientes(self):
        if not self.clientes:
            print("Nenhum cliente está cadastrado!")

        else:
            print("\n=====LISTA DE CLIENTES =====")
            for cpf, cliente in self.clientes.items():
                print(f"NOME: {cliente.nome}")
                print(f"CPF: {cliente.cpf}")
                print(f"AGÊNCIA: {cliente.conta.agencia}")
                print(f"CONTA: {cliente.conta.numero}")
                print("\n=========================")   


banco = Banco()

while True:
    menu = """
====== MENU BANCÁRIO ======
[1] SACAR
[2] DEPOSITAR
[3] EXTRATO
[4] CADASTRAR CLIENTE
[5] LISTAR CLIENTES
[0] SAIR
Escolha uma opção: """
    opcao = input(menu)

    if opcao == "1":
        cpf = input("Informe o CPF do cliente: ")
        try:
            valor = float(input("Informe o valor para saque: R$"))
            banco.realizar_saque(cpf, valor)
        except ValueError:
            print("Erro! Valor inválido.")

    elif opcao == "2":
        cpf = input("Informe o CPF do cliente: ")
        try:
            valor = float(input("Informe o valor para depósito: R$"))
            banco.realizar_deposito(cpf, valor)
        except ValueError:
            print("Erro! Valor inválido.")

    elif opcao == "3":
        cpf = input("Informe o CPF do cliente: ")
        banco.mostrar_extrato(cpf)

    elif opcao == "4":
        nome = input("Nome do cliente: ")
        cpf = input("CPF (somente números): ")
        agencia = input("Agência: ")
        numero_conta = input("Número da conta: ")
        banco.cadastrar_cliente(nome, cpf, agencia, numero_conta)

    elif opcao == "5":
        banco.listar_clientes()    

    elif opcao == "0":
        print("Encerrando o sistema. Obrigado por utilizar nosso banco!")
        break

    else:
        print("Erro! Opção inválida! Tente novamente.")
