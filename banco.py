
def menu():
    menu =  """
    ========================== MENU ==========================
    | [d]\tDepositar                                           |
    | [s]\tSacar                                               |
    | [e]\tExtrato                                             |
    | [nc]\tNova Conta                                         |
    | [lc] \tListar Contas                                     |
    | [nu]\tNovo Usuario                                       |
    | [q]\tSair                                                |
    ============================================================
    => """ 
    return menu


def deposito (saldo, valor, valores_depositos, /):
    if(valor_deposito >= 0):
            saldo =+ valor
            valores_depositos.append(valor_deposito)
            print("Depósito concluído")
    else:
            print("valor inválido")
    return saldo, valores_depositos

def cadastrar_usuario(usuarios):
    nome = input("Digite seu nome: ")
    cpf = input("Digite seu cpf: ")
    
    usuario = filtar_usuario(cpf, usuarios)
    if usuario:
        print("ERRO: Usuário já cadastrado")
        return
    
    idade = input("Digite a sua idade: ")
    celular = input("Digite o numero do seu celular: ")
    dados = {"nome": nome, "cpf":cpf, "idade":idade, "celular":celular}
    usuarios.append(dados)
    print("========================== Cadastro Concluído ==========================")
    
def filtar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
    
def saque (*,saldo, valor, valores_saques, limites_saques, qtde_saques, limite_valor):
    exec_saldo = valor>saldo
    exec_limite = valor>  limite_valor
    exec_saques= qtde_saques>limites_saques
      
    if exec_saldo:
            print("Transação não efetuada: limite de saques diários alcançado, por favor tente novamente outro dia")
    elif exec_limite:
            print("Transação não efetuada:: o valor máximo de depósito é de 500 reais, por favor tente novamente com um valor menor")
    elif exec_saques:
            print("Transação não efetuada: Saldo insuficiente")
    else:
            saldo -= valor
            qtde_saques += 1
            valores_saques.append(valor_saque)
            print("Saque efetuado com sucesso, saldo atual: R${}".format(saldo))
    return saldo, valores_saques, qtde_saques
  
def criar_conta( usuarios, numero_conta, contagem_conta, AGENCIA):
    cpf = input("Digite seu cpf: ")
    usuario = filtar_usuario(cpf, usuarios)
    if usuario:
        contagem_conta+= 1
        numero_conta = numero_conta + "{}".format(contagem_conta)
        conta = {"cpf":cpf,"numero_conta":numero_conta,"agencia":AGENCIA}
        contas.append(conta)
        print("========================== CONTA CRIADA ==========================")

def listar_contas(contas):
    for conta in contas:
        print("Agencia: {} \n numero: {}\n Cpf do titular: {}".format(conta['agencia'], conta['numero_conta'], conta['cpf']))
        print("-----------------------------------------------------------------------------------------------")
        
numero_conta = "0"
AGENCIA = "001"
contagem_conta = 0                
saldo = 0
limite = 500
extrato = ""
valores_saques = []
valores_depositos = []
numero_saques = 0
LIMITE_SAQUES = 3
quantidade_deposito = 0
usuarios = []
contas = []

while True:
    opcao = input(menu())
    
    if opcao == "d":
        valor_deposito = float (input("Digite o valor que deseja depositar(OBS: somente valores positivos):  "))
        saldo, valores_depositos = deposito(saldo, valor_deposito, valores_depositos)
        
    elif opcao == "s":
        valor_saque = float(input("OBS: Só se pode realizar 3 saques diários e o valor máximo do saque é de R$500,00 \n Digite o valor do saque:"))
        saldo, valores_saques, numero_saques = saque(saldo=saldo,
                                      valor=valor_saque,
                                      valores_saques= valores_saques,
                                      limites_saques= LIMITE_SAQUES,
                                      qtde_saques= numero_saques)
    elif opcao == "e":
        print("Saldo: R%{:.2f} \n Depósitos: {} \n Saques: {}".format(saldo, valores_depositos, valores_saques))
        
    elif opcao == "nu":
        cadastrar_usuario(usuarios)
    elif opcao == "nc":
        criar_conta(usuarios, numero_conta, contagem_conta, AGENCIA)    
    
    elif opcao == "lc":
        listar_contas(contas)
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
    
    
    