menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
valores_saques = []
valores_depositos = []
numero_saques = 0
LIMITE_SAQUES = 3
quantidade_deposito = 0

while True:
    opcao = input(menu)
    
    if opcao == "d":
        valor_deposito = float (input("Digite o valor que deseja depositar(OBS: somente valores positivos):  "))
        if(valor_deposito >= 0):
            saldo =+ valor_deposito
            valores_depositos.append(valor_deposito)
            print("Depósito concluído")
        else:
            print("valor inválido")
        
    elif opcao == "s":
        valor_saque = float(input("OBS: Só se pode realizar 3 saques diários e o valor máximo do saque é de R$500,00 \n Digite o valor do saque:"))
        if(numero_saques>=LIMITE_SAQUES):
            print("Transação não efetuada: limite de saques diários alcançado, por favor tente novamente outro dia")
        elif(valor_saque> 500):
            print("Transação não efetuada:: o valor máximo de depósito é de 500 reais, por favor tente novamente com um valor menor")
        elif(saldo<valor_saque):
            print("Transação não efetuada: Saldo insuficiente")
        else:
            saldo -= valor_saque 
            numero_saques += 1
            valores_saques.append(valor_saque)
            print("Saque efetuado com sucesso, saldo atual: R${}".format(saldo))  
    elif opcao == "e":
        print("Saldo: R%{:.2f} \n Depósitos: {} \n Saques: {}".format(saldo, valores_depositos, valores_saques))
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
    
    
    