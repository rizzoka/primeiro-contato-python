#em Python, a indentação é fundamental para definir blocos de código. O código dentro de uma função, loop ou estrutura condicional deve ser indentado corretamente para que o interpretador entenda quais linhas pertencem a qual bloco.

def sacar(valor):
    saldo = 500
    #é de 4 espaços ou um tab, mas o mais comum é usar 4 espaços para cada nível de indentação
    if saldo >= valor:
        print("Saque realizado com sucesso!")
        print("Retire o seu dinhero na boca do caixa.")

    print("Obrigado por usar nosso serviço!")

# def depositar(valor):
# saldo = 500
# saldo +=valor
# erro: sem identação

sacar(700)