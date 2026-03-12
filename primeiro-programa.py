print(1 + 10) # int

print(1.5 + 10.5) # float

print(True) #bool - bolleano

print("Olá, mundo!") # str

# no modo de execução:
# dir() # mostra as funções e variáveis disponíveis no ambiente de execução
# dir(100) # mostra as funções e variáveis disponíveis para o tipo int

# help() # mostra a documentação das funções e variáveis disponíveis no ambiente de execução
# help(print) # mostra a documentação da função print

#As variaveis nn precisam de tipo definido 

nome = "Guilherme"
idade = 20;

#eu tambem posso definir tudo em uma linha
nome, idade = "Isadora", 27

print(nome, idade)

#é mais comum no python usar o nome da variável entre _ underline ( Snake Case ), do que usar tipo limiteSaqueDiario 
limite_saque_diario = 1000

# Para escrever variáveis constantes, utilizamos letras MAIUSCULAS e separação por underline
BRAZILIAN_STATES = ["SP", "RJ", "MG", "ES"]

print(BRAZILIAN_STATES)

#CONVERSÃO DE TIPOS

print(int(3.0)) 
print(int(1.5)) # converte float para int, arredondando para baixo

print(int("10")) # converte string para int
print(float("10.10")) # converte string para float

print(str(10.50)) # converte float para string

valor = 10
valor_str = str(valor)
print(type(valor)) # mostra o tipo da variável, nesse caso int
print(type(valor_str)) # mostra o tipo da variável, nesse caso str

print(100 / 2) # divisão normal, resultado é float
print(100 // 2) # divisão inteira, resultado é int, pois o // arredonda para baixo

preco = 28
print(str(preco) + " reais") # concatenação de string, converte o int para str e junta com a string " reais"
texto = f"preco é {preco}, vai comprar?" # f-string, permite inserir variáveis dentro da string usando {}
print(texto)

nome2 = input("Informe o seu nome: ") # função para ler uma entrada
idade = input(f"Informe a sua idade {nome2}:") 

print(f"Olá, {nome2}!") # função para imprimir uma mensagem com o nome informado

print(nome2, idade, end="... \n") # end="... \n" para adiciona "..." no final antes de pular a linha

print(nome2, idade, sep="#") # sep="#" para separar os valores com "#"