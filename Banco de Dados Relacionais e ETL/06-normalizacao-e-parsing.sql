/*
  PROJETO: Sistema de Gestão de Reservas de Viagens
  DESCRIÇÃO: Normalização da estrutura de endereços e parsing de strings.
  TÉCNICAS: Data Wrangling, Manipulação de Strings (SUBSTRING_INDEX) e Refatoração de Schema.
*/

-- =============================================================================
-- 1. EVOLUÇÃO DO ESQUEMA (DQL)
-- =============================================================================

-- Desmembramento do campo único 'endereco' em colunas atômicas.
-- Esta prática melhora a indexação e permite análises regionais (por cidade/estado).
ALTER TABLE usuarios
    ADD COLUMN rua    VARCHAR(100),
    ADD COLUMN numero VARCHAR(10),
    ADD COLUMN cidade VARCHAR(50),
    ADD COLUMN estado VARCHAR(50);

-- =============================================================================
-- 2. DATA WRANGLING: PARSING E MIGRAÇÃO
-- =============================================================================

-- Extração de informações da string composta original utilizando delimitadores.
-- A lógica utiliza SUBSTRING_INDEX para isolar cada componente entre as vírgulas.
UPDATE usuarios
SET 
    rua    = TRIM(SUBSTRING_INDEX(SUBSTRING_INDEX(endereco, ',', 1), ',', -1)),
    numero = TRIM(SUBSTRING_INDEX(SUBSTRING_INDEX(endereco, ',', 2), ',', -1)),
    cidade = TRIM(SUBSTRING_INDEX(SUBSTRING_INDEX(endereco, ',', 3), ',', -1)),
    estado = TRIM(SUBSTRING_INDEX(endereco, ',', -1));

-- =============================================================================
-- 3. FINALIZAÇÃO E LIMPEZA
-- =============================================================================

-- Remoção da coluna redundante após a validação da migração dos dados.
ALTER TABLE usuarios
    DROP COLUMN endereco;