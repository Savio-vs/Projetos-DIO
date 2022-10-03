from datetime import date

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
        'cpf': cpf
    }
    lista_cliente.append(cliente)

def criar_conta_corrente():
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

'''função de saque ok!!!'''
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
        
    
'''função de deposito ok!!!'''
def depositar(valor_deposito,valor_conta,extrat):
    if valor_deposito > 0:
        valor_conta = round(valor_conta +valor_deposito,2)
        extrat.append(f"R$ {valor_deposito} deposito em {date.today()}")
        return valor_conta
    else:
        print("Não é possivel depositar um valor negativo!")
        return valor_conta
    
'''função de extrato ok!!!'''
def extrato(valor_conta,extrat):
    print(f"\nValor em conta: {valor_conta}")
    for i in range(len(extrat)):
        print(extrat[i])
