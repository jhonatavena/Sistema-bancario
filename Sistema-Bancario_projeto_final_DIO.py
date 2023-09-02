import os
import getpass

limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUE = 2

cliente = {
    "Nome Completo": "",
    "CPF": "",
    "Estado": "",
    "Cidade": "",
    "Senha": "",
    "Saldo": 0
}

def criar_conta():
    cliente["Nome Completo"] = input("Digite seu nome completo: ")
    cliente["CPF"] = input("Digite seu CPF: ")
    cliente["Estado"] = input("Digite seu estado: ")
    cliente["Cidade"] = input("Digite sua cidade: ")
    cliente["Senha"] = input("Digite sua senha: ")

while True:
    inicial = input('\nBem vindo ao VenaBank!\n\n[1]Criar conta [2]Fazer Login\nDigite a opção desejada: ')

    if inicial == '1':
        criar_conta()
        os.system('cls')
        print('\n\nParabéns, conta criada na Venabank com sucesso!\n\n')
    
    elif inicial == '2':
        while True:
            acesso = input('LOGIN\nDigite seu usuário\nCPF: ')
            if acesso == cliente['CPF']:
                break
            else:
                print('Login não identificado')
            
        acesso_senha = getpass.getpass('Digite sua senha: ')
        if acesso_senha == cliente['Senha']:
            print(f'Bem vindo {cliente["Nome Completo"]}')
            os.system('cls')
        else:
            print('Senha incorreta')
            continue
        
        while True:
            menu = input('Digite a opção desejada:\n[D]epósito [S]aque [E]xtrato [Q]uit: ')
            
            if menu == 'D' or menu == 'd':
                os.system('cls')
                try:
                    deposito = int(input('DEPÓSITO\nDigite o valor que deseja depositar: '))
                    if deposito >= 0:
                        cliente["Saldo"] += deposito
                        extrato.append(f'Depósito realizado de +R${deposito}')
                        print('Operação realizada com sucesso!\n')
                    else:
                        print('Operação Inválida!\nTente novamente, por gentileza!\n')
                except ValueError:
                    print('Valor de depósito inválido. Digite um valor numérico válido.\n')
            
            elif menu == 'S' or menu == 's':
                os.system('cls')
                try:
                    saque = int(input('SAQUE\nDigite o valor que deseja sacar: '))
                    if saque <= limite and saque >= 0:
                        if saque <= cliente["Saldo"] and numero_saques < LIMITE_SAQUE:
                            cliente["Saldo"] -= saque
                            extrato.append(f'Saque realizado de -R${saque}')
                            numero_saques += 1
                            print('Operação realizada com sucesso!\n')
                        elif saque > cliente["Saldo"]:
                            print('Saldo na conta insuficiente!\n')
                        elif numero_saques >= LIMITE_SAQUE:
                            print('Você atingiu o limite de saques diários!\n')
                    else:
                        print('Operação Inválida!\nLimite de R$500 por dia atingido\nTente novamente por gentileza!\n')
                except ValueError:
                    print('Valor de saque inválido. Digite um valor numérico válido.\n')

            elif menu == 'E' or menu == 'e':
                os.system('cls')
                if len(extrato) >= 1:
                    print(f'Extrato\n\n{cliente["Nome Completo"]}\nSALDO ATUAL: R${cliente["Saldo"]}\n\nHISTÓRICO DE TRANSAÇÕES:')
                    for transacoes in extrato:
                        print(transacoes)
                else:
                    print(f'Seu saldo atual é R${cliente["Saldo"]}\n\nNão houve transações.\n')

            elif menu == 'Q' or menu == 'q':
                break
            
            else:
                print('Operação inválida!\nSelecione novamente a opção desejada.\n')
    
    else:
        os.system('cls')
        print('Por favor, tente novamente e digite um comando válido.')
