"""
Arquivo de Estudo: Método Copy (.copy) em Listas
Objetivo: Demonstrar a cópia rasa (shallow copy) de uma lista, evitando que 
          modificações na nova lista afetem a original.
"""

# ==============================================================================
# Exemplo: Copiando listas com .copy()
# ------------------------------------------------------------------------------
# Diferente de fazer `nova_lista = lista` (o que apenas copia a referência da 
# memória, interligando alteracoes entre ambas), o método '.copy()' cria um 
# *novo* objeto de lista com os mesmos itens da original.
# 
# Isso é conhecido como "Shallow Copy" (Cópia rasa).
# É essencial para proteger a base de dados original ao processá-la e alterá-la.
# ==============================================================================

lista = [1, "Python", [40, 30, 20]]

# O ideal é atribuir o resultado da cópia a uma nova variável para não
# perder a utilidade dessa função poderosa.
lista_copiada = lista.copy()

print(lista)         # [1, "Python", [40, 30, 20]]
print(lista_copiada) # [1, "Python", [40, 30, 20]]
print(id(lista) == id(lista_copiada)) # Retorna False, atestando estarem em blocos de memoria isolados