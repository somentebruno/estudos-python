"""
Arquivo de Estudo: Função len() em Tuplas
Objetivo: Demonstrar como obter o número total de elementos de uma tupla
          utilizando a função built-in len().
"""

# ==============================================================================
# Exemplo 1: Contando Elementos com len()
# ------------------------------------------------------------------------------
# A função built-in len() retorna um inteiro representando o número total
# de elementos presentes na tupla (seu comprimento/tamanho).
#
# Características importantes:
#   - len() conta apenas os elementos do nível externo (não é recursiva).
#     Ex: uma tupla aninhada conta como 1 elemento, independente do seu tamanho.
#   - É uma operação de leitura (O(1) em tuplas): extremamente eficiente, pois
#     o Python armazena o tamanho internamente e não precisa percorrer a coleção.
#   - Funciona com qualquer sequência: strings, listas, tuplas, dicionários, etc.
# ==============================================================================
linguagens = (
    "python",
    "js",
    "c",
    "java",
    "csharp",
)

# Retorna a quantidade total de elementos da tupla
print(len(linguagens))  # 5