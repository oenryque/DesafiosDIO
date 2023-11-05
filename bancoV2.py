

import os
from colorama import init, Fore, Style, Back
cor_fundo = Back.YELLOW  # Cor de fundo azul
cor_texto = Fore.WHITE  # Cor do texto branco
BANCO = "Santander"
MAXIMO_SAQUE = 500.00
LIMITE_SAQUES = 3
saldo = 0
extrato = []
saques_realizados = 0

init(autoreset=True)  # Inicializa o colorama
def iniciar_interface(nome, descricao):
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela do prompt

    # Define cores e estilo
    cor_fundo = Back.WHITE
    cor_texto = Fore.BLACK
    cor_amarela = Fore.YELLOW  # Adicionando a cor amarela
    largura_total = 60  # Largura total da interface
    descricao = ">>>> "+ descricao + " <<<<"
    # Adiciona o nome do banco antes do nome da interface
    nome_completo = f"{BANCO} / {nome}"

    # Calcula o espaçamento à esquerda e à direita do texto para centralizá-lo
    espaco_esquerda = (largura_total - len(nome_completo)) // 2
    espaco_direita = largura_total - len(nome_completo) - espaco_esquerda

    # Calcula o espaçamento para centralizar a descrição
    espaco_descricao = (largura_total - len(descricao)) // 2

    print(cor_fundo + f'{"#" * largura_total}' + Style.RESET_ALL)
    print(cor_fundo + ' ' * espaco_esquerda + nome_completo.upper() + ' ' * espaco_direita + Style.RESET_ALL)
    print(cor_fundo + f'{"#" * largura_total}' + Style.RESET_ALL)
    print(cor_amarela + ' ' * espaco_descricao + descricao + ' ' * espaco_descricao + Style.RESET_ALL)  # Usando a cor amarela para a descrição
    print("\n")
def interface_de_confirmacao():
    global cor_fundo 
    global cor_texto
    largura_total = 60  # Largura total da interface
    while True:
        resposta = input(cor_fundo + f'digite "S" para AVANÇAR / "N" para VOLTAR:' + Style.RESET_ALL + " ").strip().upper()
        if resposta == 'S':
            return True
        elif resposta == 'N':
            return False
        else:
            print(cor_fundo + cor_texto + "Opção inválida. Por favor, digite 'S' para Sim ou 'N' para Não." + Style.RESET_ALL)


def realizar_saque():
    global saques_realizados
    nome = "Saque"
    maximo_saque = MAXIMO_SAQUE
    limite_saques = LIMITE_SAQUES
    global saldo, extrato
    #etapa 1
    iniciar_interface(nome, "Deseja realizar um saque?")
    start = interface_de_confirmacao()
    while start == True:
        print("\n")
        if saques_realizados >= limite_saques:
            iniciar_interface(nome, "Você não tem saques para hoje.")
        else:
            while True:
                iniciar_interface(nome, f"Você tem {limite_saques-saques_realizados} restantes hoje.")
                saque = float(input(cor_fundo + f'digite o valor do teu saque >>>' + Style.RESET_ALL + "  "))
                if saque > maximo_saque or saque > saldo:
                    iniciar_interface(nome, "Seu saque é maior doque o permitido!")
                    start = interface_de_confirmacao()
                    if start:
                        continue
                    break
                else:
                    saldo -= saque
                    iniciar_interface(nome, f"Saque de R${saque:.2f} realizado com sucesso")
                    print(f"\n")
                    print(f"Saldo atual de R${saldo:.2f}")
                    #atualização do extrato
                    extrato.append(f"saque : R${saque:.2f} ")
                    extrato.append(f"saldo : R${saldo:.2f} ")
                    print("\n")
                    saques_realizados += 1
                    opcao = input(cor_fundo + f'digite qualquer coisa para continuar >>>' + Style.RESET_ALL + "  ").strip().upper()
                    break
        break
def visualizar_extrato():
    nome = "Extrato"
    global extrato
    #etapa 1
    iniciar_interface(nome, "Deseja visualizar o seu extrato?")
    start = interface_de_confirmacao()
    while start == True:
        iniciar_interface(nome, "Esse é seu extrato de hoje")
        for item in extrato:
            print(f"{item}")
        opcao = input(cor_fundo + f'digite qualquer coisa para continuar >>>' + Style.RESET_ALL + "  ").strip().upper()
        break
def realizar_deposito():
    nome = "Depósitos"
    descricao = "Deseja Realizar um depósito?"
    iniciar_interface(nome, "Deseja realizar um deposito?")
    deposito = 0
    global saldo, extrato

    start = interface_de_confirmacao()
    while start == True:
        iniciar_interface(nome, "Faça seu deposito:")
        print("\n")
        deposito = float(input("Digite o valor do seu deposito:"))
        if deposito <= 0:
            continue
        else:
            iniciar_interface(nome, "Faça seu deposito:")
            print("\n")
            continuar = input(f"Confirmar o deposito de: R${deposito:.2f} (Y/N)")
            if continuar.upper() == "Y":
                break
            else:
                continue
    #atualização do saldo em conta
    saldo += deposito            
    
    #informativo para o usuário
    iniciar_interface(nome, "Informações do Deposito")
    print("\n")
    print(f"deposito de R${deposito:.2f} realizado com sucesso!")
    print(f"Seu saldo atual é de R${saldo:.2f}")
    #atualização do extrato
    extrato.append(f"deposito : R${deposito:.2f} ")
    extrato.append(f"saldo : R${saldo:.2f} ")
    #volta para o inicio
    seguir = input("\n \n Digite qualquer coisa para continuar:")

def aplicativo():
    rodar_aplicativo = True
    while rodar_aplicativo == True:
        iniciar_interface("PAGINA INICIAL", "Sistema bancário V2")
        print("""        (D) Deposito
        (S) Saques
        (E) Extrato    
        (Q) Sair
            
                    """)
        #ESCOLHER UMA DAS OPÇÕES:
        opcao = input(cor_fundo + f'digite uma das opções acima >>>' + Style.RESET_ALL + "  ").strip().upper()

        if opcao == "D": #FUNÇÕES DO DEPOSITO
            realizar_deposito() 
        elif opcao == "S": #funções do saque
            realizar_saque()
        elif opcao == "E":
            visualizar_extrato()      
        elif opcao == "Q":
            break 
        else:
            continue

aplicativo()