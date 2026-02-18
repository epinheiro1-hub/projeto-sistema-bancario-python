'''Importa a classe Banco responsável por gerenciar clientes e contas
Importa exceções personalizadas usadas no fluxo de operações

'''
from operacoes.banco import Banco
from utilitarios.exceptions import SaldoInsuficienteError,ContaInexistenteError
#Função que exibe o menu principal da aplicação
def menu_principal():
    print("\n---Projeto Python Avançado -- Sistema bancário digital ---\n")
    print("1. Adicionar Cliente")
    print("2. Criar Conta")
    print("3. Acessar Conta")
    print("4. Sair\n")
    return input("Escolha uma opção : ")

#Função que exibe o menu de operaçõs de uma conta específica
def menu_conta(banco):
    try:
        num_conta=int(input("Digite o número da conta: "))
        conta=banco.buscar_conta(num_conta)
        while True:
            print(f"\n--- Operações para Conta N {conta._numero} ---")
            print(f"Cliente: {conta._cliente.nome} | Saldo: R${conta.saldo:.2f}")
            print("1. Depositar")
            print("2. Sacar")
            print("3. Ver Extrato")
            print("4. Voltar ao Menu Principal")

            opcao=input("Escolha uma opção : ")
            if opcao=='1':
                valor=float(input("Digite o valor para depósito "))
                conta.depositar(valor)
            elif opcao =='2':
                try:
                    valor=float(input("Digite o valor para saque "))
                    conta.sacar(valor)
                except SaldoInsuficienteError as e:
                    print(f"Erro na operação : {e}")
            elif opcao =='3':
                conta.extrato()
            elif opcao=='4':
                break
            else:
                print("Opção inválida. Tente novamente.")
    except ContaInexistenteError as e:
        print(f"Erro {e}")
    except ValueError:
        print("Erro: Entrada Inválida. Por favor, digite um número.")

#Função principal que controla o fluxo do sistema
def main():
    banco= Banco("Banco Digital Eduardo Antônio")
    while True:
        opcao= menu_principal()
        if opcao =='1':
            nome=input("Digite o nome do cliente: ")
            cpf=input("Digite o CPF do cliente: ")
            banco.adicionar_cliente(nome,cpf)
        elif opcao =='2':
            cpf=input("Digite o CPF do cliente para vincular a conta: ")
            cliente=banco._clientes.get(cpf)
            if cliente:
                tipo=input("Digite o tipo da conta (corrente/poupança): ")
                banco.criar_conta(cliente,tipo)
            else:
                print("Cliente não encontrado. Cadastre o cliente primeiro.")
        elif opcao=='3':
            menu_conta(banco)
        elif opcao=='4':
            print("\nObrigado por usar nosso sistema. Até logo!\n")
            break
        else:
            print("\nOpção inválida. Por favor, tente novamente.\n")
if __name__=="__main__":
    main()


