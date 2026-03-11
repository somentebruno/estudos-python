"""
Arquivo de Estudo: Método .pop() em Conjuntos
Objetivo: Demonstrar como remover e retornar um elemento arbitrário de um
          conjunto, já que sets não possuem índices ou ordem definida.
"""

# ==============================================================================
# Exemplo 1: Removendo Elementos Arbitrários com .pop()
# ------------------------------------------------------------------------------
# O método .pop() remove e RETORNA um elemento do conjunto.
# Como conjuntos não são ordenados, não é possível controlar QUAL elemento
# será removido — a escolha é interna ao Python e pode variar entre execuções.
#
# Características importantes:
#   - Modifica o conjunto original diretamente (operação in-place).
#   - Ao contrário do .pop() em listas, NÃO aceita índice como argumento.
#   - Lança KeyError se chamado em um conjunto vazio.
#   - O valor retornado pode ser armazenado em uma variável para uso posterior:
#     Ex: elemento = numeros.pop()
#   - Útil quando precisamos processar e consumir os elementos de um conjunto
#     sem nos preocupar com a ordem de remoção.
# ==============================================================================
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

# Exibe o conjunto após eliminação automática de duplicatas
print(numeros)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# Remove e retorna um elemento arbitrário (ordem não garantida)
print(numeros.pop())
print(numeros.pop())

# Exibe o conjunto com dois elementos a menos
print(numeros)