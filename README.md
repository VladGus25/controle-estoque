# Sistema de Controle de Estoque

Sistema de controle de estoque desenvolvido em **Python** com integração ao **Supabase (PostgreSQL)**.

O projeto permite cadastrar, consultar, editar e excluir produtos, além de controlar entradas e saídas de estoque e consultar relatórios e histórico de movimentações.

## Funcionalidades

* Cadastro de produtos
* Listagem de produtos
* Edição de produtos
* Exclusão de produtos
* Consulta do relatório de estoque
* Cálculo do valor total do estoque
* Entrada de produtos no estoque
* Saída de produtos do estoque
* Consulta do histórico de movimentações
* Validação de quantidade em movimentações
* Integração com banco de dados PostgreSQL através do Supabase

## Tecnologias utilizadas

* **Python**
* **PostgreSQL**
* **Supabase**
* **Git**
* **GitHub**
* **python-dotenv**

## Estrutura do projeto

```text
controle_estoque/
│
├── config/
│   └── supabase.py
│
├── database/
│   ├── functions/
│   │   └── functions.sql
│   ├── inserts/
│   │   └── inserts.sql
│   ├── procedures/
│   │   └── procedures.sql
│   ├── tables/
│   │   └── tables.sql
│   └── views/
│       └── views.sql
│
├── src/
│   ├── conexao.py
│   └── main.py
│
├── .env
├── .gitignore
└── README.md
```

## Banco de dados

O banco de dados utiliza PostgreSQL através do Supabase.

O projeto possui:

* Tabelas para categorias, produtos e movimentações de estoque
* Functions para operações e cálculos
* Procedure para movimentação de estoque
* View para relatório de estoque
* Scripts SQL para criação e inserção de dados

## Configuração

### 1. Clone o repositório

```bash
git clone https://github.com/VladGus25/controle-estoque.git
```

### 2. Entre na pasta do projeto

```bash
cd controle-estoque
```

### 3. Instale as dependências

```bash
pip install supabase python-dotenv
```

### 4. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
SUPABASE_URL=sua_url_do_supabase
SUPABASE_KEY=sua_chave_do_supabase
```

> **Importante:** nunca compartilhe ou envie o arquivo `.env` para o GitHub. As credenciais do Supabase devem permanecer privadas.

### 5. Execute o projeto

```bash
python src/main.py
```

##  Objetivo

Este projeto foi desenvolvido com o objetivo de praticar conceitos de:

* Programação em Python
* CRUD
* Integração com banco de dados
* PostgreSQL
* Functions e Procedures
* Views
* Controle de estoque
* Variáveis de ambiente
* Git e GitHub

##  Autor

**Vladimir Gustavo**

GitHub: [VladGus25](https://github.com/VladGus25)
