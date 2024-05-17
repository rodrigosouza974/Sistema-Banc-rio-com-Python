saldo=2000
saque=0
deposito= 0
opcao = -1
lista_Saque =[]
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
        saque =int(input("Qual a quantia deseja sacar: "))
        saldo -= saque
        #ao realizar a ação a variavel lista_Saque armazena ação em uma lista
        lista_Saque.append(saque)
        print('Saque realizado.')

    elif opcao == 2:
        deposito =int(input("Qual a quantia deseja depositar: "))
        saldo += deposito
        lista_Deposito.append(deposito)
        print('Deposito Realizado.')

      
    elif opcao == 3:
        print(f"Esses foram os saques realizados: {lista_Saque}")
        print(f"Esses foram os saques realizados: {lista_Deposito}")

    elif opcao == 0:
        print('Operação finalizada.')
    elif opcao != 0:
        print("Opção inválida. Por favor, escolha novamente.")

print("Obrigado por usar nosso sistema bancário. Até logo!")


