"""
Arquivo de Estudo: Objetos de Primeira Classe em Python
Objetivo: Demonstrar que funções em Python são tratadas como objetos de primeira classe,
          podendo ser passadas como argumentos para outras funções, atribuídas a 
          variáveis e retornadas como resultados.
"""

# ==============================================================================
# Funções como Objetos de Primeira Classe
# ------------------------------------------------------------------------------
# No Python, funções são objetos. Isso significa que podemos:
#   1. Atribuí-las a variáveis.
#   2. Passá-las como argumento para outras funções.
#   3. Retorná-las a partir de outras funções.
# ==============================================================================

def somar(a, b):
    return a + b


def exibir_resultado(a, b, funcao):
    """
    Esta função recebe dois valores e uma OUTRA função como parâmetro.
    Ela executa a função recebida e exibe o resultado formatado.
    """
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")


# ==============================================================================
# Exemplo 1: Passando Função por Argumento
# ------------------------------------------------------------------------------
# Aqui passamos a função 'somar' (sem os parênteses, apenas o nome do objeto)
# para dentro da função 'exibir_resultado'.
# ==============================================================================
exibir_resultado(10, 10, somar)  # Saída: O resultado da operação 10 + 10 = 20


# ==============================================================================
# Exemplo 2: Atribuindo Função a uma Variável
# ------------------------------------------------------------------------------
# Podemos criar um apelido para uma função simplesmente atribuindo-a a uma variável.
# ==============================================================================
op = somar
print(op(1, 23))  # Saída: 24