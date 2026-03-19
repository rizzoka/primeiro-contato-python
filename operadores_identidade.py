#Compara se objetos ocupam o mesmo espaço na memória
curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

print(curso is nome_curso) # True, porque ambos apontam para o mesmo objeto na memória.

print(curso is not nome_curso) # False, porque ambos apontam para o mesmo objeto na memória.

print(saldo is limite) # True, porque ambos são inteiros com o mesmo valor e, em Python, pequenos inteiros são internados (interned), ou seja, eles compartilham o mesmo objeto na memória para otimizar o uso de memória. Portanto, saldo e limite apontam para o mesmo objeto inteiro 200 na memória.