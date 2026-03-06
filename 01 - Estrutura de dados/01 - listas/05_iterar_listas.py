"""
Arquivo de Estudo: Iteração em Listas Python
Objetivo: Demonstrar diferentes abordagens para percorrer (iterar) os elementos de uma lista.
"""

# Inicialização de uma lista básica com strings para exemplificar a iteração.
carros = ["gol", "celta", "palio"]

# ==============================================================================
# Exemplo 1: Iteração direta (Comum)
# ------------------------------------------------------------------------------
# Utilizamos o laço de repetição 'for' para extrair cada elemento 
# sequencialmente até o final da lista em questão.
#
# Essa abordagem é mais "pytônica" (limpa e natural da linguagem), sendo 
# recomendada sempre que precisarmos apensar *acessar os valores*.
# ==============================================================================
print("Iteração Direta (Apenas valores):")
for carro in carros:
    print(carro)

print("\n" + "-" * 40 + "\n")  # Um separador visual simples para o console

# ==============================================================================
# Exemplo 2: Iteração com a função integrada 'enumerate'
# ------------------------------------------------------------------------------
# A função 'enumerate' é uma Built-in function incrivelmente útil. 
# Ela nos devolve tuplas contendo o valor e respectivo índice do elemento sendo 
# iterado em tempo de execução.
#
# Considerada uma ótima prática de programação (Best Practice) em Python, pois 
# evita a necessidade de criarmos variáveis contadoras manualmente apenas para 
# acompanhar a posição (ex: i = 0, i += 1) - algo muito comum em outras linguagens, 
# mas que não torna o código idealmente pythônico.
# ==============================================================================
print("Iteração com Enumerate (Índices e valores):")
for indice, carro in enumerate(carros):
    # Utilizamos f-string (interpolação moderna) para formatar a saída.
    print(f"[{indice}] Veículo: {carro}")