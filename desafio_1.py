menu = """
Bem Vindo ao Banco Suzy

Selecione a operação desejada:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = []
numero_saque = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":

        valor_deposito = float(input("Digite o valor a ser depositado: "))
        
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato.append(f"+R${valor_deposito:.2f}    Depósito")
            
            print(f"Deposito efetuado com sucesso \n   Valor depositado: R${valor_deposito:.2f} \n\nSaldo Atual: R${saldo:.2f}")
            
        else:
            print("Operação inválida. Valor depositado deve ser maior do que 0")

    if opcao == "s":
        
        valor_saque = float(input("Digite o valor do saque: "))

        if valor_saque <= saldo and valor_saque <= limite and numero_saque < LIMITE_SAQUES:
            numero_saque += 1
            saldo -= valor_saque
            extrato.append(f"-R${valor_saque:.2f}    Saque")
            print(f"Saque efetuado com sucesso \n   Valor sacado: R${valor_saque:.2f} \n\nSaldo Atual: R${saldo:.2f}")
        elif numero_saque >= LIMITE_SAQUES:
            print("Você chegou ao limíte de operações de saque diário, tente novamente em outro dia")
        elif valor_saque > limite:
            print(f"Não foi possível efetuar a transação, o seu limite de saque é de R${limite:.2f} por saque")
        elif valor_saque > saldo:
            print("Saldo insuficiente. Vai trabalhar e pare de ficar gastando, seu pobre!!!!")
        else:
            print("Tente novamente")


    if opcao == "e":
        for item in extrato:
            print(item)

        print(f"\nSaldo Atual: R${saldo:.2f}")



    if opcao == "q":
        break




