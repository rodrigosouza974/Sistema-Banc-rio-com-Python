
def saque(saldo, max_saques, lista_saque, contador_saques):
    if saldo <= 0:
        print("Você não possui saldo suficiente.")
        return saldo, lista_saque, contador_saques
    
    saque = int(input("Qual a quantia deseja sacar: "))
    
    if saque > 500:
        print("O valor máximo de saque é 500. Operação cancelada.")
        return saldo, lista_saque, contador_saques
    
    if contador_saques >= max_saques:
        print("Você atingiu o limite máximo de saques permitidos. Operação cancelada.")
        return saldo, lista_saque, contador_saques
    
    if saque > saldo:
        print("Saldo insuficiente para realizar o saque. Operação cancelada.")
        return saldo, lista_saque, contador_saques
    
    saldo -= saque
    contador_saques += 1
    lista_saque.append(saque)
    print(f"Saque de {saque} realizado com sucesso!")
    
    return saldo, lista_saque, contador_saques
     
def deposito(saldo, lista_deposito):
    """
    Realiza um depósito em uma conta bancária.

    Parâmetros:
    saldo (float): O saldo atual da conta.
    lista_deposito (list): A lista de depósitos realizados.

    Retorna:
    tuple: O saldo atualizado e a lista de depósitos.
    """
    try:
        deposito = int(input("Qual a quantia deseja depositar: "))
        if deposito > 0:
            saldo += deposito
            lista_deposito.append(deposito)
            print('Depósito realizado com sucesso!')
        else:
            print('O valor do depósito deve ser positivo.')
    except ValueError:
        print('Por favor, insira um valor numérico válido.')
        
    return saldo, lista_deposito

def extrato(saldo, lista_saque, lista_deposito):
    def formatar_para_real(valor):
        return f"R${valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

    saques_formatados = [formatar_para_real(saque) for saque in lista_saque]
    depositos_formatados = [formatar_para_real(deposito) for deposito in lista_deposito]

    print("\nExtrato:")
    print("Esses são os saques realizados:")
    for i, saque_formatado in enumerate(saques_formatados, start=1):
        print(f"{i}º saque: {saque_formatado}")

    print("Esses são os depósitos realizados:")
    for i, deposito_formatado in enumerate(depositos_formatados, start=1):
        print(f"{i}º depósito: {deposito_formatado}")

    print(f"Seu saldo atual é de {formatar_para_real(saldo)}\n")

def menu():
    print("""
==================================================
                  Página Inicial                   
==================================================

Bem-vindo à nossa aplicação! Aqui estão algumas 
informações importantes:

    1. Sacar
    2. depositar
    3. Extrato
    4. Sair

Por favor, escolha uma das opções acima para 
continuar.

==================================================
""")

def sistema_bancario():
    saldo = 2000
    lista_saque = []
    lista_deposito = []
    contador_saques = 0
    max_saques = 3

    menu()

    while True:
        try:
            operacao = int(input("Digite o número da operação: "))

            if operacao == 1:
                saldo, lista_saque, contador_saques = saque(saldo, max_saques, lista_saque, contador_saques)
            elif operacao == 2:
                saldo, lista_deposito = deposito(saldo, lista_deposito)
            elif operacao == 3:
                extrato(saldo, lista_saque, lista_deposito)
            elif operacao == 4:
                print("Saindo do sistema. Até logo!")
                break
            else:
                print("Operação inválida. Tente novamente.")
        except ValueError:
            print("Por favor, insira um número válido.")
        print()
    # Exibir o menu novamente após cada operação para referência
        menu()
# Chama a função principal do sistema bancário
sistema_bancario()

"""
#sistema bancario com usuário exemplo

class ContaBancaria: #funçoes sacar, depo, extrato
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
        self.extrato = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: +R${valor}")
            return f"Depósito de R${valor} realizado com sucesso."
        else:
            return "Valor de depósito inválido."

    def sacar(self, valor):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                self.extrato.append(f"Saque: -R${valor}")
                return f"Saque de R${valor} realizado com sucesso."
            else:
                return "Saldo insuficiente para saque."
        else:
            return "Valor de saque inválido."

    def ver_extrato(self):
        return "\n".join(self.extrato) if self.extrato else "Nenhuma transação realizada."

    def ver_saldo(self):
        return f"Saldo atual: R${self.saldo}"

# Função para exibir o menu e obter a escolha do usuário
def mostrar_menu():
    print("\n=== Sistema Bancário ===")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Ver Extrato")
    print("4. Ver Saldo")
    print("5. Sair")
    return input("Escolha uma opção: ")

# Função principal para executar o sistema bancário
def executar_banco():
    titular = input("Digite o nome do titular da conta: ")
    saldo_inicial = float(input("Digite o saldo inicial da conta: "))
    conta = ContaBancaria(titular, saldo_inicial)

    while True:
        opcao = mostrar_menu()
        
        if opcao == '1':
            valor = float(input("Digite o valor para depositar: "))
            print(conta.depositar(valor))
        elif opcao == '2':
            valor = float(input("Digite o valor para sacar: "))
            print(conta.sacar(valor))
        elif opcao == '3':
            print("=== Extrato ===")
            print(conta.ver_extrato())
        elif opcao == '4':
            print(conta.ver_saldo())
        elif opcao == '5':
            print("Saindo do sistema bancário. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

# Executando o sistema bancário
executar_banco()
"""

