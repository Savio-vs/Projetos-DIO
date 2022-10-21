from classes import *

CONTAS_CORRENTE = []
CONTADOR = 1
while True:
    
    var = view_1()
    if var =='1':
         
        c = conta_corrente(conta=CONTADOR,
        nome=input("Nome do cliente: "),
        nascimento=input("Data de Nascimento: "),
        endereco=input("Endereço: "),
        cpf=input("CPF: "))
        CONTAS_CORRENTE.append(c)
        CONTADOR+=1
    
    elif var =='2':
        for i in CONTAS_CORRENTE:
            print(i)

    elif var =='3':
        if len(CONTAS_CORRENTE) != 0:
            conta = int(input("Numero da sua conta: "))
            for i in CONTAS_CORRENTE:
                if i.conta == conta:
                    objeto = i
                    entrada = True
                else:
                    entrada=False
            if entrada == False:
                print("Conta Inexistente:")
        else:
            print("não existe contas cadastradas.")
            entrada = False
        while entrada:
            var = view_2()
            if var == 'D':
                valor = float(input("Valor de Deposito: "))
                objeto.Deposito(valor)
                
            elif var =='S':
                valor = float(input("Valor de Saque: "))
                objeto.Saque(valor)
            elif var == 'E':
                print(objeto.Extrato())
            elif var =='0':
                break
    
    elif var =='0':
        break

    else:
        print(f"'{var}'não é uma opção válida.\nInsira uma opção válida")
        
