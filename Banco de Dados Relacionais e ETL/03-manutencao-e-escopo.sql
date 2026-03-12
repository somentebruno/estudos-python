/*
  PROJETO: Sistema de Gestão de Reservas de Viagens
  DESCRIÇÃO: Operações de atualização e exclusão de registros (DML).
  FOCO: Manutenção de integridade e manipulação de registros existentes.
*/

-- =============================================================================
-- 1. ATUALIZAÇÃO DE REGISTROS (UPDATE)
-- =============================================================================

-- Atualização de endereço utilizando o e-mail como chave única de busca.
-- A boa prática recomenda o uso de campos UNIQUE ou PK para garantir o escopo.
UPDATE usuarios 
SET endereco = 'Nova Rua, 123' 
WHERE email = 'joao@example.com';

-- =============================================================================
-- 2. EXCLUSÃO DE REGISTROS (DELETE)
-- =============================================================================

-- Purga de registros baseada no ciclo de vida da reserva.
-- Remoção de instâncias com status 'cancelada' para limpeza da base transacional.
DELETE FROM reservas 
WHERE status = 'cancelada';