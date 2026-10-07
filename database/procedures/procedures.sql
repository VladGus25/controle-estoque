-- =========================================
-- PROCEDURE: MOVIMENTAR ESTOQUE
-- =========================================

CREATE OR REPLACE PROCEDURE movimentar_estoque(
    p_id_produto INTEGER,
    p_quantidade INTEGER,
    p_tipo VARCHAR
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_estoque_atual INTEGER;
BEGIN

    -- Verifica se a quantidade informada é válida
    IF p_quantidade <= 0 THEN
        RAISE EXCEPTION
        'A quantidade deve ser maior que zero.';
    END IF;


    -- Busca o estoque atual do produto
    SELECT quantidade
    INTO v_estoque_atual
    FROM produto
    WHERE id_produto = p_id_produto;


    -- Verifica se o produto existe
    IF NOT FOUND THEN
        RAISE EXCEPTION
        'Produto não encontrado.';
    END IF;


    -- ENTRADA DE ESTOQUE
    IF UPPER(p_tipo) = 'ENTRADA' THEN

        UPDATE produto
        SET quantidade = quantidade + p_quantidade
        WHERE id_produto = p_id_produto;


    -- SAÍDA DE ESTOQUE
    ELSIF UPPER(p_tipo) = 'SAIDA' THEN

        -- Verifica se existe estoque suficiente
        IF v_estoque_atual < p_quantidade THEN
            RAISE EXCEPTION
            'Estoque insuficiente. Estoque atual: %',
            v_estoque_atual;
        END IF;

        UPDATE produto
        SET quantidade = quantidade - p_quantidade
        WHERE id_produto = p_id_produto;


    ELSE

        RAISE EXCEPTION
        'Tipo inválido. Utilize ENTRADA ou SAIDA.';

    END IF;


    -- Registra o histórico da movimentação
    INSERT INTO movimentacao_estoque (
        id_produto,
        tipo,
        quantidade
    )
    VALUES (
        p_id_produto,
        UPPER(p_tipo),
        p_quantidade
    );

END;
$$;
