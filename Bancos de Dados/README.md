# 🗄️ Bancos de Dados Relacionais e NoSQL

Este repositório faz parte da trilha de estudos de **Engenharia de Dados**, abrigando projetos de implementação, manipulação e evolução de bancos de dados **Relacionais (SQL)** e **Não Relacionais (NoSQL)**.

## 📂 Estrutura do Diretório

O conteúdo está organizado em frentes tecnológicas distintas para facilitar a navegação e a documentação de portfólio.

---

### 🗃️ [01. Relacionais e SQL](./01-Relacionais-e-SQL/)

Focado na construção, normalização e extração de dados utilizando linguagens **SQL** (compatível com MySQL/MariaDB). Abrange modelagem, estruturação e técnicas de **Data Wrangling**.

**Trilha de Execução (Scripts):**

1. **[Setup e Inicialização](./01-Relacionais-e-SQL/01-setup-travel-schema.sql)**: Criação das tabelas base e inserção inicial (Seeds).
2. **[Consultas e Filtragem](./01-Relacionais-e-SQL/02-consultas-e-filtros.sql)**: DQL básico com filtros, operadores lógicos e uso do `LIKE`.
3. **[Manutenção e Escopo](./01-Relacionais-e-SQL/03-manutencao-e-escopo.sql)**: Boas práticas na alteração de dados legados (`UPDATE` e `DELETE`).
4. **[Refatoração e Evolução](./01-Relacionais-e-SQL/04-refatoracao-e-evolucao.sql)**: Evolução do schema e simulação de *Blue-Green Deployment*.
5. **[Constraints e Integridade](./01-Relacionais-e-SQL/05-constraints-e-integridade.sql)**: Chaves primárias (PK), chaves estrangeiras (FK) e manutenções em `CASCADE`.
6. **[Normalização e Parsing](./01-Relacionais-e-SQL/06-normalizacao-e-parsing.sql)**: Desmembramento de colunas não atômicas via funções de strings avançadas (`SUBSTRING_INDEX`).
7. **[Joins e Subconsultas](./01-Relacionais-e-SQL/07-joins-e-subconsultas.sql)**: Junções relacionais (`INNER`, `LEFT`, `RIGHT JOIN`) e resolução via subqueries complexas e correlacionadas.
8. **[Agregação e Ordenação](./01-Relacionais-e-SQL/08-agregacao-e-ordenacao.sql)**: Emprego de métricas e funções matemáticas (`COUNT`, `AVG`, `SUM`, `MIN`, `MAX`), agrupamentos (`GROUP BY`), paginação de retornos (`LIMIT / OFFSET`) e organização de dados (`ORDER BY`).

---

### 🍃 [02. Bancos de Dados NoSQL](./02-NoSQL/)

*(Em Construção)* 
Módulo destinado à exploração de bancos de dados que fogem do paradigma tabular convencional (como orientados a documentos, chave-valor), com destaque conceitual para sua alta escalabilidade horizontal e esquemas flexíveis.

---

## 🚀 Como Executar

**Ambiente SQL (Módulo 01)**:
1. Certifique-se de ter um SGBD SQL ativo (Ex: MySQL Workbench, DBeaver ou terminal CLI).
2. Execute os scripts sequencialmente da pasta `01-Relacionais-e-SQL` (nº 01 ao nº 08).
3. Acompanhe os comentários pedagógicos fixados em cada roteiro para fixação dos aprendizados.

---

## 📑 Boas Práticas Mapeadas no Portfólio
- **Nomenclatura Semântica**: Diretrizes rígidas com nomes de tabelas em caixa baixa e sublinhados descritivos.
- **Integridade Sistêmica**: Implantação de chaves visando a eliminação de dados zumbis ou orfãos em bancos legados.
- **Micro-Documentação e Clean Code**: Código comentado do princípio ao fim não apenas com "o que faz", mas focando no "por que foi feito assim".

---
*Este repositório serve como prova de conceito de estudos sólidos e de fácil consulta de sintaxe e comandos essenciais para DataOps/DataEng.*
