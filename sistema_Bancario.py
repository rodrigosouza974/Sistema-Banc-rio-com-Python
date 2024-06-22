class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.clientes = []
        self.contas = []
        self.cpf_set = set()  # Usado para rastrear CPFs únicos

    def adicionar_cliente(self, cliente):
        if cliente.cpf in self.cpf_set:
            print("Erro: Já existe um cliente com esse CPF.")
            return False
        self.clientes.append(cliente)
        self.cpf_set.add(cliente.cpf)
        return True
    
    def criar_conta(self, cliente):
        nova_conta = Conta(cliente)
        self.contas.append(nova_conta)
        cliente.adicionar_conta(nova_conta)
        return nova_conta

class Cliente:
    def __init__(self, nome, cpf,data_nascimento,endereço):
        self.nome = nome
        self.cpf = cpf
        self.contas = []
        self.data_nascimento = data_nascimento
        self.endereço = endereço

    def formatar_cpf(self, cpf):
        return ''.join(filter(str.isdigit, cpf))

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class Conta:
    def __init__(self, cliente):
        self.cliente = cliente
        self.saldo = 0.0
        self.transacoes = []

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
    
    1. Adicionar Cliente
    2. Criar Conta
    3. Sacar
    4. depositar
    5. Extrato
    0. Sair

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

            if operacao == '1':
                nome = input("Nome do cliente: ")
                cpf = input("CPF do cliente (apenas números): ")
                endereco = input("Endereço do cliente (logradouro, nro - bairro - cidade/sigla estado): ")
                cliente = Cliente(nome, cpf, endereco)
                if Banco.adicionar_cliente(cliente):
                    print("Cliente adicionado com sucesso.")

            elif operacao == '2':
                cpf = input("CPF do cliente (apenas números): ")
                cliente = next((c for c in Banco.clientes if c.cpf == cpf), None)
                if cliente:
                    conta = Banco.criar_conta(cliente)
                    print("Conta criada com sucesso.")
                else:
                    print("Cliente não encontrado.")
                
            if operacao == 3:
                saldo, lista_saque, contador_saques = saque(saldo, max_saques, lista_saque, contador_saques)
            elif operacao == 4:
                saldo, lista_deposito = deposito(saldo, lista_deposito)
            elif operacao == 5:
                extrato(saldo, lista_saque, lista_deposito)
            elif operacao == 0:
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


