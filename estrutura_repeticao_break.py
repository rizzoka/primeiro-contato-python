while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break #o break é utilizado para sair do laço de repetição, mesmo que a condição de parada não tenha sido atingida

    print(numero)

for numero in range(100):
    if numero == 10:
        break

    print(numero)

for numero in range(20):
    if numero == 12:
        continue #o continue é utilizado para pular a iteração atual do laço de repetição, ou seja, ele não executa o código abaixo do continue e passa para a próxima iteração -> 12 some

    print(numero, end=" ")