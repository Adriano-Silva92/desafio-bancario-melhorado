import textwrap

def menu():
    menu = """\n
    ================ MENU ================
    [1]\tDEPOSITAR
    [2]\tSACAR
    [3]\tEXTRATO
    [4]\tNOVA CONTA
    [5]\tLISTAR CONTAS
    [6]\tNOVO USUÁRIO
    [0]\tSAIR
    => """
    return input(textwrap.dedent(menu))


def localizar_conta(contas, cpf, numero_conta):
    for conta in contas:
        if conta["usuario"]["cpf"] == cpf and conta["numero_conta"] == numero_conta:
            return conta
    return None


def depositar(conta):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        conta["saldo"] += valor
        conta["extrato"] += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Valor inválido para depósito. @@@")


def sacar(conta, limite, limite_saques):
    valor = float(input("Informe o valor do saque: "))
    if valor <= 0:
        print("\n@@@ Valor inválido para saque. @@@")
        return

    if valor > conta["saldo"]:
        print("\n@@@ Saldo insuficiente. @@@")
    elif valor > limite:
        print("\n@@@ O valor do saque excede o limite por operação. @@@")
    elif conta["numero_saques"] >= limite_saques:
        print("\n@@@ Número máximo de saques diários atingido. @@@")
    else:
        conta["saldo"] -= valor
        conta["extrato"] += f"Saque:\t\tR$ {valor:.2f}\n"
        conta["numero_saques"] += 1
        print("\n=== Saque realizado com sucesso! ===")


def exibir_extrato(conta):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not conta["extrato"] else conta["extrato"])
    print(f"\nSaldo:\t\tR$ {conta['saldo']:.2f}")
    print("==========================================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    if filtrar_usuario(cpf, usuarios):
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    return next((u for u in usuarios if u["cpf"] == cpf), None)


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        conta = {
            "agencia": agencia,
            "numero_conta": numero_conta,
            "usuario": usuario,
            "saldo": 0,
            "extrato": "",
            "numero_saques": 0
        }
        print("\n=== Conta criada com sucesso! ===")
        return conta

    print("\n@@@ Usuário não encontrado. @@@")
    return None


def listar_contas(contas):
    for conta in contas:
        linha = f"""\n
        Agência:\t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def selecionar_conta(contas):
    cpf = input("Informe o CPF do titular: ")
    try:
        numero_conta = int(input("Informe o número da conta: "))
    except ValueError:
        print("@@@ Número da conta inválido. @@@")
        return None

    conta = localizar_conta(contas, cpf, numero_conta)
    if not conta:
        print("@@@ Conta não encontrada. @@@")
    return conta


def main():
    LIMITE_SAQUES = 3
    LIMITE_POR_SAQUE = 500
    AGENCIA = "0001"

    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            conta = selecionar_conta(contas)
            if conta:
                depositar(conta)

        elif opcao == "2":
            conta = selecionar_conta(contas)
            if conta:
                sacar(conta, LIMITE_POR_SAQUE, LIMITE_SAQUES)

        elif opcao == "3":
            conta = selecionar_conta(contas)
            if conta:
                exibir_extrato(conta)

        elif opcao == "6":
            criar_usuario(usuarios)

        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "5":
            listar_contas(contas)

        elif opcao == "0":
            print("\n>>> Obrigado por usar nosso sistema bancário! <<<")
            break

        else:
            print("\n@@@ Operação inválida. Tente novamente. @@@")

main()
