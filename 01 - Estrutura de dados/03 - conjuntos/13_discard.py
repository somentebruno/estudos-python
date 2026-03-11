"""
Arquivo de Estudo: Método .discard() em Conjuntos
Objetivo: Demonstrar como remover um elemento específico de um conjunto
          de forma segura, sem gerar erros quando o elemento não existe.
"""

# ==============================================================================
# Exemplo 1: Removendo Elementos com .discard()
# ------------------------------------------------------------------------------
# O método .discard(elemento) remove o elemento especificado do conjunto.
# Sua principal vantagem em relação ao .remove() é a segurança:
#   - .discard(): se o elemento NÃO existir, simplesmente ignora a operação.
#   - .remove(): se o elemento NÃO existir, lança um KeyError.
#
# Características importantes:
#   - Modifica o conjunto original diretamente (operação in-place).
#   - Não retorna nada (retorna None).
#   - É a forma preferida quando não temos certeza se o elemento existe.
#   - Para remover e obter o valor removido, use .pop() no lugar.
# ==============================================================================
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# Remove o elemento 1 do conjunto (ele existe → remoção realizada)
numeros.discard(1)

# Tenta remover o elemento 45 (não existe → nenhum erro, operação ignorada)
numeros.discard(45)

print(numeros)  # {0, 2, 3, 4, 5, 6, 7, 8, 9}