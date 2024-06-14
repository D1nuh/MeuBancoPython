menu = """

[d] depositos
[s] saques
[e] estratos
[q] sair

"""

saldo = 0
limite = 500
numero_saques = 0
valorSaqueTotal = 0
LIMITES_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao == "d":
        
        valorDeposito = float(input("Qual valor que deseja depositar? "))
        print(f"\nSucesso, você depositou R$ {valorDeposito}")
        saldo += valorDeposito
        
    elif opcao == "s":
            valorSaque = float(input(f"\n Seu saldo é {saldo} Qual valor deseja sacar? "))
            if valorSaque <= saldo and numero_saques < LIMITES_SAQUES and valorSaque + valorSaqueTotal < limite:
                        print(f"Sucesso, você sacou um total de {valorSaque} agora você tem um saldo de R$ {saldo - valorSaque} disponivel!, Saques disponiveis {LIMITES_SAQUES - (numero_saques+1)} ")
                        numero_saques += 1
                        saldo -= valorSaque
                        valorSaqueTotal += valorSaque
            elif valorSaque + valorSaqueTotal > limite:
                print(f"Limite indisponivel. Disponivel {limite - valorSaqueTotal}")
            elif valorSaque + valorSaqueTotal == limite:
                print(f" Sucesso, você sacou {valorSaque}! Limite atingido. Limite Dispontivel: 0")
                valorSaqueTotal += valorSaque
                saldo -= valorSaque
            else:
                print(f"\nOps, algo deu errado, verifique seu saldo ou seus saques diarios")
    elif opcao == "e":
        print(f"""
----------- Extrato --------------
saldo: {saldo}
limite de saque {limite}
Saques totais {valorSaqueTotal}
numero de saques disponivel: {LIMITES_SAQUES - (numero_saques + 1)}
---------------------------------------
""")
    
    elif opcao == "q":
        break
        
    else:
         print("Operação inválida, por favor selecione novamente a operação desejada.")
else:
    print("algo deu muito errado!")    
    