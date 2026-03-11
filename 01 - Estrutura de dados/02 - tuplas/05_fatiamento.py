"""
Arquivo de Estudo: Fatiamento de Tuplas (Slicing)
Objetivo: Demonstrar como extrair subconjuntos de elementos de uma tupla
          utilizando a sintaxe de fatiamento [start:stop:step].
"""

# ==============================================================================
# Exemplo 1: Fatiamento com Sintaxe [start:stop:step]
# ------------------------------------------------------------------------------
# O fatiamento (slicing) permite extrair um intervalo de elementos de uma tupla
# sem a necessidade de loops. A sintaxe segue o padrão:
#   [start] => índice inicial (inclusivo). Se omitido, começa do zero.
#   [stop]  => índice final (exclusivo). Se omitido, vai até o final.
#   [step]  => salto entre os elementos. Se omitido, assume 1 (um a um).
#
# O resultado de um fatiamento é SEMPRE uma nova tupla, nunca um elemento único.
# Valores negativos no 'step' invertem a direção da leitura.
# ==============================================================================
tupla = ("p", "y", "t", "h", "o", "n",)

# Do índice 2 até o final (sem stop definido)
print(tupla[2:])   # ("t", "h", "o", "n")

# Do início até o índice 2 (exclusivo)
print(tupla[:2])   # ("p", "y")

# Do índice 1 até o índice 3 (exclusivo)
print(tupla[1:3])  # ("y", "t")

# Do índice 0 ao 3 (exclusivo), pulando de 2 em 2 (step=2)
print(tupla[0:3:2])  # ("p", "t")

# Sem start, stop e step definidos: retorna a tupla completa
print(tupla[::])   # ("p", "y", "t", "h", "o", "n")

# Step -1: inverte a ordem, percorrendo toda a tupla de trás pra frente
print(tupla[::-1]) # ("n", "o", "h", "t", "y", "p")