menu = """
[c] Criar conta
[v] Dados bancarios
[d] Depositar
[s] Sacar
[e] Extrato
[f] Sair
"""
saldo = 0
limite = 600
extrato = ""
numeros_saques = 0
LIMITES_SAQUES = 3

from random import randint
agencia = randint(00000, 9999)

loginUsuario = { 'senha': [] }
contas = {'agencia' : [], 'saldo' : [], 'extrato' : [] , 'contaCorrente' : []}
usuario = {'nome' : [], 'dataNascimento' : [], 'CPF' : [], 'endereco' : [] }

while True:
    opcao = input(menu)
    if opcao == "c":
    
        Nome = input("\n Informe seu nome completo:  \n")
        dataNascimento = input("\n Insira sua data de nascimento:  \n")
        CPF = input("\n Informe seu CPF:  \n")
        endereco = input("\n Digite seu endereço completo:  \n" )
        

        usuario['nome'].append(Nome)
        usuario['dataNascimento'].append(dataNascimento)
        usuario['CPF'].append(CPF)
        usuario['endereco'].append(endereco)
        

        contas['agencia'].append(agencia)
        contas['extrato'].append(extrato)

        valor = float(input("Deposite um valor para ativar sua conta! \n"))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito abertura de conta: R$ {valor:.2f}\n"
        
       
    if opcao == "v":
        print(usuario["nome"])
        print(usuario["dataNascimento"])
        print(usuario["CPF"])
        print(usuario["endereco"])
        print(contas["agencia"])
        print("[Conta corrente]")
  
    if opcao == "d":
        
        valor = float(input("Informe o valor do deposito: \n"))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito R$ {valor:.2f}\n"

        else:   
            print ("Não foi possivel realizar essa operação! O valor informado é invalido")


    elif  opcao == "s":       
        valor = float(input("Informe o valor do saque: \n"))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numeros_saques >= LIMITES_SAQUES

        if excedeu_saldo:
             print("Saldo insuficiente, operação não realizada!")
    
        elif excedeu_limite:
                print("O valor do saque é acima do limite, operação não realizada.")

        elif excedeu_saques:
                print("Não foi possivel sacar, atingiu o limite diario.")   
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numeros_saques += 1
        else :
            print("Operação falhou, o valor informado é invalido!")

    elif opcao == "e":
        print("\n=========== EXTRATO =============")
        print("Não foram realizadas nenhuma movimentação na conta." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===================================")

    
    elif opcao == "f":
     break

else:
    print("Numero digitado não se aplica ao menu, por favor selecione novamente.")
