from datetime import date

SAQUES_DIAS = 1
VALOR_EM_CONTA = 0
EXTRATO = []
while True:
    var = input("""
    [d] Depositar valor:
    [s] Sacar valor:
    [e] Visualizar Extrato:
    [f] Sair do Sistema:
""").upper()
    
    if var == 'D':
        valor = float(input("Insira o valor que deseja depositar: "))
        if valor > 0 :
            VALOR_EM_CONTA = round(VALOR_EM_CONTA +  valor,2)
            EXTRATO.append(f"R$ {valor} depositado em {date.today()}")
        else:
            print("\ninsira um valor valor válido:\n")
    elif var == 'S':
        if SAQUES_DIAS > 3:
            print("Seu limite de saques diario foi exedido:")

        elif VALOR_EM_CONTA > 0 :
            valor = float(input("Insira o valor que deseja sacar: ")) 
            if valor > 500:
                print("""
                valor de saque indisponivel:
                Valor Máximo de saque é de R$ 500.       
                        """)
            elif VALOR_EM_CONTA >= valor:
                VALOR_EM_CONTA = round(VALOR_EM_CONTA - valor,2)
                EXTRATO.append(f"R$ {valor} saque em {date.today()}")
                SAQUES_DIAS+=1
            else:
                print("Saldo em conta indisponivel:")
        else:
            print("Saldo insuficiente:")
    
    elif var == 'E':
        print(f"\nValor em conta: {VALOR_EM_CONTA}")
        for i in range(len(EXTRATO)):
            print(EXTRATO[i])
    
    elif var =='F':
        break
    else:
        print(f"'{var}'não é uma opção válida.\nInsira uma opção válida")
        