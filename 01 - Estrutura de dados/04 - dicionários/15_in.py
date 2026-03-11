"""
Arquivo de Estudo: Operador 'in' em Dicionários
Objetivo: Demonstrar como verificar a existência de uma chave dentro de um 
          dicionário ou de dicionários aninhados.
"""

# ==============================================================================
# Sobre o Operador 'in'
# ------------------------------------------------------------------------------
# No contexto de dicionários, o operador 'in' verifica se uma CHAVE existe 
# na coleção. Ele NÃO verifica os valores.
#
# Performance: Assim como nos conjuntos (sets), a busca com 'in' em dicionários 
# é O(1), sendo extremamente rápida pois utiliza a tabela hash interna.
# ==============================================================================
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

# Verificando se uma chave existe no dicionário principal
resultado = "guilherme@gmail.com" in contatos  # True
print(resultado)

resultado = "megui@gmail.com" in contatos  # False
print(resultado)

# ==============================================================================
# Verificação em Dicionários Aninhados
# ------------------------------------------------------------------------------
# Podemos usar o operador 'in' para verificar a existência de chaves dentro 
# de sub-dicionários, acessando-os primeiro pela chave pai.
# ==============================================================================
resultado = "idade" in contatos["guilherme@gmail.com"]  # False
print(resultado)

resultado = "telefone" in contatos["giovanna@gmail.com"]  # True
print(resultado)