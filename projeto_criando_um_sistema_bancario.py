menu = """

[q] Sair
[d] Depositar
[s] Sacar
[e] Extrato

 = """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

#função while para repetir as operações até que seja selecionada a opção que quebre o loop.
while True:
    
    opcao = input(menu)
    if opcao == "d":
        valor = float(input("Informe o valor do depósito:"))    
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"

        else:
            print("Falha na operação: Valor inválido")

        
    elif opcao == "s":
    
        valor = float(input("Insira o valor do saque: "))
        
        excedeu_valor_saldo = valor > saldo

        excedeu_valor_limite = valor > limite

        excedeu_saque = numero_saques >= limite_saques

        if excedeu_valor_saldo:
            print("Operação invalida: Saldo insuficiente.")

        elif excedeu_valor_limite:
            print("Operação invalida: Valor excedeu o limite ")

        elif excedeu_saque:
            print("Operação invalida: Limite de saques excedidos")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
             print("Operação invalida: Valor inválido")

    elif opcao == "e":
        print("\n=============== EXTRATO ===============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=========================================")


    elif opcao == "q":
        break

    else:
        print("Operação invalida, por favor selecione novamente a operação desejada")

