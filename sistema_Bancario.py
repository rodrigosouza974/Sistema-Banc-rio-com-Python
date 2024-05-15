sacar=0
depositar=0
visualizar_Extrato =""
opcao = -1


#exibe quais função voce quer realizar
opcao = -1  # Definindo uma opção inicial inválida para entrar no loop

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
        print('Saque realizado.')
    elif opcao == 2:
        print('Exibindo depositar.')
    elif opcao == 3:
        print('Exibindo extrato.')
    elif opcao != 0:
        print("Opção inválida. Por favor, escolha novamente.")

print("Obrigado por usar nosso sistema bancário. Até logo!")

#processa sua entrada
#retorna algo na tela
#
#
#