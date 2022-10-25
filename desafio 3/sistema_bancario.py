from classes import *

lista_clientes = []
contador = 1
while True:
    
    var = view_1()
    if var =='1':# criação do cliente
        cliente = PessoaFisica(nome=input("Nome: "),    
        nascimento=input("Data de Nascimento: "),
        cpf=input("CPF: "),
        endereco=input("Endereço: "))
        lista_clientes.append(cliente)
        
    elif var == '2':# criação da conta
        saida=False
        cliente = input("informe o usuáro desta conta:")
        for i in lista_clientes:
            if i.nome == cliente:
                i.adicionar_conta(contador)
                contador+=1
                saida = True
        if saida==False:
            print("Cliente não encontrado.")
    
    elif var =='3':# listar clientes
        for i in lista_clientes:
            print(i)

    elif var =='4':# utilizar uma conta
        if len(lista_clientes) != 0:
            cpf = input("Identificador do Cliente(CPF):")
            for i in lista_clientes:
                if i.cpf == cpf:
                    if len(i.contas)==1:
                        objeto = i.contas[0]
                        entrada = True
                    
                    elif len(i.contas)>1:
                        conta = int(input("selecione uma conta:"))
                        for i in i.contas:
                            if i.numero == conta:
                                objeto = i
                                entrada = True
                    else:
                        entrada=False

                    
                else:
                    entrada=False
            if entrada == False:
                print("Erro 404!:")
        else:
            print("Não existe cadastros.")
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
                print(objeto)
            
            elif var =='0':
                break
    
    elif var =='0':
        break

    else:
        print(f"'{var}'não é uma opção válida.\nInsira uma opção válida")
        
