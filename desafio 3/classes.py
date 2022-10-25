class Cliente:
    def __init__(self,endereco) -> None:
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self,conta):
        pass
    def adicionar_conta(self,numero):     
        self.contas.append(Conta_corrente(numero,PessoaFisica.nome))

class PessoaFisica(Cliente):
    def __init__(self,nome,nascimento,cpf,**kw) -> None:
        self._nome = nome
        self._data = nascimento
        self._cpf=cpf
        super().__init__(**kw)

    def __str__(self) -> str:
        numero=[]
        for i in self.contas:
            numero.append(i.numero)
        return f'\
        Nome:{self.nome}\n\
        CPF:{self._cpf}\n\
        Data de Nascimento:{self._data}\n\
        Endereço:{self.endereco}\n\
        Nº da Conta registrada: {numero}\n'
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def cpf(self):
        return self._cpf

class Conta():
    def __init__(self,numero,cliente) -> None:
        self._saldo = 0
        self._numero = numero
        self._cliente = cliente
        self._agencia = '0001'
        self._historico = Historico()
    
    @classmethod
    def nova_conta(cls,numero,cliente):
        return cls(numero,cliente)

    @property
    def cliente(self):
        return self._cliente    
    @property
    def numero(self):
        return self._numero
    
    def Saque(self,valor):
        if valor > 500:
            print("valor de saque superior ao permitido.")
        elif valor > self._saldo:
            print("saldo em conta insuficiente")
        
        else:
            self._saldo = round(self._saldo - valor,2)
            self._historico.Transacao('Saque',valor)
        
            
    
    def Deposito(self,valor):
        if valor > 0 :
            self._saldo += valor 
        self._historico.Transacao('Deposito',valor)
        

class Conta_corrente(Conta):
    def __init__(self,numero,cliente) :
        self._limite = 780
        self._limite_saques = 1
        super().__init__(numero,cliente)
    
    def Saque(self, valor):
        if self._limite_saques > 3:
            print("Saques diarios exedidos.")
        else:
            super().Saque(valor)
            self._limite_saques+=1

    def __str__(self) -> str:
        return f'saldo em conta >{self._saldo}\n\
        {self._historico.imprimir()}'
        
    

class Historico():
    def __init__(self) :
        self.extrato = []
    
    def Transacao(self,tipo,valor):
        self.extrato.append(f'transação: {tipo} -- R${valor}')
    
    def imprimir(self):
        for i in self.extrato:
            print(i)
def view_1():
   
    var = input("""
    [1] Cadastrar Cliente:
    [2] Criar Conta:
    [3] Listar Clientes:
    [4] Utilizar uma conta:
    [0] Sair do Sistema:
                """)   
    return var
    
def view_2():

    var = input("""
    [D] Depositar valor:
    [S] Sacar valor:
    [E] Visualizar Extrato:
    [0] Sair do Sistema:
                """).upper()
    return var