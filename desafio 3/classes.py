
from distutils.command.clean import clean


class cliente:
    def __init__(self,nome,nascimento,endereco,cpf) -> None:
        self.nome = nome
        self.data = nascimento
        self.endereco = endereco
        self.cpf=cpf

    
class conta_corrente(cliente):
    def __init__(self,conta,**kw) -> None:
        self.conta = conta
        self.valor_em_conta = 0
        self.saques_diario = 1
        self.extrato = []
        super().__init__(**kw)
    
    def __str__(self) -> str:
        return f"\
        Nome:{self.nome}\n\
        CPF: {self.cpf}\n\
        Endereço: {self.endereco}\n\
        Conta: {self.conta}\n"
    
    def Extrato(self):
        print(f'\
        Usuário: {self.nome}\n\
        Valor em conta: {self.valor_em_conta}')
        for i in range(len(self.extrato)):
            print(self.extrato[i])
        
    
    def Saque(self,valor):
        if valor > 500:
            print("valor de saque superior ao permitido.")
        elif valor > self.valor_em_conta:
            print("saldo em conta insuficiente")
        elif self.saques_diario > 3:
            print("Saques diarios exedidos.")
        else:
            self.valor_em_conta = round(self.valor_em_conta - valor,2)
            self.extrato.append(f'Saque de R$ {valor}')
            self.saques_diario+=1
            print("Saque bem sucedido\nAguarde seu dinheiro. ")
    
    def Deposito(self,valor):
        self.valor_em_conta = valor 
        self.extrato.append(f'Deposito de R$ {valor}')
        
        print("Deposito concluido:")


def view_1():
    clean
    var = input("""
    [1] Criar Conta Corrente:
    [2] Listar Clientes:
    [3] Utilizar uma conta:
    [0] Sair do Sistema:
                """)   
    return var
    
def view_2():
    clean
    var = input("""
    [D] Depositar valor:
    [S] Sacar valor:
    [E] Visualizar Extrato:
    [0] Sair do Sistema:
                """).upper()
    return var

'''Teste
clientes=['savio','Paulo','Marcio']
contas=[]
for i in range(len(clientes)):
    c = conta_corrente(conta=(i+1),nome=clientes[i],nascimento= '25/02/1997',endereco='Rua 01',cpf='2020')
    contas.append(c) 


for i in contas:
    if i.conta == 2:
        print("achei a conta...")'''
    
        
