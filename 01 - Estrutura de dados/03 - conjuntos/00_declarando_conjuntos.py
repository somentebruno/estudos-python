"""
Arquivo de Estudo: Declaração de Conjuntos (Sets)
Objetivo: Demonstrar as diferentes formas de criar conjuntos em Python,
          destacando sua principal característica: a eliminação automática
          de elementos duplicados.
"""

# ==============================================================================
# Sobre Conjuntos (Sets)
# ------------------------------------------------------------------------------
# Conjuntos são coleções NÃO ordenadas e NÃO indexadas de elementos únicos.
# Isso significa que:
#   - Duplicatas são automaticamente ignoradas na criação e inserção.
#   - A ordem de exibição dos elementos pode variar a cada execução.
#   - Não é possível acessar elementos por índice (ex: conjunto[0] gera erro).
# São criados pelo construtor built-in set(), que aceita qualquer iterável.
# ==============================================================================

# ==============================================================================
# Exemplo 1: Convertendo Lista para Conjunto
# ------------------------------------------------------------------------------
# Ao passar uma lista com valores repetidos para set(), os duplicados
# são automaticamente removidos, retornando apenas valores únicos.
# ==============================================================================
numeros = set([1, 2, 3, 1, 3, 4])
print(numeros)  # {1, 2, 3, 4}

# ==============================================================================
# Exemplo 2: Convertendo String para Conjunto
# ------------------------------------------------------------------------------
# Ao passar uma string para set(), cada caractere se torna um elemento único.
# Caracteres repetidos são eliminados, e a ordem de saída não é garantida.
# ==============================================================================
letras = set("abacaxi")
print(letras)  # {"b", "a", "c", "x", "i"}

# ==============================================================================
# Exemplo 3: Convertendo Tupla para Conjunto
# ------------------------------------------------------------------------------
# Assim como com listas e strings, ao converter uma tupla para conjunto,
# os elementos duplicados são eliminados automaticamente.
# ==============================================================================
carros = set(("palio", "gol", "celta", "palio"))
print(carros)  # {"gol", "celta", "palio"}