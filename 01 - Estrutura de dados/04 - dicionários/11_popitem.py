"""
Arquivo de Estudo: Método .popitem() em Dicionários
Objetivo: Demonstrar como remover e retornar o último par chave-valor inserido 
          no dicionário.
"""

# ==============================================================================
# Exemplo 1: Removendo o Último Item com .popitem()
# ------------------------------------------------------------------------------
# Diferente do .pop(), que exige uma chave específica, o .popitem() remove e 
# retorna o último par (chave, valor) inserido no dicionário (ordem LIFO - Last 
# In, First Out). 
#
# Retorno: Uma tupla contendo a chave e o valor do item removido.
#
# Características importantes:
#   - Modifica o dicionário original diretamente.
#   - Útil para processar dicionários como se fossem pilhas de dados.
#   - Se o dicionário estiver vazio, o método lança um KeyError.
# ==============================================================================
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# Remove o último item inserido e retorna como uma tupla (chave, valor)
resultado = contatos.popitem()  
print(resultado)  # ('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})

# Tentar chamar popitem() em um dicionário vazio gera erro
# contatos.popitem()  # KeyError