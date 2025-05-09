
from datetime import datetime, date, time, timedelta
import re

menu = """
Bem Vindo ao Banco Suzy

Selecione a operação desejada:

[d] Depositar
[s] Sacar
[e] Extrato
[a] Abrir Conta
[q] Sair

"""
saldo = 0
limite = 500
extrato = []
numero_saque = 0
LIMITE_SAQUES = 3
numero_operacao_dia = 0
mascara_ptbr = "%d/%m/%Y %H:%M:%S"
cadastro = {}
agencia = "0001"
conta_corrente = 0


def saque(saldo, valor_saque, extrato, limite, numero_saque, LIMITE_SAQUES, numero_operacao_dia, mascara):
    if valor_saque <= saldo and valor_saque <= limite and numero_saque < LIMITE_SAQUES and numero_operacao_dia <= 10:

        numero_operacao_dia += 1
        numero_saque += 1
        saldo -= valor_saque
        data_operacao = datetime.now()
        extrato.append(f"(-)R${valor_saque:.2f}    -    {data_operacao.strftime(mascara)}  - Saque")
        
        print(f"Saque efetuado com sucesso \n   Valor sacado: R${valor_saque:.2f} \n\nSaldo Atual: R${saldo:.2f}")
            
    elif numero_saque >= LIMITE_SAQUES:
        print("Você chegou ao limíte de operações de saque diário, tente novamente em outro dia")
    elif valor_saque > limite:
        print(f"Não foi possível efetuar a transação, o seu limite de saque é de R${limite:.2f} por saque")
    elif valor_saque > saldo:
        print("Saldo insuficiente. Faça um deposito em sua conta para poder sacar!")
    elif numero_operacao_dia > 10:
        print("Você chegou ao limíte de operações diário em sua conta, tente novamente em outro dia")
    else:
        print("Tente novamente")

    return saldo, extrato, numero_saque, numero_operacao_dia


def deposito(saldo, valor_deposito, extrato, numero_operacao_dia, mascara):

    if valor_deposito > 0 and numero_operacao_dia <= 10:

        numero_operacao_dia += 1
        saldo += valor_deposito
        data_operacao = datetime.now()
        extrato.append(f"(+)R${valor_deposito:.2f}    -    {data_operacao.strftime(mascara)}  - Depósito")
            
        print(f"Deposito efetuado com sucesso \n   Valor depositado: R${valor_deposito:.2f} \n\nSaldo Atual: R${saldo:.2f}")

    elif numero_operacao_dia > 10:
        print("Você chegou ao limíte de operações diário em sua conta, tente novamente em outro dia")
            
    else:
        print("Operação inválida. Valor depositado deve ser maior do que 0")

    return saldo, extrato, numero_operacao_dia



def mostrar_extrato(saldo,/,extrato):
    print("""
###########EXTRATO#############
              
    """)
    for item in extrato:

        print(item)

    print(f"\nSaldo Atual: R${saldo:.2f}")

    print("""
###############################
                """)


def abrir_conta(cpf, agencia, cadastro, conta_corrente, saldo):
    if agencia not in cadastro:
        cadastro[agencia] = {}

    conta_corrente += 1
    cadastro[agencia][conta_corrente] = {
        "cpf": cpf,
        "nome": input("Digite o seu nome: "),
        "data_nascimento": input("Digite a sua data de nascimento: "),
        "endereco": {
            "logradouro": input("Digite o logradouro (rua, avenida, etc.): "),
            "numero_local": input("Digite o número do local: "),
            "cidade": input("Digite a cidade: "),
            "estado": input("Digite a sigla do estado: ")
        },
        "saldo": saldo
    }

    print(f"\nBem Vindo {cadastro[agencia][conta_corrente]['nome']}! Conta criada com sucesso!\nAgência: {agencia}\nConta: {conta_corrente}")
    return cadastro, conta_corrente

    
    



def limpar_cpf(cpf):
    cpf = re.sub(r'\D','',cpf)
    cpf = cpf.strip()

    return cpf






while True:

    opcao = input(menu)

    if opcao == "d":

        valor_deposito = float(input("Digite o valor a ser depositado: "))
 
        saldo, extrato, numero_operacao_dia = deposito(saldo, valor_deposito, extrato, numero_operacao_dia, mascara_ptbr)


    if opcao == "s":
        
        valor_saque = float(input("Digite o valor do saque: "))
        saldo, extrato, numero_saque, numero_operacao_dia = saque(
            saldo=saldo,
            valor_saque=valor_saque, 
            extrato = extrato, 
            limite=limite, 
            numero_saque = numero_saque, 
            LIMITE_SAQUES=LIMITE_SAQUES, 
            numero_operacao_dia=numero_operacao_dia,
            mascara=mascara_ptbr
            )


    if opcao == "e":

        if numero_operacao_dia <= 10:
            numero_operacao_dia += 1
            mostrar_extrato(saldo,extrato=extrato)
        else:
            print("Você chegou ao limíte de operações diário em sua conta, tente novamente em outro dia")

    if opcao == "a":

        cpf=input("Digite o seu CPF: ")
        cpf = limpar_cpf(cpf)
        
        while len(cpf) != 11:
            cpf = input("CPF inválido. Certifique-se de digitar 11 números ou digite 0 para sair: ")

            if cpf == '0':
                break

            cpf = limpar_cpf(cpf)
        
        if len(cpf) == 11:
            cadastro, conta_corrente = abrir_conta(cpf, agencia, cadastro, conta_corrente, saldo) 


    if opcao == "q":
        break