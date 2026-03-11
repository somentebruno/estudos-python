"""
Arquivo de Estudo: Método .remove() em Conjuntos
Objetivo: Demonstrar como remover um elemento específico de um conjunto
          pelo seu valor, e entender o comportamento quando o elemento não existe.
"""

# ==============================================================================
# Exemplo 1: Removendo Elementos pelo Valor com .remove()
# ------------------------------------------------------------------------------
# O método .remove(elemento) remove o elemento especificado do conjunto.
# Diferente do .discard(), o .remove() é rigoroso: se o elemento NÃO existir
# no conjunto, ele lança uma exceção KeyError.
#
# Comparativo com outros métodos de remoção:
#   - .remove(x) → remove x; lança KeyError se x não existir.
#   - .discard(x) → remove x; ignora silenciosamente se x não existir.
#   - .pop()      → remove e retorna um elemento arbitrário.
#
# Características importantes:
#   - Modifica o conjunto original diretamente (operação in-place).
#   - Não retorna o elemento removido (retorna None).
#     Por isso, print(numeros.remove(0)) imprime "None", não o valor 0.
#   - Use .remove() quando tiver certeza que o elemento existe no conjunto.
# ==============================================================================
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)          # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# Remove o elemento 0 do conjunto (retorna None, não o valor removido)
print(numeros.remove(0))  # None

print(numeros)          # {1, 2, 3, 4, 5, 6, 7, 8, 9}