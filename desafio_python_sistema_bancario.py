menu = '''
============ MENU ===========
1 - Sacar
2 - Depositar
3 - Extrato
0 - Sair
=============================

'''

saldo = 500
LIMITE_SAQUES = 3
extrato = ""
numeros_saques = 0

while True:

    sistema = int(input(menu))

    if sistema == 1:
        saque = float(input("Qual o valor do saque? "))
        
        if saque > 500:
            print("Seu limite de saque é de 500 reais.")

        elif saque > saldo:
            print("Você não tem saldo suficiente.")

        elif numeros_saques >= LIMITE_SAQUES:
            print("Número de saques excedido.")

        elif saque <= 500 and saque <= saldo and numeros_saques < LIMITE_SAQUES and saque > 0:
            saldo -= saque
            extrato += f"Saque: R$ {saque:.2f}\n"
            numeros_saques += 1

        else:
            print("Operação falhou! Valor inválido.")    
    elif sistema == 2:
        deposito = float(input("Quanto você irá depositar? "))
        if deposito > 0:
            extrato += f"Depósito: R$ {deposito:.2f}\n"
            saldo += deposito

        else:
            print("Operação falhou! Valor inválido.")
    elif sistema == 3:
        if extrato == "":
            print("Não foram realizadas movimentações.")

        else:    
            print(
    f'''
============ Extrato ===========

{extrato}
================================
Saldo: R$: {saldo:.2f}

Obrigado!
    '''
    )
            
    elif sistema == 03:
            break

    else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")