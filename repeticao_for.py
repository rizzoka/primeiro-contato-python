texto = input("Informe um texto:")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()
    print("Executa no final do laço")

# o range é uma função que gera uma sequência de números, muito utilizada em laços de repetição
range(4)

#no range é obrigatorio ter um start e um stop, o step(passo) é opcional
for numero in range(0,11):
    print(numero, end=" ")

#a tabuada do 5 (start, stop, step)
for numero in range(0,51,5):
    print(numero, end=" ")