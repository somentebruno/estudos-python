"""
Arquivo de Estudo: Método .union() em Conjuntos
Objetivo: Demonstrar como combinar dois ou mais conjuntos em um único,
          unindo todos os seus elementos sem duplicatas.
"""

# ==============================================================================
# Exemplo 1: Unindo Conjuntos com .union()
# ------------------------------------------------------------------------------
# O método .union() retorna um NOVO conjunto contendo todos os elementos
# presentes em ambos os conjuntos combinados. Duplicatas são automaticamente
# eliminadas, pois a regra de unicidade dos sets é sempre preservada.
#
# Características importantes:
#   - Não modifica os conjuntos originais (operação não destrutiva).
#   - Equivalente ao operador | (pipe): conjunto_a | conjunto_b.
#   - Pode receber múltiplos conjuntos como argumento:
#     Ex: conjunto_a.union(conjunto_b, conjunto_c)
# ==============================================================================
conjunto_a = {1, 2}
conjunto_b = {3, 4}

# Retorna um novo conjunto com todos os elementos de A e B unidos
resultado = conjunto_a.union(conjunto_b)
print(resultado)  # {1, 2, 3, 4}