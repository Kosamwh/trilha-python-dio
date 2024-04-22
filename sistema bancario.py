menu = """
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



while True:
    opcao = input(menu)


  
    if opcao == "d":
        valor = float(input("Informe o valor do deposito: "))


        if valor > 0:
            saldo += valor
            extrato += f"Deposito R$ {valor:.2f}\n"



        else:   
            print ("Não foi possivel realizar essa operação! O valor informado é invalido")


    elif  opcao == "s":       
        valor = float(input("Informe o valor do saque: "))

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
            print("O valor informado é invalido!")



    elif opcao == "e":
        print("\n________ EXTRATO ________")
        print("Não foram realizadas nenhuma movimentação na conta." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("____________________________")

    
    elif opcao == "f":
     break


else:
    print("Numero digitado não se aplica ao menu, por favor selecione novamente.")
