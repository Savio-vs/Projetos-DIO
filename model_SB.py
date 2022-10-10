from datetime import date
<<<<<<< HEAD


CONTATOR_CONTAS = 0

=======
CONTATOR_CONTAS = 1
>>>>>>> 5cd1fdecf22480f468f813fb9069108de1bf8c41
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
<<<<<<< HEAD
        'numero_conta': '0'
=======
        'conta': '0'
>>>>>>> 5cd1fdecf22480f468f813fb9069108de1bf8c41
    }
    arquivo = open('clientes.txt','a')
    arquivo.write("Nome: "+cliente['nome'])
    arquivo.write("\nCPF: "+cliente['cpf'])
    arquivo.write("\nData de nascimento: "+cliente['dataNasc'])
    arquivo.write("\nNumero de nascimento: "+cliente['numero_conta']+"\n")
    
    arquivo.close()
    #lista_cliente.append(cliente)

def criar_conta_corrente(lista_cliente,lista_conta):
<<<<<<< HEAD
    
    global CONTATOR_CONTAS  
    CONTATOR_CONTAS = CONTATOR_CONTAS + 1
=======
    global CONTATOR_CONTAS
    numero = str(CONTATOR_CONTAS)
    CONTATOR_CONTAS = CONTATOR_CONTAS +1

>>>>>>> 5cd1fdecf22480f468f813fb9069108de1bf8c41
    usuario = input("Usuario da conta(CPF): ")
   
    for i in range(len(lista_cliente)):
        conta_cliente = lista_cliente[i]
        
        print(f"CPF ->{conta_cliente['cpf']} -> {usuario}")

        if conta_cliente['cpf'] in usuario :
            
            conta = {
            'agencia': '0001',
<<<<<<< HEAD
            'numero': str(CONTATOR_CONTAS),
            'usuario': conta_cliente['nome'],
            'saldo': 0
            }
            conta_cliente['numero_conta'].append(conta['numero']) 
            lista_conta.append(conta)
        else:
            x=input("""
            Usuário inexistente:
            Deseja tentar novamente?(S/N)
            """).upper()
            if x == 'S':
                criar_conta_corrente(lista_cliente,lista_conta)
            else:
                pass
=======
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
>>>>>>> 5cd1fdecf22480f468f813fb9069108de1bf8c41
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
        
    

<<<<<<< HEAD
def depositar(conta_corrente,extrat):
    if len(conta_corrente) != 0:
        conta  = input("Informe o numero da sua conta")
        for i in range(len(conta_corrente)):
            verificar_conta = conta_corrente[i]

            if verificar_conta['numero'] in conta:
                valor_deposito = float(input("Insira o valor que deseja depositar: "))
                if valor_deposito > 0:
                    verificar_conta['valor_conta'] = round(verificar_conta['valor_conta'] + valor_deposito,2)
                    extrat.append(f"R$ {valor_deposito} deposito em {date.today()}")
                    
                else:
                    print("Não é possivel depositar um valor negativo!")
            else:
                x=input("""
                Conta inexistente:
                Deseja tentar novamente?(S/N)
                """).upper()
                if x == 'S':
                    depositar(conta_corrente,extrat)
                else:
                    pass
    else:
        print("não existem contas cadastradas:\n")           
=======
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

>>>>>>> 5cd1fdecf22480f468f813fb9069108de1bf8c41
        
            
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
