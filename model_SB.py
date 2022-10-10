from datetime import date
CONTATOR_CONTAS = 1
def criar_cliente(lista_cliente):
    nome = input("Nome: ")
    nascimento = input("Data de nascimento: ")
    endereco = input("Endereço: ")
    cpf = input("CPF: ")
    for i in range (len(lista_cliente)):
        cliente_cpf = lista_cliente[i]
        if cliente_cpf['cpf'] in cpf:
            print("\nCPF já cadastrado.\nTente outro:")
            criar_cliente(lista_cliente)
        else:
            break

    cliente = {
        'nome': nome,
        'dataNasc': nascimento,
        'endereco': endereco,
        'cpf': cpf,
        'conta': '0'
    }
    lista_cliente.append(cliente)

def criar_conta_corrente(lista_cliente,lista_conta):
    global CONTATOR_CONTAS
    numero = str(CONTATOR_CONTAS)
    CONTATOR_CONTAS = CONTATOR_CONTAS +1

    usuario = input("Usuario da conta(CPF): ")
   
    for i in range(len(lista_cliente)):
        conta_cliente = lista_cliente[i]
        
        print(f"CPF ->{conta_cliente['cpf']} -> {usuario}")

        if conta_cliente['cpf'] in usuario :
            
            conta = {
            'agencia': '0001',
            'numero': numero,
            'usuario': conta_cliente['nome'],
            'valor_conta': 0,
            'extrato':[],
            'qtd_saques':1
            }
            conta_cliente['conta'] = numero
            lista_conta.append(conta)
        else:
            """print("Usuário inexistente:\n")
            criar_conta_corrente(lista_cliente,lista_conta)
    """
def listar_clientes(lista_clientes):
    for i in range (len(lista_clientes)):
            view = lista_clientes[i]
            print(f"""
            Cliente {i+1}
            Nome:{view['nome']}
            Data de Nascimento:{view['dataNasc']}
            Endereço: {view['endereco']}
            CPF: {view['cpf']}
            Conta Corrente: {view['conta']}
            """)


def saque(conta_corrente,numero_conta):
    

    for i in range(len(conta_corrente)):
        conta = conta_corrente[i]
        if conta['numero'] in numero_conta:
            valor_saque = float(input("Insira o valor que deseja sacar: "))
    
    if conta['qtd_saques'] > 3:
        print("\nLimite de saque diario exedido:")
        
    elif conta['valor_conta'] > valor_saque:
        if valor_saque > 500:
            print("""
            valor de saque indisponivel:
            Valor Máximo de saque é de R$ 500.       
                    """)
            

        elif conta['valor_conta'] >= valor_saque:
            conta['valor_conta'] = round(conta['valor_conta'] - valor_saque,2)
            conta['extrato'].append(f"R$ {valor_saque} saque em {date.today()}")
            
            conta['qtd_saques']+=1
            
        else:
            print("Saldo em conta indisponivel:")
    else:
        print("Saldo insuficiente:")
        
    

def depositar(conta_corrente,numero_conta):
    
    for i in range(len(conta_corrente)):
        conta = conta_corrente[i]
        if conta['numero'] in numero_conta:
            valor_deposito = float(input("Insira o valor que deseja depositar: "))
            if valor_deposito > 0:
                conta['valor_conta'] = round(conta['valor_conta'] +valor_deposito,2)
                conta['extrato'].append(f"R$ {valor_deposito} deposito em {date.today()}")
                
            else:
                print("Não é possivel depositar um valor negativo!")
        else:
            print('Conta inexistente.')     

        
            
'''função de extrato ok!!!'''
def extrato(conta_corrente,numero_conta):
    for i in range(len(conta_corrente)):
        conta = conta_corrente[i]
        if conta['numero'] in numero_conta:
            print(f"\nValor em conta: {conta['valor_conta']}")
            for i in conta['extrato']:
                print(i)

def view_1():
    var = input("""
    [1] Cadastrar Cliente:
    [2] Cadastrar Conta Corrente:
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
