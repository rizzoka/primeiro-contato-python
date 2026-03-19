saldo = 100
saque = 200
limite = 100

saldo >= saque and saque <= limite # False

saldo >= saque or saque <= limite # True


contatos_emergencia = []

not 1000 > 1500 # True, porque o not inverte o resultado da comparação. 1000 não é maior que 1500, então a expressão original é False, e o not a torna True.

not contatos_emergencia # True, porque a lista de contatos de emergência está vazia, o que é considerado False em um contexto booleano. O not inverte isso para True.

not "saque 1500" # False, porque uma string não vazia é considerada True em um contexto booleano. 

not "" # True, porque uma string vazia é considerada False em um contexto booleano.

saldo = 1000
saque = 250
limite = 200
conta_especial = True

saldo >= saque and saque <= limite or conta_especial and saldo >= saque #True 

(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque) # True 