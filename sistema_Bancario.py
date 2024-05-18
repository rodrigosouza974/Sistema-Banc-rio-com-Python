import locale
saldo=2000
saque=0
deposito= 0
opcao = -1
contador_saques = 0
lista_Saque =[]
limite_Saque =[]
max_saques = 2
lista_Deposito=[]
extrato =[]

print(
"""
==================================================
                  Página Inicial                   
==================================================

Bem-vindo à nossa aplicação! Aqui estão algumas 
informações importantes:

- Opção 1: [1] Sacar
- Opção 2: [2] depositar
- Opção 3: [3] Extrato
- Opção 0: [0] Sair

Por favor, escolha uma das opções acima para 
continuar.

==================================================
"""
)
while opcao != 0:
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        if saldo > 0:
            if saque <= 500 : 
                if contador_saques <= max_saques:
                    saque =int(input("Qual a quantia deseja sacar: "))
                    saldo -= saque
                    contador_saques += 1
                    print(f"Saque de {saque} realizado com sucesso!")
                    #ao realizar a ação a variavel lista_Saque armazena ação em uma lista
                    lista_Saque.append(saque)
                else:
                    print("Você atingiu o limite máximo de saques permitidos.Sua operação foi cancelada.")
            else:
                    print("Limite de Saque Excedido. Sua operação foi cancelada")
        else:
            print("Você não possui saldo suficiente")

    elif opcao == 2:
        deposito =int(input("Qual a quantia deseja depositar: "))
        saldo += deposito
        lista_Deposito.append(deposito)
        print('Deposito Realizado.')

      
    elif opcao == 3:
        # Função para formatar os valores em reais
        def formatar_para_real(valor):
            return f"R${valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

        # Converter e imprimir a lista de saques formatados em reais
        saques_formatados = [formatar_para_real(saque) for saque in lista_Saque]

        # Exibir os saques formatados
        for saque_formatado in saques_formatados:
            print(saque_formatado)

    elif opcao == 0:
        print('Operação finalizada.')
    elif opcao != 0:
        print("Opção inválida. Por favor, escolha novamente.")

print("Obrigado por usar nosso sistema bancário. Até logo!")


