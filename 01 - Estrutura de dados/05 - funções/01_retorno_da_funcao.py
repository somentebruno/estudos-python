"""
Arquivo de Estudo: Retorno de Funções em Python
Objetivo: Demonstrar como retornar valores simples e valores múltiplos (tuplas).
"""

# ==============================================================================
# Retorno Simples
# ------------------------------------------------------------------------------
# A palavra reservada 'return' finaliza a execução da função e envia o 
# resultado de volta para quem a chamou.
# ==============================================================================
def calcular_total(numeros):
    return sum(numeros)


# ==============================================================================
# Retorno Múltiplo
# ------------------------------------------------------------------------------
# Em Python, se uma função retorna mais de um valor separado por vírgula, 
# ela automaticamente os empacota em uma Tupla.
# ==============================================================================
def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor


# --- Execução e Testes ---
print(calcular_total([10, 20, 34]))          # Saída: 64
print(retorna_antecessor_e_sucessor(10))     # Saída: (9, 11) -> Uma Tupla