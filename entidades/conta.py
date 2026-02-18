'''Importa a classe base abstrata e o decorador para métodos abstratos
importa a classe datatime para registrar a data e a hora das transações
importa exceção personalizada para saldo insuficiente
'''
from abc import ABC, abstractmethod
from datetime import datetime
from utilitarios.exceptions import SaldoInsuficienteError

'''Define a classe abstrata Conta, que serve como base para outros tipos de conta
Atributo de classe que calcula quantas contas foram criadas
Construtor de classe
Numero da conta (atributo protegido)
Saldo da conta (atributo protegido)
Referencia ao cliente dona da conta
Lista para armazenar histórico de transações (atributo protegido)
Incrementa o total de contas criadas (atributo protegido)
'''
class Conta(ABC):
    _total_contas=0
    def __init__ (self,numero:int,cliente):
        self._numero=numero
        self._saldo=0.0
        self._cliente=cliente
        self._historico=[]
        self._total_contas+=1
    #Propriedade para acessar o saldo de forma controlada
    @property
    def saldo(self):
        return self._saldo
    #Metodo de classe para consultar o número
    @classmethod
    def get_total_contas(cls):
        return cls._total_contas
    #Metodo para realizar depósitos
    def depositar(self,valor:float):
        if valor>0:
            self._saldo+=valor
            self._historico.append((datetime.now(),f"Depósito de R$ {valor:.2f}"))
            print (f"Depósito de R${valor:.2f} realizado com sucesso")
        else:
            print("Valor de depósito inválido.")
    #Metodo abstrato que deve ser implementado pelas subclasses
    @abstractmethod
    def sacar(self,valor:float):
        pass
    #Metodo para exibir o extrato da conta
    def extrato (self):
        print(f"\n--Extrato da Conta N {self._numero} ---")
        print(f"Cliente: {self._cliente.nome}")
        print(f"Saldo atual: R$ {self._saldo:2.f}")
        print("Histórico de transações:")
        if not self._historico:
            print("Nenhuma transação registrada")
        for data,transacao in self._historico:
            print(f"- {data.strftime('%d/%m/%Y %H:%M:%S')} : {transacao}")
            print("---------------------------------\n")

#Define a subclasse ContaCorrente
class ContaCorrente(Conta):
    #Construtor com limite padrão de cheque especial
    def __init__(self,numero:int,cliente,limite:float=500.0):
        #Chama o construtor da classe base
        super().__init__(numero,cliente)
        #Define o limite do cheque especial
        self.limite=limite
    #Implementação do método sacar com cheque especial
    def sacar(self,valor:float):
        if valor <=0:
            print("Valor de saque inválido")
            return
        #Calcula o saldo disponível (saldo+limite)
        saldo_disponivel=self.saldo + self.limite
        if valor>saque_disponivel:
            raise SaldoInsuficienteError(saldo_disponivel,valor,"Saldo e limite insuficientes")
        #Deduz o valor do saque do saldo
        self._saldo-=valor
        #Registra a transição no histórico
        self._historico.append((datetime.now(),f"Saque de R${valor:.2f}"))
        print(f"Saque de R{valor:.2f} realizado com sucesso.")
#Define a subclasse ContaPoupança
class ContaPoupanca(Conta):
    #Construtor da poupança herda do construtor base
    def __init__(self,numero:int,cliente):
        super().__init__(numero,cliente)
    #Metodo sacar apenas com saldo disponível
    def sacar (self,valor:float):
        if valor <=0:
            print("Valor de saque inválido")
            return
        if valor>self._saldo:
            raise SaldoInsuficienteError(self._saldo,valor)
        #Deduz o valor do saldo
        self._saldo-=valor
        #Registra transição no histórico
        self._historico.append((datetime.now(),f"Saque de R$ {valor:.2f}"))
        print(f"Saque de R${valor:.2f} realizado com sucesso.")

