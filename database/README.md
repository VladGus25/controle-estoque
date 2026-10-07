# Banco de Dados

Este diretório contém os scripts SQL utilizados para estruturar e documentar o banco de dados do sistema de controle de estoque.

## Estrutura

### `tables/`

Contém o script responsável pela criação das tabelas do sistema:

- `categoria`
- `produto`
- `movimentacao_estoque`

### `inserts/`

Contém comandos `INSERT` utilizados para cadastrar dados iniciais de exemplo, como:

- Categorias
- Produtos
- Movimentações de estoque

### `functions/`

Contém as Functions utilizadas pelo sistema:

- `calcular_valor_estoque` — calcula o valor total do estoque de um produto.
- `executar_movimentacao_estoque` — executa uma movimentação de estoque e chama a Procedure responsável pela operação.

### `procedures/`

Contém a Procedure:

- `movimentar_estoque` — realiza entradas e saídas de produtos, verifica a quantidade disponível e registra a movimentação no histórico.

### `views/`

Contém a View:

- `vw_relatorio_estoque` — apresenta informações dos produtos, suas categorias, preços, quantidades, valor total em estoque e situação do estoque.

A situação do estoque pode ser:

- `SEM ESTOQUE`
- `ESTOQUE BAIXO`
- `ESTOQUE NORMAL`

## Banco utilizado

O projeto utiliza **PostgreSQL através do Supabase**.

O banco de dados é responsável pelo armazenamento dos produtos, categorias e movimentações, além de possuir Functions, Procedure e View utilizadas pelo sistema.