/*
  Project: Travel Management System
  Description: Database schema and initial data seeding.
*/

-- Schema Creation
CREATE TABLE IF NOT EXISTS usuarios (
    id              INT PRIMARY KEY,
    nome            VARCHAR(255) NOT NULL,
    email           VARCHAR(255) NOT NULL UNIQUE,
    data_nascimento DATE NOT NULL,
    endereco        VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS destinos (
    id              INT PRIMARY KEY,
    nome            VARCHAR(255) NOT NULL UNIQUE,
    descricao       VARCHAR(500) NOT NULL
);

CREATE TABLE IF NOT EXISTS reservas (
    id              INT PRIMARY KEY,
    id_usuario      INT NOT NULL,
    id_destino      INT NOT NULL,
    data            DATE NOT NULL,
    status          VARCHAR(50) DEFAULT 'pendente',
    
    CONSTRAINT fk_reserva_usuario FOREIGN KEY (id_usuario) REFERENCES usuarios(id),
    CONSTRAINT fk_reserva_destino FOREIGN KEY (id_destino) REFERENCES destinos(id)
);

-- Data Seeding
INSERT INTO usuarios (id, nome, email, data_nascimento, endereco) 
VALUES 
    (1, 'João Silva', 'joao@example.com', '1990-05-15', 'Rua A, 123, Cidade X, Estado Y'),
    (2, 'Maria Santos', 'maria@example.com', '1985-08-22', 'Rua B, 456, Cidade Y, Estado Z'),
    (3, 'Pedro Souza', 'pedro@example.com', '1998-02-10', 'Avenida C, 789, Cidade X, Estado Y');

INSERT INTO destinos (id, nome, descricao) 
VALUES 
    (1, 'Praia das Tartarugas', 'Uma bela praia com areias brancas e mar cristalino'),
    (2, 'Cachoeira do Vale Verde', 'Uma cachoeira exuberante cercada por natureza'),
    (3, 'Cidade Histórica de Pedra Alta', 'Uma cidade rica em história e arquitetura');

INSERT INTO reservas (id, id_usuario, id_destino, data, status) 
VALUES 
    (1, 1, 2, '2023-07-10', 'confirmada'),
    (2, 2, 1, '2023-08-05', 'pendente'),
    (3, 3, 3, '2023-09-20', 'cancelada');

-- Operations
SELECT nome, email 
FROM usuarios 
WHERE nome LIKE '%Silva%' 
  AND data_nascimento < '1990-01-01';

UPDATE usuarios 
SET endereco = 'Nova Rua, 123' 
WHERE email = 'joao@example.com';

DELETE FROM reservas 
WHERE status = 'cancelada';