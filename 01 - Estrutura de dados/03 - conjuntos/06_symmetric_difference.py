"""
Arquivo de Estudo: Método .symmetric_difference() em Conjuntos
Objetivo: Demonstrar como encontrar os elementos que são exclusivos de cada
          conjunto, ou seja, tudo que NÃO é compartilhado entre os dois.
"""

# ==============================================================================
# Exemplo 1: Diferença Simétrica com .symmetric_difference()
# ------------------------------------------------------------------------------
# O método .symmetric_difference() retorna um NOVO conjunto com os elementos
# que estão em UM OU OUTRO conjunto, mas NÃO em ambos simultaneamente.
# É o inverso da interseção: exclui o que os conjuntos têm em comum e
# mantém apenas o que é exclusivo de cada um.
#
# Resumindo visualmente:
#   A = {1, 2, 3}  |  B = {2, 3, 4}
#   Comuns (interseção): {2, 3}  → são descartados
#   Resultado: {1, 4}  → apenas os exclusivos de cada lado
#
# Características importantes:
#   - É comutativo: A.symmetric_difference(B) == B.symmetric_difference(A).
#   - Não modifica os conjuntos originais (operação não destrutiva).
#   - Equivalente ao operador ^ (XOR): conjunto_a ^ conjunto_b.
# ==============================================================================
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

# Retorna apenas os elementos exclusivos de A e de B (exclui os comuns: 2 e 3)
resultado = conjunto_a.symmetric_difference(conjunto_b)
print(resultado)  # {1, 4}