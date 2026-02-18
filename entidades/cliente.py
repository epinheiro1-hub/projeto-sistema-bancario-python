'''Módulo entidade Cliente
    Definir a classe cliente
    Método construtor que inicializa os atributos da classe (nome,cpf)
    Atributo para armazenar nome do cliente 
    Atributo para armazenar cpf do cliente
    Lista vazia para armazenar as contas associadas ao cliente
    Método para adicionar a conta na lista de contas do cliente
    Insere o objeto contas na lista de contas
    Método especial que define a representação em string do objeto
    retorna uma string formatada com nome e cpf do cliente

'''
class Cliente: 
    def __init__(self,nome: str ,cpf: str):
        self.nome=nome
        self.cpf=cpf
        self.contas=[]
    def adicionar_conta(self,conta):
        self.contas.append(conta)
    def __str__(self):
        return f"Cliente: {self.nome} CPF: {self.cpf}"