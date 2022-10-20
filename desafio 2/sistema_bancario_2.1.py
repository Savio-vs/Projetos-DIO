
from model_SB import *

SAQUES_DIAS = 1

CLIENTES = []
CONTAS_CORRENTE = []
while True:
    
    var = view_1()
    if var =='1':
        criar_cliente(CLIENTES)
    
    elif var == '2':
        criar_conta_corrente(CLIENTES,CONTAS_CORRENTE)
    
    elif var =='3':
        listar_clientes(lista_clientes=CLIENTES)

    elif var =='4':
        if len(CONTAS_CORRENTE) != 0:
            conta = input("Numero da sua conta: ")
            entrada = True
        else:
            print("não existe contas cadastradas.")
            entrada = False
        while entrada:
            var = view_2()
            if var == 'D':
            
                depositar(CONTAS_CORRENTE , numero_conta=conta)
            
            elif var =='S':
                saque(CONTAS_CORRENTE,numero_conta=conta)
            
            elif var == 'E':
                extrato(CONTAS_CORRENTE,numero_conta=conta)

            elif var =='0':
                break
    
    elif var =='0':
        break

    else:
        print(f"'{var}'não é uma opção válida.\nInsira uma opção válida")
        
