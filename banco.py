import os

def limpar_terminal():
    os.system('cls')

MAXIMO_SAQUE = 500.00
LIMITE_SAQUES = 3
saldo = 0.00
extrato = ""
saques_realizados = 0

while True:
    limpar_terminal()
    opcao = input("""
    ****** SISTEMA BANCÁRIO ******
    
    (D) Deposito
    (S) Saques
    (E) Extrato    
    (Q) Sair    
                  
    Digite uma das opções acima:""")

    if opcao.upper() == "D": #FUNÇÕES DO DEPOSITO
        limpar_terminal()
        print("****** Depósitos ******")
        deposito = 0
        while True:
            deposito = float(input("Digite o valor do seu deposito:"))
            if deposito <= 0:
                continue
            else:
                continuar = input(f"Confirmar o deposito de: R${deposito:.2f} (Y/N)")
                if continuar.upper() == "Y":
                    break
                else:
                    continue
        limpar_terminal()
        #atualização do saldo em conta
        saldo += deposito            
        
        #informativo para o usuário
        print(f"deposito de R${deposito:.2f} realizado com sucesso!")
        print(f"Seu saldo atual é de R${saldo:.2f}")

        #atualização do extrato
        extrato += f"\n - deposito de R${deposito:.2f} "
        extrato += f"\n - saldo de R${saldo:.2f} "

        #volta para o inicio
        seguir = input("\n \n Digite qualquer coisa para continuar:")
        continue

    elif opcao.upper() == "S": #funções do saque
        limpar_terminal()
        print("****** Saques ******")
        if saques_realizados >= LIMITE_SAQUES:
            print(f"Você não tem saques para hoje.")
        else:
            print(f"Você tem {LIMITE_SAQUES-saques_realizados} restantes hoje.")
            saque = float(input(f"Digite o valor do saque (até R${MAXIMO_SAQUE:.2f}):"))
            if saque > MAXIMO_SAQUE or saque > saldo:
                print("Seu saque é maior doque o permitido!")
            else:
                saldo -= saque
                print(f"Saque de R${saque:.2f} realizado com sucesso")
                print(f"Saldo atual de R${saldo:.2f}")
                #atualização do extrato
                extrato += f"\n - saque de R${saque:.2f} "
                extrato += f"\n - saldo de R${saldo:.2f} "
                saques_realizados += 1
        #volta para o inicio
        seguir = input("\n \n Digite qualquer coisa para continuar:")
        continue
    elif opcao.upper() == "E":
        limpar_terminal()
        print("****** Extratos ******")
        print(extrato)
        #volta para o inicio
        seguir = input("\n \n Digite qualquer coisa para continuar:")
        continue
    elif opcao.upper() == "Q":
        limpar_terminal()
        print("****** Saindo ******")
        break
    else:
        continue