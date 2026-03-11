"""
Arquivo de Estudo: Método .clear() em Dicionários
Objetivo: Demonstrar como remover todos os itens de um dicionário de uma vez,
          esvaziando-o completamente.
"""

# ==============================================================================
# Exemplo 1: Esvaziando um Dicionário com .clear()
# ------------------------------------------------------------------------------
# O método .clear() remove todos os pares chave-valor do dicionário. 
# Diferente de deletar o objeto (del contatos), o .clear() esvazia a coleção 
# mas mantém a referência à variável na memória, permitindo que ela continue 
# sendo usada como um dicionário vazio.
# ==============================================================================
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

# Remove todos os itens (operação in-place)
contatos.clear()

print(contatos)  # {} — dicionário agora está vazio