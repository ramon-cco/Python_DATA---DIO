def exibir_menu():
    menu = """
    [d] Depositar | [s] Sacar | [e] Extrato
    [q] Sair
    => """
    return input(menu)


def depositar(saldo, extrato):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Seu saldo atual é R$ {saldo:.2f}")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato


def sacar(saldo, extrato, numero_saques, LIMITE_SAQUES, limite):
    valor = float(input("Informe o valor do saque: "))
    if valor > 0:
        if valor > saldo:
            print(f"Operação falhou! Você não tem saldo suficiente.\nSeu saldo atual é R$ {saldo:.2f}")
        elif valor > limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! Número máximo de saques excedido para o limite diário.")
        else:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato, numero_saques


def mostrar_extrato(extrato, saldo):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print("\n================ SALDO =================")
    print(f"Saldo: R$ {saldo:.2f}")
    print("==========================================")

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = exibir_menu()

        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)
        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques, LIMITE_SAQUES, limite)
        elif opcao == "e":
            mostrar_extrato(extrato, saldo)
        elif opcao == "q":
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == "__main__":
    main()
