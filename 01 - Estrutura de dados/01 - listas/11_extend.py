"""
Arquivo de Estudo: Método Extend (.extend) em Listas
Objetivo: Demonstrar como adicionar múltiplos elementos a uma lista, 
          mesclando duas estruturas sem criar sublistas.
"""

# ==============================================================================
# Exemplo: Adicionando múltiplos itens com .extend()
# ------------------------------------------------------------------------------
# Diferente do '.append()' - que adiciona um único item ou cria uma sublista 
# caso você tente adicionar um array -, o método '.extend()' extrai os elementos 
# do iterável (no caso, de outra lista) e os insere individualmente no final
# da lista atual.
#
# Isso é muito útil para concatenar/juntar listas diferentes de forma simples
# e eficiente.
# ==============================================================================

linguagens = ["python", "js", "c"]

print("Lista original:")
print(linguagens)  # ["python", "js", "c"]

# Adicionamos uma nova lista inteira e seus itens são mesclados 
# no primeiro nível da lista original.
linguagens.extend(["java", "csharp"])

print("\nLista apos o extend:")
print(linguagens)  # ["python", "js", "c", "java", "csharp"]