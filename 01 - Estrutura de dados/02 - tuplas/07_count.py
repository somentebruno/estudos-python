"""
Arquivo de Estudo: Método .count() em Tuplas
Objetivo: Demonstrar como contar a ocorrência de um elemento específico
          dentro de uma tupla utilizando o método .count().
"""

# ==============================================================================
# Exemplo 1: Contando Ocorrências com .count()
# ------------------------------------------------------------------------------
# O método .count(valor) percorre toda a tupla e retorna um inteiro indicando
# quantas vezes o 'valor' passado como argumento aparece na sequência.
#
# Características importantes:
#   - A busca é sensível a maiúsculas/minúsculas (case-sensitive).
#   - Se o valor não existir na tupla, retorna 0 (sem lançar erros).
#   - Funciona com qualquer tipo de dado: strings, inteiros, listas, etc.
#   - É uma operação de leitura: não altera a tupla original (imutabilidade).
# ==============================================================================
cores = (
    "vermelho",
    "azul",
    "verde",
    "azul",
)

# "vermelho" aparece apenas 1 vez
print(cores.count("vermelho"))  # 1

# "azul" aparece 2 vezes na tupla
print(cores.count("azul"))  # 2

# "verde" aparece apenas 1 vez
print(cores.count("verde"))  # 1