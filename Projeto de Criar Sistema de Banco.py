# Só pode depositar valores positivos. 
# Todos os depoistos devem ser armazenados em uma variavel e exibido
# na operação extrato.
# 3 saques diarios com limite maximo de R$500 reais.
# Caso naõ tenha saldo devera exibir uma mensagem que não existe sal-
#do na conta.
# Todos os saques devem ser armazenados em uma variavel e exibido no
# extrato.
# A operaçao deve listar todos os depositos e saques.
# No fim da lista exibido o saldo atual da conta.
# Os valors devem ser exibidos com R$ XXX.XX

menu = """

  [1] Depositar
  [2] Sacar
  [3] Extrato
  [0] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        print("Depósito")
        deposito = input ("Insira o valor aqui:R$ ")
        if float(deposito) >=0:
         print("Depósito efetuado com sucesso, seu saldo é:", saldo+float(deposito))
         saldo == saldo + float(deposito)
        else:
            print("ERRO, o valor não pode ser negativo.")    
        
    elif opcao == "2":
         print("Saque")
         saque = input ("Insira o valor do saque:R$ ")
         
        
    elif opcao == "3":
         print ("Extrato")
    
    elif opcao == "0":
         print("Obrigado por usar nosso sistema, volte sempre!")
         break
    
    else:
         print("Operação Inválida, por favor selecione novamente a operação desejada.")
