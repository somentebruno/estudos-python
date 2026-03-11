"""
Arquivo de Estudo: Método .pop() em Dicionários
Objetivo: Demonstrar como remover um item específico de um dicionário e recuperar 
          o seu valor ao mesmo tempo.
"""

# ==============================================================================
# Exemplo 1: Removendo e Recuperando Valor com .pop()
# ------------------------------------------------------------------------------
# O método .pop(chave) remove o item associado à chave informada e RETORNA o seu 
# valor. Se a chave for encontrada, o dicionário é modificado e o valor é 
# extraído para ser utilizado (por exemplo, armazenado em uma variável).
# ==============================================================================
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# Remove a chave e retorna o dicionário interno associado a ela
resultado = contatos.pop("guilherme@gmail.com")  # {'nome': 'Guilherme', 'telefone': '3333-2221'}
print(resultado)

# ==============================================================================
# Exemplo 2: Remoção Segura com Valor Padrão
# ------------------------------------------------------------------------------
# Se tentarmos usar .pop() em uma chave inexistente sem um segundo argumento, 
# o Python lançará um KeyError. Para evitar isso, passamos um valor padrão de 
# fallback. Se a chave não existir, esse valor será retornado em vez do erro.
# ==============================================================================
resultado = contatos.pop("guilherme@gmail.com", {})  # Agora a chave não existe mais, retorna {}
print(resultado)