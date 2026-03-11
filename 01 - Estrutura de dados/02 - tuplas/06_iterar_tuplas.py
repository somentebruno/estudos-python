"""
Arquivo de Estudo: Iteração de Tuplas
Objetivo: Demonstrar as diferentes formas de percorrer os elementos de uma tupla,
          tanto acessando os valores diretamente quanto obtendo seus índices.
"""

# ==============================================================================
# Exemplo 1: Iteração Simples com 'for'
# ------------------------------------------------------------------------------
# A forma mais direta de percorrer uma tupla é usando o laço 'for'.
# A cada iteração, a variável de controle (aqui: 'carro') recebe automaticamente
# o valor do próximo elemento, sem necessidade de controlar o índice manualmente.
# ==============================================================================
carros = (
    "gol",
    "celta",
    "palio",
)

for carro in carros:
    print(carro)


# ==============================================================================
# Exemplo 2: Iteração com Índice usando enumerate()
# ------------------------------------------------------------------------------
# Quando precisamos do índice (posição) de cada elemento durante a iteração,
# usamos a função built-in enumerate(). Ela retorna pares (índice, valor) a cada 
# iteração, dispensando o uso manual de contadores como 'i = 0; i += 1'.
# É a forma pythônica e mais legível de iterar com índice.
# ==============================================================================
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")