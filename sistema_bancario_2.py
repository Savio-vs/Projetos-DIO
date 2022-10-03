from model_SB import *

SAQUES_DIAS = 1
VALOR_EM_CONTA =[]
EXTRATO = []
CLIENTES = []
CONTAS_CORRENTE = []
while True:
    var = input("""
    [1] Cadastrar Cliente:
    [2] Cadastrar Conta Corrente:
    [3] Listar Clientes:
    [4] Depositar valor:
    [5] Sacar valor:
    [6] Visualizar Extrato:
    [0] Sair do Sistema:
                """)
    if var =='1':
        criar_cliente(CLIENTES)
    
    elif var == '2':
        criar_conta_corrente(CLIENTES,CONTAS_CORRENTE)
        print(CONTAS_CORRENTE)
    elif var =='3':
        listar_clientes(lista_clientes=CLIENTES)
            
    elif var == '4':
       
        depositar(CONTAS_CORRENTE,EXTRATO)
        print(CONTAS_CORRENTE)
    
    elif var =='5':
        valor = float(input("Insira o valor que deseja sacar: "))
        VALOR_EM_CONTA,SAQUES_DIAS = saque(valor,saque_dias=SAQUES_DIAS,valor_conta=VALOR_EM_CONTA,extrato=EXTRATO)
    
    elif var == '6':
        extrato(VALOR_EM_CONTA,EXTRATO)

    elif var =='0':
        break
    else:
        print(f"'{var}'não é uma opção válida.\nInsira uma opção válida")
        