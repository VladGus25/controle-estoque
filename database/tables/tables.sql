-- =========================================
-- TABELA: CATEGORIA
-- =========================================

CREATE TABLE categoria (
    id_categoria SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);


-- =========================================
-- TABELA: PRODUTO
-- =========================================

CREATE TABLE produto (
    id_produto SERIAL PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    preco NUMERIC(10,2) NOT NULL,
    quantidade INTEGER NOT NULL DEFAULT 0,
    id_categoria INTEGER NOT NULL,

    CONSTRAINT fk_produto_categoria
        FOREIGN KEY (id_categoria)
        REFERENCES categoria(id_categoria)
);


-- =========================================
-- TABELA: MOVIMENTAÇÃO DE ESTOQUE
-- =========================================

CREATE TABLE movimentacao_estoque (
    id_movimentacao SERIAL PRIMARY KEY,
    id_produto INTEGER NOT NULL,
    tipo VARCHAR(10) NOT NULL,
    quantidade INTEGER NOT NULL,
    data_movimentacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_movimentacao_produto
        FOREIGN KEY (id_produto)
        REFERENCES produto(id_produto),

    CONSTRAINT chk_tipo_movimentacao
        CHECK (tipo IN ('ENTRADA', 'SAIDA'))
);
