from Cliente import Cliente
from Conta import Conta

# Criando um cliente
nome = input("Digite o nome do cliente: ")
fone = input("Digite o N. de celular do cliente: ")
c1= Cliente(nome, fone)

# Criando uma conta
numero_conta = int(input("Digite o numero da conta: "))
conta=Conta(c1.get_nome(), numero_conta, 0)

# Menu de opções
while True:
    print("\n--- MENU ---")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Ver Extrato")
    print("0 - Sair")
    print()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor = float(input("Digite o valor para deposito: "))
        conta.deposita(valor)

    elif opcao == "2":
        valor = float(input("Digite o valor para saque: "))

    elif opcao == "3":
        conta.extrato()

    elif opcao == "0":
        print()
        print("Obrigado por usar o Sistama bancário!")
        break


    else:
        print("Opção invalida. Tente novamente.")
