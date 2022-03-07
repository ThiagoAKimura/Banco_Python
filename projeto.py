import os
from datetime import date, datetime

#Função para criar novas contas!
def criarNovo():
    nome = input("Digite o nome: ")
    cpf = input("Digite o CPF: ")
    tipo_conta = input("Digite o tipo de conta(conta salário; comum e plus): ")
    valor_inicial = float(input("Digite o valor inicial da conta: "))
    senha = input("Crie uma senha: ")
    # Criação do extrato

    def createExtrato():
        data_operacao = datetime.now()
        data_hora_operacao = data_operacao.strftime('%d/%m/%Y %H:%M')
        extrato = open(cpf + " extrato" + ".txt", "w")
        extrato.write("Nome: %s\n" %nome)
        extrato.write("CPF: %s\n" %cpf)
        extrato.write("Tipo da conta: %s\n"  %tipo_conta.lower())
        extrato.write("Data: " + data_hora_operacao + " + %.2f" %valor_inicial + " Tarifa: 0.00" + " Saldo:  %.2f\n" %valor_inicial )
    createExtrato()

    #Condição para não criar clientes com o mesmo cpf

    if os.path.isfile(cpf+".txt"):
        print("Cliente já existente!")

    #Criação da conta em .txt

    else:
        arquivo = open(cpf+".txt", "w")
        arquivo.write("%s\n" %nome)
        arquivo.write("%s\n" %cpf)
        arquivo.write("%s\n" %tipo_conta.lower())
        arquivo.write("%.2f\n" %valor_inicial)
        arquivo.write("%s\n" %senha)
        arquivo.close()
        print("Obrigado por escolher o banco QuemPoupaTem!")


# Função para deletar contas

def deletar():
    senhas = []
    delet_cpf = input("Digite o cpf da conta que quer desativar: ")
    delet_senha = input("Digite a senha: ")
    if os.path.isfile(delet_cpf + ".txt"):
        arquivo = open (delet_cpf + ".txt", "r")
        a = arquivo.readlines()
        arquivo.close()
        for linha in a:
            senhas.append(linha.strip().split())
        for linha in range(len(senhas)):
            for coluna in range(len(senhas[linha])):
                if delet_senha == senhas[4][0]:
                    os.remove(delet_cpf+ ".txt")
                    os.remove(delet_cpf + " extrato" + ".txt")
                    print("Conta deletada! Esperamos ter você de volta um dia!")
                    break
                else:
                    print("Senha incorreta! Tentar novamente")
                    
            break
    else:
        print("Cliente inexistente! Tentar novamente")

# Funcao para debitar de uma conta!
                  
def debitar():

    data_operacao = datetime.now()
    data_hora_operacao = data_operacao.strftime('%d/%m/%Y %H:%M')

    senhas = []

    saldo = []

    tipo_contas = []

    debitar_cpf = input("Digite o cpf da conta que quer debitar: ")

    debitar_senha = input("Digite a senha: ")

    debitar_valor = float(input("Digite o quanto você quer debitar: "))

    tarifa_salario = debitar_valor * 0.05
    tarifa_comum = debitar_valor * 0.03
    tarifa_plus = debitar_valor * 0.01

    conta_salario = debitar_valor + tarifa_salario
    conta_comum = debitar_valor + tarifa_comum
    conta_plus = debitar_valor + tarifa_plus

    if os.path.isfile(debitar_cpf + ".txt"):
        arquivo = open (debitar_cpf + ".txt", "r")
        a = arquivo.readlines()
        arquivo.close()
        for linha in a:
            senhas.append(linha.strip().split())
        for linha in range(len(senhas)):
            for coluna in range(len(senhas[linha])):
                if  debitar_senha == senhas[4][0]:
                    for linha in a:
                        tipo_contas.append(linha.strip().split())
                    for linha in range(len(tipo_contas)):
                        for coluna in range(len(tipo_contas[linha])):
                            if tipo_contas[2][0] == "salario":
                                for linha in a:
                                    saldo.append(linha.strip().split(': '))
                                for linha in range(len(saldo)):
                                    for coluna in range(len(saldo[linha])):
                                        if float(saldo[3][0]) > 0:
                                            novo_saldo = float(saldo[3][0]) - conta_salario
                                            arquivo = open(debitar_cpf + ".txt", "a")
                                            arquivo.write("%.2f\n" %novo_saldo)
                                            arquivo.close()
                                            extrato = open(debitar_cpf + " extrato" + ".txt" , "a")
                                            extrato.write("Data: " + data_hora_operacao + " - %s"  %str(debitar_valor) + " Tarifa: %.2f"  %(tarifa_salario) + " Saldo: %.2f\n" %(novo_saldo) )
                                            extrato.close()
                                            print("Transação Realizada!")
                                            return
                                        else:
                                            print("Impossivel realizar essa operação")

                            elif tipo_contas[2][0] == "comum":
                                for linha in a:
                                    saldo.append(linha.strip().split(': '))
                                for linha in range(len(saldo)):
                                    for coluna in range(len(saldo[linha])):
                                        if float(saldo[3][0]) > -500:
                                            novo_saldo = float(saldo[3][0]) - conta_comum
                                            arquivo = open(debitar_cpf + ".txt", "a")
                                            arquivo.write("%.2f\n" %novo_saldo)
                                            arquivo.close()
                                            extrato = open(debitar_cpf + " extrato" + ".txt" , "a")
                                            extrato.write("Data: " + data_hora_operacao + " - %s"  %str(debitar_valor) + " Tarifa: %.2f"  %(tarifa_comum) + " Saldo: %.2f\n" %(novo_saldo) )
                                            extrato.close()
                                            print("Transação Realizada!")
                                            return
                                            
                                        else:
                                            print("Impossivel realizar essa operação")
                                        
                            elif tipo_contas[2][0] == "plus":
                                for linha in a:
                                    saldo.append(linha.strip().split(': '))
                                for linha in range(len(saldo)):
                                    for coluna in range(len(saldo[linha])):
                                        if float(saldo[3][0]) > -5000:
                                            novo_saldo = float(saldo[3][0]) - conta_plus
                                            arquivo = open(debitar_cpf + ".txt", "a")
                                            arquivo.write("%.2f\n" %novo_saldo)
                                            arquivo.close()
                                            extrato = open(debitar_cpf + " extrato" + ".txt" , "a")
                                            extrato.write("Data: " + data_hora_operacao + " - %s"  %str(debitar_valor) + " Tarifa: %.2f"  %(tarifa_plus) + " Saldo: %.2f\n" %(novo_saldo) )
                                            extrato.close()
                                            print("Transação Realizada!")
                                            return
                                        else:
                                            print("Impossivel realizar essa operação")
    
                else:
                    print("Senha incorreta!!")
    else:
        print("CPF inválido!")
                    
# Função para depositar em uma conta!

def depositar():

    data_operacao = datetime.now()
    data_hora_operacao = data_operacao.strftime('%d/%m/%Y %H:%M')

    depositar_cpf = input("Digite o cpf da conta que quer depositar: ")

    depositar_valor = float(input("Digite o quanto você quer depositar: "))

    valores = []

    arquivo = open (depositar_cpf + ".txt", "r")
    a = arquivo.readlines()
    arquivo.close()

    if os.path.isfile(depositar_cpf + ".txt"):
        arquivo = open (depositar_cpf + ".txt", "r")
        a = arquivo.readlines()
        arquivo.close()
        for linha in a:
            valores.append(linha.strip().split())
        for linha in range(len(valores)):
            for coluna in range(len(valores[linha])):
                if float(valores[5][0]) > 0:
                    conta = float(valores[5][0]) + depositar_valor
                    arquivo = open(depositar_cpf + ".txt", "a")
                    arquivo.write("%.2f\n" %conta)
                    arquivo.close()
                    extrato = open(depositar_cpf + " extrato" + ".txt" , "a")
                    extrato.write("Data: " + data_hora_operacao + " + %s"  %str(depositar_valor) + " Tarifa: 0.00" + " Saldo: %s\n" %str(conta) )
                    extrato.close()
                    print("Transação Realizada!")
                    return
                else:
                    print("Impossivel realizar esta operação!")
    else:
        print("Cliente não encontrado!")
    
# Função para ver o saldo!

def saldo():
    cpf = input("Digite o cpf da conta que quer ver o saldo: ")
    senha = input("Digite a senha: ")

    senhas = []

    if os.path.isfile(cpf+".txt"):
        arquivo = open (cpf + ".txt", "r")
        a = arquivo.readlines()
        arquivo.close()
        for linha in a:
            senhas.append(linha.strip().split())
        for linha in range(len(senhas)):
            for coluna in range(len(senhas[linha])):
                if senha == senhas[4][0]:
                    print("Seu saldo é de: " + senhas[6][0])
                    return
                else:
                    print("Senha incorreta!")
    else:
        print("Cliente não encontrado!") 
    
# Função para ver o extrato!

def extrato():
    cpf = input("Digite o cpf da conta que quer ver o saldo: ")
    senha = input("Digite a senha: ")

    senhas = []

    senhas1 = []

    if os.path.isfile(cpf + ".txt"):
        arquivo = open (cpf + ".txt", "r")
        a = arquivo.readlines()
        arquivo.close()
        for linha in a:
            senhas1.append(linha.strip().split())
        for linha in range(len(senhas1)):
            for coluna in range(len(senhas1[linha])):
                if senha == senhas1[4][0]:
                    arquivo = open (cpf +" extrato" + ".txt", "r")
                    a = arquivo.readlines()
                    arquivo.close()
                    for linha in a:
                        senhas.append(linha.strip().split())
                    for linha in range(len(senhas)):
                            for coluna in range(len(senhas[linha])):
                                print(*senhas[0])
                                print(*senhas[1])
                                print(*senhas[2])
                                print(*senhas[3])
                                print(*senhas[4])
                                print(*senhas[5])
                                return
                else:
                    print("Senha incorreta!")
    else:
        print("Cliente não encontrado!")


def main():
    while True:
        print()
        print("Banco QuemPoupaTem")
        print()
        print("--- MENU ---")
        print()
        print("1- Criar novo cliente")
        print("2- Apaga cliente")
        print("3- Debita")
        print("4- Deposita")
        print("5- Saldo")
        print("6- Extrato")
        print()
        print()
        print("0- Sair")
        print()
        opcao = input("Escolha uma das opções: ")

        if opcao == "1":
            criarNovo()

        if opcao == "2":
            deletar()
        
        if opcao == "3":
            debitar()
        
        if opcao == "4":
            depositar()

        if opcao =="5":
            saldo()

        if opcao == "6":
            extrato()

        if opcao == "0":
            print("Obrigado! Até a proxima!")
            break


main()