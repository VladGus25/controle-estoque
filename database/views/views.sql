-- =========================================
-- VIEW: RELATÓRIO DE ESTOQUE
-- =========================================

CREATE OR REPLACE VIEW vw_relatorio_estoque AS
SELECT
    p.id_produto,
    p.nome AS produto,
    c.nome AS categoria,
    p.preco,
    p.quantidade,
    (p.preco * p.quantidade::numeric) AS valor_em_estoque,

    CASE
        WHEN p.quantidade = 0 THEN 'SEM ESTOQUE'
        WHEN p.quantidade <= 5 THEN 'ESTOQUE BAIXO'
        ELSE 'ESTOQUE NORMAL'
    END AS situacao

FROM produto p
INNER JOIN categoria c
    ON p.id_categoria = c.id_categoria;