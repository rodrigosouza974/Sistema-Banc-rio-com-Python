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
    def __init__(self, nome, cpf,data_nascimento,endereco):
        self.nome = nome
        self.cpf = cpf
        self.contas = []
        self.data_nascimento = data_nascimento
        self.endereço =  str(endereco)

    def formatar_cpf(self, cpf):
        return ''.join(filter(str.isdigit, cpf))

    def adicionar_conta(self,conta):
        self.contas.append(conta)
        return
        #ao não colocar o return aqui ele não me confirmou se existia alguém com o cpf já cadastrado
class Conta: #conta corrente
    
    def __init__(self, cliente):
        self.cliente = cliente
        self.saldo = 0.0
        self.transacoes = []
        self.lista_saque = []
        self.lista_deposito = []
        self.max_saques = 3
        self.contador_saques = 0
        self.numero = Conta.numero_sequencial
        Conta.numero_sequencial += 1
        self.agencia = "0001"

    def saque(self):
        if self.saldo <= 0:
            print("Você não possui saldo suficiente.")
            return
        
        saque = int(input("Qual a quantia deseja sacar: "))
        
        if saque > 500:
            print("O valor máximo de saque é 500. Operação cancelada.")
            return 
        
        if  self.contador_saques >= self.max_saques:
            print("Você atingiu o limite máximo de saques permitidos. Operação cancelada.")
            return 
        
        if saque > self.saldo :
            print("Saldo insuficiente para realizar o saque. Operação cancelada.")
            return
        
        self.saldo -= saque
        self.contador_saques += 1
        self.lista_saque.append(saque)
        print(f"Saque de {saque} realizado com sucesso!")  
        
    def deposito(self):
        try:
            deposito = int(input("Qual a quantia deseja depositar: "))
            if deposito > 0:
                self.saldo += deposito
                self.lista_deposito.append(deposito)
                print('Depósito realizado com sucesso!')
            else:
                print('O valor do depósito deve ser positivo.')
        except ValueError:
            print('Por favor, insira um valor numérico válido.')
            
    def extrato(self):
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

        print(f"Seu saldo atual é de {formatar_para_real(self.saldo)}\n")

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
    banco = Banco("Meu Banco")

    # Inicializando o banco
    banco = Banco("Meu Banco")

    # Adicionando um cliente fictício para teste
    cliente_ficticio = Cliente(
        nome="Rodrigo", 
        cpf="16924917763", 
        data_nascimento="06/07/19999", 
        endereco="Rua que não existe, 123"
    )
    banco.adicionar_cliente(cliente_ficticio)

    menu()

    while True:
        try:
            operacao = int(input("Digite o número da operação: "))

            if operacao == 1:
                nome = input("Nome do cliente: ")
                #verificação da entrada CPF
                while True:
                    cpf = input("CPF do cliente (apenas números): ")
                    if cpf.isdigit() and len(cpf) == 11:
                        break
                    else:
                        print("Entrada inválida! Por favor, digite apenas números e que seja um CPF válido com 11 dígitos.")
                data_nascimento = input("Data de nascimento do cliente (DD/MM/AAAA): ")
                logradouro = input("Informe o logradouro (Rua, Avenida, etc.): ")
                numero = input("Número: ")
                bairro = input("Bairro: ")
                cidade = input("Cidade: ")
                estado = input("Estado (sigla): ")

                # Função para formatar o endereço
                def formatar_endereco(logradouro, numero, bairro, cidade, estado):
                    endereco_formatado = f"{logradouro}, {numero} - {bairro} - {cidade}/{estado}"
                    return endereco_formatado
                # Formatando o endereço conforme especificação
                endereco_formatado = formatar_endereco(logradouro, numero, bairro, cidade, estado)
                
                print(f"{endereco_formatado}")

                # Criando um objeto Cliente com os dados fornecidos
                cliente = Cliente(nome, cpf,data_nascimento, endereco_formatado)
               
                # Adicionando o cliente ao banco
                if banco.adicionar_cliente(cliente):
                    print("Cliente adicionado com sucesso.")
                else:
                    print("Não foi possível adicionar o cliente. CPF já cadastrado.")

            elif operacao == 2:
                cpf = input("CPF do cliente (apenas números): ")
                # Procura pelo cliente na lista de clientes do banco usando compreensão de lista
                cliente = next((c for c in banco.clientes if c.cpf == cpf), None)
                if cliente:
                    conta = banco.criar_conta(cliente)
                    print("Conta criada com sucesso.")
                else:
                    print("Cliente não encontrado.")
        
        # Operação Saque   
            elif operacao == 3: 
                cpf = input("CPF do cliente (apenas números): ")
                cliente = next((c for c in banco.clientes if c.cpf == cpf), None)
                if cliente:
                    conta = cliente.contas[0]  # Assumindo que o cliente possui pelo menos uma conta
                    conta.saque()
                else:
                    print("Cliente não encontrado.")
        # Operação Deposito
            elif operacao == 4:
                cpf = input("CPF do cliente (apenas números): ")
                cliente = next((c for c in banco.clientes if c.cpf == cpf), None)
                if cliente:
                    conta = cliente.contas[0]  # Assumindo que o cliente possui pelo menos uma conta
                    conta.deposito()
                else:
                    print("Cliente não encontrado.")
        # Operação Extrato  
            elif operacao == 5:
                cpf = input("CPF do cliente (apenas números): ")
                cliente = next((c for c in banco.clientes if c.cpf == cpf), None)
                if cliente:
                    conta = cliente.contas[0]  # Assumindo que o cliente possui pelo menos uma conta
                    conta.extrato()
                else:
                    print("Cliente não encontrado.")

            elif operacao == 0:
                print("Saindo do sistema. Até logo!")
                break
        except ValueError:
            print("Por favor, insira um número válido.")
        print()
    # Exibir o menu novamente após cada operação para referência
        menu()
# Chama a função principal do sistema bancário
sistema_bancario()


