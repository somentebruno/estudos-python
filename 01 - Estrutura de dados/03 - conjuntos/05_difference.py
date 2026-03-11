"""
Arquivo de Estudo: Método .difference() em Conjuntos
Objetivo: Demonstrar como identificar os elementos exclusivos de um conjunto,
          ou seja, os que existem em um mas não estão presentes no outro.
"""

# ==============================================================================
# Exemplo 1: Diferença entre Conjuntos com .difference()
# ------------------------------------------------------------------------------
# O método .difference() retorna um NOVO conjunto com os elementos que existem
# no conjunto chamador, mas que NÃO estão presentes no conjunto passado
# como argumento. É como uma subtração: A - B (o que A tem que B não tem).
#
# Características importantes:
#   - A ordem importa: A.difference(B) ≠ B.difference(A) (não é comutativo).
#   - Não modifica os conjuntos originais (operação não destrutiva).
#   - Equivalente ao operador - (subtração): conjunto_a - conjunto_b.
#   - Útil para encontrar dados exclusivos de uma coleção, comparar listas
#     de clientes, permissões, produtos, etc.
# ==============================================================================
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

# Elementos que existem em A mas NÃO existem em B → apenas o 1
resultado = conjunto_a.difference(conjunto_b)
print(resultado)  # {1}

# Elementos que existem em B mas NÃO existem em A → apenas o 4
resultado = conjunto_b.difference(conjunto_a)
print(resultado)  # {4}