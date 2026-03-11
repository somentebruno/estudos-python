"""
Arquivo de Estudo: Dicionários Aninhados (Nested Dicts)
Objetivo: Demonstrar a estruturação de dados complexos através do aninhamento 
          de dicionários, permitindo criar estruturas de dados multidimensionais.
"""

# ==============================================================================
# Exemplo 1: Estruturando Dicionários Aninhados
# ------------------------------------------------------------------------------
# Dicionários podem conter qualquer tipo de objeto como valor, inclusive outros 
# dicionários. Esta é uma forma poderosa de agrupar informações relacionadas 
# sob uma única chave mestre (neste caso, o e-mail atua como Chave Primária).
# ==============================================================================
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

# ==============================================================================
# Exemplo 2: Acessando Dados em Profundidade
# ------------------------------------------------------------------------------
# Para acessar valores em dicionários aninhados, encadeamos os colchetes [].
# O primeiro nível seleciona o dicionário interno pela chave principal,
# e o segundo nível seleciona o atributo específico dentro desse dicionário.
# ==============================================================================
telefone = contatos["giovanna@gmail.com"]["telefone"]  # "3443-2121"
print(telefone)