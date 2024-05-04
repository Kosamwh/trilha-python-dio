import textwrap

def menu():
    menu = """ \n
    [c]\tCriar conta
    [u]\tNovo Usuario
    [v]\tListar contas
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [f]\tSair
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    
        if valor > 0:
            saldo += valor
            extrato += f"Deposito R$ {valor:.2f}\n"
            print("~~~~ Deposito realizado com sucesso. ~~~~")

        else:   
            print ("Não foi possivel realizar essa operação! O valor informado é invalido")
        
        return saldo, extrato



def saque( * ,saldo, extrato, limite, valor, numero_saques, limiteSaques):
    
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limiteSaques

        if excedeu_saldo:
             print("Saldo insuficiente, operação não realizada!")


        elif excedeu_limite:
                print("O valor do saque é acima do limite, operação não realizada.")


        elif excedeu_saques:
                print("Não foi possivel sacar, atingiu o limite diario.")  


        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Operação realizada! Aguarde alguns instantes o saque.")


        else :
            print("Operação falhou, o valor informado é invalido!")

        return saldo, extrato



def Exibirextrato (saldo, /, *, extrato ):
     print("\n ~~~~~~~~~~~~~~Extrato~~~~~~~~~~~~~~~~" )
     print("Não há nenhuma movimentação em sua conta!" if not extrato else extrato)
     print(f"\n Saldo:\t\tR${saldo:.2f}")
     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def criarUsuario(usuarios):
    cpf = input("informe seu CPF: \n")
    usuario = filtrar_Usuario(cpf, usuarios) 

    if usuarios:
        print(" \n CPF já está sendo utilizado!")
        return
    
    Nome = input("\n Informe seu nome completo:  \n")
    dataNascimento = input("\n Insira sua data de nascimento(dd-mm-aaaa):  \n")
    endereco = input("\n Digite seu endereço completo:  \n" )

    usuarios.append({"nome": Nome, "dataNascimento": dataNascimento, "cpf": cpf, "endereco": endereco})  
    print("~~~~~ Usuario cadastrado com sucesso!! ~~~~")


def filtrar_Usuario(cpf, usuario):
    usuario_filtrado = [usuario for usuario in usuario if usuario["cpf"]== cpf]
    return usuario_filtrado[0] if usuario_filtrado else None


def CriarConta (agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuario. \n")
    usuario = filtrar_Usuario(cpf, usuarios)

    if usuario:
        print("\n ~~~~~ Sua conta foi criada! ~~~~~~\n ")
        return {"agencia": agencia,"numero_conta": numero_conta, "usuario": usuarios}
    
    print("Não foi possível encontrar este usuario! Criação de conta suspendida.")


def listarContas(contas):
    for conta in contas:
        linha = f""""\
            Agencia:\t{conta['agencia']}
            Conta corrent:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print('=' * 100)
        print(textwrap.dedent(linha))



     

def main():
    LIMITESAQUE = 3
    AGENCIA = '0001'

    saldo = 0
    limite = 600
    extrato = ""
    numero_saques = 0
    usuario = []
    contas = [] 

    while True:
         opcao = menu()
        
         if opcao == "d":
              valor = float(input("Informe um valor para o deposito: \n"))
              
              saldo, extrato = depositar(saldo, valor, extrato)

         elif opcao == "s":
              valor = float(input("Informe a quantia de saque: \n"))

              saldo, extrato = saque(
                   
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numeroSaques=numero_saques,
                limiteSaques=LIMITESAQUE,
            )

         elif opcao == "e":
            Exibirextrato(saldo, extrato=extrato)
         
         elif opcao == "c":
              criarUsuario(usuario)


         elif opcao == "u":

            numero_conta = len(contas) + 1
            conta = CriarConta(AGENCIA, numero_conta, usuario)

            if conta:
               contas.append(conta)

         elif opcao == "v":
              listarContas(contas)
         
         elif opcao == "f":
              break
         
         else:
           print("Numero digitado não se aplica ao menu, por favor selecione novamente.")
main()
         



