"""
Arquivo de Estudo: Operador 'in' em Conjuntos
Objetivo: Demonstrar como verificar a existência de um elemento em um conjunto
          utilizando o operador de pertencimento 'in'.
"""

# ==============================================================================
# Exemplo 1: Verificando Pertencimento com o Operador 'in'
# ------------------------------------------------------------------------------
# O operador 'in' verifica se um elemento está presente em uma coleção,
# retornando True ou False (booleano).
#
# Em conjuntos, o operador 'in' tem uma performance superior em relação
# a listas e tuplas:
#   - Listas/Tuplas: verificação O(n) — percorre toda a coleção em pior caso.
#   - Sets/Dicionários: verificação O(1) — usa tabela hash internamente,
#     tornando a busca praticamente instantânea independente do tamanho.
#
# Por isso, quando a necessidade principal é verificar existência de elementos
# repetidamente, conjuntos são a estrutura ideal para essa operação.
# Também existe o operador 'not in' para verificar ausência de um elemento.
# ==============================================================================
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

# 1 pertence ao conjunto → True
print(1 in numeros)   # True

# 10 não pertence ao conjunto → False
print(10 in numeros)  # False