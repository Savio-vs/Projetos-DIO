from datetime import date


CONTATOR_CONTAS = 0

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
        'numero_conta': '0'
    }
    arquivo = open('clientes.txt','a')
    arquivo.write("Nome: "+cliente['nome'])
    arquivo.write("\nCPF: "+cliente['cpf'])
    arquivo.write("\nData de nascimento: "+cliente['dataNasc'])
    arquivo.write("\nNumero de nascimento: "+cliente['numero_conta']+"\n")
    
    arquivo.close()
    #lista_cliente.append(cliente)

def criar_conta_corrente(lista_cliente,lista_conta):
    
    global CONTATOR_CONTAS  
    CONTATOR_CONTAS = CONTATOR_CONTAS + 1
    usuario = input("Usuario da conta(CPF): ")
   
    for i in range(len(lista_cliente)):
        conta_cliente = lista_cliente[i]
        if conta_cliente['cpf'] in usuario:
            conta = {
            'agencia': '0001',
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
def listar_clientes(lista_clientes):
    for i in range (len(lista_clientes)):
            view = lista_clientes[i]
            print(f"""
            Cliente {i+1}
            Nome:{view['nome']}
            Data de Nascimento:{view['dataNasc']}
            Endereço: {view['endereco']}
            CPF: {view['cpf']}
            """)


def saque(valor_saque,saque_dias,valor_conta,extrato):
    if saque_dias > 3:
        print("\nLimite de saque diario exedido:")
        return valor_conta,saque_dias
    
    elif valor_conta > valor_saque:
        if valor_saque > 500:
            print("""
            valor de saque indisponivel:
            Valor Máximo de saque é de R$ 500.       
                    """)
            return valor_conta,saque_dias

        elif valor_conta >= valor_saque:
            valor_conta = round(valor_conta - valor_saque,2)
            extrato.append(f"R$ {valor_saque} saque em {date.today()}")
            
            saque_dias+=1
            return valor_conta,saque_dias
        else:
            print("Saldo em conta indisponivel:")
    else:
        print("Saldo insuficiente:")
        
    

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
        
            
'''função de extrato ok!!!'''
def extrato(valor_conta,extrat):
    print(f"\nValor em conta: {valor_conta}")
    for i in range(len(extrat)):
        print(extrat[i])
