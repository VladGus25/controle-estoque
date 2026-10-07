-- =========================================
-- FUNCTION: CALCULAR VALOR DO ESTOQUE
-- =========================================

CREATE OR REPLACE FUNCTION calcular_valor_estoque(
    p_id_produto INTEGER
)
RETURNS NUMERIC(12,2)
LANGUAGE plpgsql
AS $$
DECLARE
    v_total NUMERIC(12,2);
BEGIN

    SELECT preco * quantidade
    INTO v_total
    FROM produto
    WHERE id_produto = p_id_produto;

    IF v_total IS NULL THEN
        RAISE EXCEPTION 'Produto não encontrado.';
    END IF;

    RETURN v_total;

END;
$$;


-- =========================================
-- FUNCTION: EXECUTAR MOVIMENTAÇÃO DE ESTOQUE
-- =========================================

CREATE OR REPLACE FUNCTION executar_movimentacao_estoque(
    p_id_produto INTEGER,
    p_quantidade INTEGER,
    p_tipo VARCHAR
)
RETURNS TEXT
LANGUAGE plpgsql
AS $$
BEGIN

    CALL movimentar_estoque(
        p_id_produto,
        p_quantidade,
        p_tipo
    );

    RETURN 'Movimentação realizada com sucesso.';

END;
$$;