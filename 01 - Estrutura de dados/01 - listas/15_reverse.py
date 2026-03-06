"""
Arquivo de Estudo: Método Reverse (.reverse) em Listas
Objetivo: Demonstrar como inverter a ordem dos elementos de uma lista 
          permanentemente.
"""

# ==============================================================================
# Exemplo: Invertendo a lista com .reverse()
# ------------------------------------------------------------------------------
# O método '.reverse()' espelha a ordem da lista atual. 
#
# Comportamento Inplace:
# Diferente de técnicas de fatiamento como list[::-1], que criam uma nova lista,
# o '.reverse()' modifica o objeto original diretamente na memória (inplace),
# o que o torna mais eficiente em termos de recursos quando não se precisa
# manter a ordem original.
# ==============================================================================

linguagens = ["python", "js", "c", "java", "csharp"]

print("Lista original:")
print(linguagens)

# Invertendo a ordem de todos os elementos permanentemente
linguagens.reverse()

print("\nLista apos o reverse:")
print(linguagens)  # ["csharp", "java", "c", "js", "python"]