"""
Arquivo de Estudo: Método .copy() em Dicionários
Objetivo: Demonstrar como criar uma cópia independente (shallow copy) de um
          dicionário, evitando que alterações em um afete o outro.
"""

# ==============================================================================
# Exemplo 1: Copiando um Dicionário com .copy()
# ------------------------------------------------------------------------------
# o método .copy() cria uma cópia rasa do dicionário. Isso significa que, 
# se alterarmos o valor de uma chave no dicionário original (reatribuindo um 
# novo objeto), a cópia não sentirá a mudança, pois ela aponta para um objeto 
# novo e independente no nível superior.
#
# Atenção: Se os valores do dicionário forem objetos mutáveis (como listas ou 
# outros dicionários), o .copy() copia apenas as referências (shallow copy). 
# Para cópias totalmente independentes em todos os níveis, deve-se usar copy.deepcopy().
# ==============================================================================
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# Cria um novo objeto dicionário com os mesmos dados
copia = contatos.copy()

# Altera a chave no dicionário de cópia (reatribuição completa do valor)
copia["guilherme@gmail.com"] = {"nome": "Gui"}

# O dicionário original permanece inalterado
print(contatos["guilherme@gmail.com"])  # {"nome": "Guilherme", "telefone": "3333-2221"}

# O dicionário de cópia reflete a mudança feita apenas nele
print(copia["guilherme@gmail.com"])      # {"nome": "Gui"}