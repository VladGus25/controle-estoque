-- =========================================
-- INSERTS: CATEGORIA
-- =========================================

INSERT INTO categoria (id_categoria, nome) VALUES
(1, 'Periféricos'),
(2, 'Informática'),
(3, 'Acessórios'),
(4, 'Componentes');


-- =========================================
-- INSERTS: PRODUTO
-- =========================================

INSERT INTO produto
(id_produto, nome, preco, quantidade, id_categoria)
VALUES
(1, 'Teclado Mecânico', 250.00, 10, 1),
(2, 'Mouse Gamer RGB', 180.00, 5, 1),
(3, 'Notebook', 3500.00, 3, 2),
(4, 'Monitor', 900.00, 0, 2),
(5, 'Headset', 300.00, 8, 3),
(6, 'Memória RAM 16GB', 350.00, 5, 4),
(7, 'Iphone 16e', 5600.00, 90, 2);


-- =========================================
-- INSERTS: MOVIMENTAÇÃO
-- =========================================

INSERT INTO movimentacao_estoque
(id_produto, tipo, quantidade)
VALUES
(1, 'SAIDA', 3);