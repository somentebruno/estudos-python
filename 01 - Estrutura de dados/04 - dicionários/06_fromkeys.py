"""
Arquivo de Estudo: Método .fromkeys() em Dicionários
Objetivo: Demonstrar como criar um novo dicionário a partir de uma lista de chaves,
          atribuindo um valor padrão a todas elas.
"""

# ==============================================================================
# Exemplo 1: Criando Dicionário com Valores Padrão (None)
# ------------------------------------------------------------------------------
# O método estático dict.fromkeys(chaves) cria um dicionário onde cada item 
# da coleção 'chaves' se torna uma chave no novo dicionário. Por padrão, 
# se o segundo argumento for omitido, todos os valores serão inicializados 
# como None.
# ==============================================================================
resultado = dict.fromkeys(["nome", "telefone"])  # {"nome": None, "telefone": None}
print(resultado)

# ==============================================================================
# Exemplo 2: Criando Dicionário com Valor Padrão Personalizado
# ------------------------------------------------------------------------------
# Podemos passar um segundo argumento para o .fromkeys() que será o valor 
# atribuído a TODAS as chaves informadas. Isso é muito útil para inicializar 
# configurações padrão ou estados iniciais de um sistema.
# ==============================================================================
resultado = dict.fromkeys(["nome", "telefone"], "vazio")  # {"nome": "vazio", "telefone": "vazio"}
print(resultado)