'''Importa a classe cliente
Importa a classe base conta e suas subsclasses
importa a exceção personalizada para conta inexistente
'''
from entidades.cliente import Cliente
from entidades.conta import Conta,ContaCorrente,ContaPoupanca
from utilitarios.exceptions import ContaInexistenteError
class Banco:
    #construtor da classe banco
    def __init__(self,nome:str):
        #nome do banco
        self.nome=nome
        #dicionarios de clientes
        self._clientes= {}
        #dicionario de contas
        self._contas= {}
    #metodo para adicionar um novo cliente ao banco
    def adicionar_cliente(self,nome:str,cpf:str) -> Cliente:
        if cpf in self._clientes:
            print("Erro: Cliente com esse CPF já cadastrado")
            return self._clientes[cpf]
        #Cria objeto cliente e adiciona ao dicionário
        novo_cliente=Cliente(nome,cpf)
        self._clientes[cpf]=novo_cliente
        print(f"Cliente {nome} adicionado com sucesso")
        return novo_cliente
        
    #Metodo para criar uma conta para um cliente
    def criar_conta(self, cliente:Cliente, tipo: str) -> Conta:
        #Número da nova conta será baseado no total de contas +1
        numero_conta=Conta.get_total_contas()+1

        #Cria conta corrente se o tipo informado for "corrente"
        if tipo.lower() == 'corrente' :
            nova_conta= ContaCorrente(numero_conta,cliente)

        elif tipo.lower() == 'poupanca' :
            nova_conta= ContaPoupanca(numero_conta,cliente)
        else:

            print("Tipo de conta inválido. Escolha 'corrente' ou 'poupança'.")
            return None
        #Adiciona a conta ao dicionário de contas
        self._contas[numero_conta]=nova_conta
        #Associa a conta ao cliente
        cliente.adicionar_conta(nova_conta)
        print(f"Conta {tipo} nº {numero_conta} criada para o cliente {cliente.nome}.")
        return nova_conta
    #Método para buscar uma conta pelo número
    def buscar_conta(self,numero_conta:int) -> Conta:
        #Recuperar a conta do dicionário
        conta=self._contas.get(numero_conta)  #atributo privado
        #Se não encontrar, lança exceção personalizada
        if not conta:
            raise ContaInexistenteError(numero_conta)
        return conta