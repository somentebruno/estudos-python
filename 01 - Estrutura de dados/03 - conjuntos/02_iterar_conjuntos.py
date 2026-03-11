"""
Arquivo de Estudo: Iteração de Conjuntos (Sets)
Objetivo: Demonstrar as diferentes formas de percorrer os elementos de um
          conjunto, tanto de forma simples quanto obtendo o índice de contagem.
"""

# ==============================================================================
# Exemplo 1: Iteração Simples com 'for'
# ------------------------------------------------------------------------------
# Apesar de conjuntos não serem indexados, ainda é possível iterá-los
# diretamente com o laço 'for'. A cada ciclo, a variável de controle
# recebe o próximo elemento disponível.
#
# Atenção: a ordem de iteração NÃO é garantida e pode variar entre execuções,
# pois conjuntos não mantêm uma sequência interna definida.
# ==============================================================================
carros = {"gol", "celta", "palio"}

for carro in carros:
    print(carro)

# ==============================================================================
# Exemplo 2: Iteração com Índice usando enumerate()
# ------------------------------------------------------------------------------
# A função enumerate() pode ser usada em qualquer iterável, incluindo sets.
# Ela gera um contador automático (índice) para cada elemento percorrido.
# Vale reforçar: esse índice representa apenas a ordem de iteração daquela
# execução específica, e não uma posição fixa do elemento no conjunto.
# ==============================================================================
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")