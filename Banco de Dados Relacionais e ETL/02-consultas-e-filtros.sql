/*
  PROJETO: Sistema de Gestão de Reservas de Viagens
  DESCRIÇÃO: Consultas de extração (DQL), filtros avançados e operadores de busca.
  OBJETIVO: Documentar padrões de filtragem e recuperação de dados.
*/

-- =============================================================================
-- 1. CONSULTAS BÁSICAS E PROJEÇÃO
-- =============================================================================

-- Listagem completa de usuários (uso moderado em produção)
SELECT * FROM usuarios;

-- Projeção de colunas específicas para otimização de tráfego de rede
SELECT 
    nome, 
    email 
FROM usuarios;

-- =============================================================================
-- 2. FILTROS COM OPERADORES DE COMPARAÇÃO
-- =============================================================================

-- Busca exata por nome
SELECT * FROM usuarios 
WHERE nome = 'João Silva';

-- Filtragem por critério cronológico (Usuários nascidos antes da década de 90)
SELECT * FROM usuarios 
WHERE data_nascimento < '1990-01-01';

-- =============================================================================
-- 3. BUSCA POR PADRÕES (PATTERN MATCHING)
-- =============================================================================

-- Uso do operador LIKE com wildcard (%) para buscar sobrenomes
-- Busca por qualquer ocorrência de 'Silva' no campo nome
SELECT * FROM usuarios 
WHERE nome LIKE '%Silva%';

-- Uso de underscore (_) para busca de caracteres específicos em posições fixas
-- Ex: 'Joao', 'Joao', atendendo a variações de um único caractere
SELECT * FROM usuarios 
WHERE nome LIKE 'Jo_o%';