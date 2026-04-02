saldo = 2000
saque = 2500

#Tudo que ta no começo vai ser retornado se for verdadeiro, e se for falso, o que ta no final
status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")