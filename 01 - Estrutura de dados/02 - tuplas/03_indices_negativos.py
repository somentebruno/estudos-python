"""
Arquivo de Estudo: Acesso a Tuplas com Índices Negativos
Objetivo: Demonstrar como acessar elementos de uma tupla de trás para frente
          utilizando a contagem de índices negativos.
"""

# ==============================================================================
# Exemplo 1: Acessando Elementos por Índice Negativo
# ------------------------------------------------------------------------------
# O Python suporta indexação negativa nativamente nas suas estruturas de dados.
# Isso permite acessar os elementos no sentido reverso, começando do final 
# da tupla. 
# O índice -1 SEMPRE representa o último elemento, o -2 o penúltimo, etc. 
# É uma forma pythônica (mecanismo inteligente) para ler e extrair os últimos 
# dados registrados de maneira rápida e sem precisar descobrir o tamanho
# da tupla (utilizando 'len()').
# ==============================================================================
frutas = (
    "maçã",
    "laranja",
    "uva",
    "pera",
)

# Acessa o último elemento da tupla (posição 1 de trás pra frente)
print(frutas[-1])  # pera

# Acessa o antepenúltimo elemento (posição 3 de trás pra frente)
print(frutas[-3])  # laranja