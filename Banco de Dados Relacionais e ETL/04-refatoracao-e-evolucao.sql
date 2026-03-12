/*
  PROJETO: Sistema de Gestão de Reservas de Viagens
  DESCRIÇÃO: Evolução do esquema de banco de dados e migração de dados.
  TÉCNICAS: Blue-Green Deployment de tabelas e Alteração Direta (ALTER TABLE).
*/

-- =============================================================================
-- ABORDAGEM 1: RECONSTRUÇÃO E MIGRAÇÃO (MAIS SEGURA PARA GRANDES MUDANÇAS)
-- =============================================================================

-- 1. Criação da nova estrutura com metadados e dimensionamento atualizado
CREATE TABLE usuarios_nova (
    id              INT PRIMARY KEY,
    nome            VARCHAR(255) NOT NULL,
    email           VARCHAR(255) NOT NULL UNIQUE,
    data_nascimento DATE NOT NULL,
    endereco        VARCHAR(100) NOT NULL
);

-- 2. Migração de dados: Transferência da tabela antiga para a nova estrutura
INSERT INTO usuarios_nova (id, nome, email, data_nascimento, endereco)
SELECT id, nome, email, data_nascimento, endereco 
FROM usuarios;

-- 3. Finalização: Remoção da tabela legada e renomeação da nova versão
DROP TABLE usuarios;
ALTER TABLE usuarios_nova RENAME TO usuarios;


-- =============================================================================
-- ABORDAGEM 2: ALTERAÇÃO DIRETA (MAIS RÁPIDA PARA MUDANÇAS SIMPLES)
-- =============================================================================

-- Redimensionamento da coluna de endereço para suportar logs mais extensos
-- Nota: MODIFY COLUMN é específico para dialetos como MySQL/MariaDB
ALTER TABLE usuarios 
MODIFY COLUMN endereco VARCHAR(100) NOT NULL;