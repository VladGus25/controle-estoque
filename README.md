# Sistema de Controle de Estoque

## Identificação

**Aluno:** Vladimir Gustavo
**Disciplina:** Projeto de Banco de Dados - Prática
**Professor:** Anderson Soares Costa

---

## Sobre o projeto

Este projeto consiste em um **Sistema de Controle de Estoque**, desenvolvido para permitir o gerenciamento de produtos e o controle das movimentações de entrada e saída do estoque.

A aplicação foi desenvolvida como uma evolução de um sistema CRUD, incorporando recursos avançados de banco de dados estudados durante a disciplina, utilizando **View, Function e Procedure** integradas diretamente às funcionalidades da aplicação.

O sistema permite cadastrar, consultar, editar e excluir produtos, além de realizar movimentações de estoque, consultar relatórios e visualizar o histórico das movimentações.

---

## Funcionalidades

* Cadastro de produtos
* Listagem de produtos
* Edição de produtos
* Exclusão de produtos
* Entrada de produtos no estoque
* Saída de produtos do estoque
* Consulta do relatório de estoque
* Cálculo do valor total do estoque
* Consulta do histórico de movimentações
* Validação das movimentações de estoque

---

## Tecnologias utilizadas

* **Python**
* **PostgreSQL**
* **Supabase**
* **Git**
* **GitHub**
* **python-dotenv**

---

## Banco de dados

### SGBD

O projeto utiliza **PostgreSQL**, hospedado através do **Supabase**.

### Principais tabelas

O banco de dados possui as seguintes tabelas principais:

* `categoria` — armazena as categorias dos produtos.
* `produto` — armazena as informações dos produtos.
* `movimentacao_estoque` — registra as entradas e saídas realizadas no estoque.

### View

**`vw_relatorio_estoque`**

A View foi criada para fornecer um relatório organizado dos produtos em estoque, reunindo informações das tabelas relacionadas.

Ela é utilizada pela aplicação na funcionalidade de **relatório de estoque**.

### Function

**`calcular_valor_estoque`**

A Function é responsável por calcular o valor do estoque com base no preço e na quantidade dos produtos.

Ela é chamada pela aplicação através da funcionalidade de **cálculo do valor do estoque**.

### Procedure

**`movimentar_estoque`**

A Procedure é responsável por realizar as movimentações de estoque.

Ela permite registrar operações de **entrada e saída de produtos**, atualizando a quantidade disponível e registrando a movimentação.

A aplicação utiliza essa Procedure nas funcionalidades de movimentação de estoque.

---

## Integração entre aplicação e banco

Os recursos de banco de dados foram integrados diretamente às funcionalidades da aplicação.

### View

```text
Aplicação
    ↓
Consulta da View
    ↓
vw_relatorio_estoque
    ↓
Resultado apresentado no sistema
```

### Function

```text
Aplicação
    ↓
Chamada da Function
    ↓
calcular_valor_estoque
    ↓
Valor calculado
    ↓
Resultado apresentado no sistema
```

### Procedure

```text
Aplicação
    ↓
Chamada da Procedure
    ↓
movimentar_estoque
    ↓
Atualização do estoque
    ↓
Registro da movimentação
```

Dessa forma, a View, Function e Procedure não estão apenas criadas no banco de dados, mas são utilizadas em funcionalidades reais da aplicação.

---

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
│   │
│   ├── inserts/
│   │   └── inserts.sql
│   │
│   ├── procedures/
│   │   └── procedures.sql
│   │
│   ├── tables/
│   │   └── tables.sql
│   │
│   ├── views/
│   │   └── views.sql
│   │
│   └── README.md
│
├── src/
│   ├── conexao.py
│   └── main.py
│
├── .env
├── .gitignore
└── README.md
```

---

## Como executar

### 1. Clonar o repositório

```bash
git clone https://github.com/VladGus25/controle-estoque.git
```

### 2. Entrar na pasta

```bash
cd controle-estoque
```

### 3. Instalar as dependências

```bash
pip install supabase python-dotenv
```

### 4. Configurar o Supabase

Criar um arquivo `.env` na raiz do projeto contendo:

```env
SUPABASE_URL=sua_url_do_supabase
SUPABASE_KEY=sua_chave_do_supabase
```

As credenciais devem permanecer privadas e o arquivo `.env` não deve ser enviado ao GitHub.

### 5. Configurar o banco de dados

Executar os scripts SQL disponíveis na pasta `database`, seguindo a ordem necessária para criação das tabelas e dos recursos utilizados pelo sistema.

### 6. Executar a aplicação

```bash
python src/main.py
```

---

## Objetivos de aprendizagem

O projeto foi desenvolvido com o objetivo de praticar e demonstrar conhecimentos em:

* Desenvolvimento de aplicações CRUD
* Integração entre Python e PostgreSQL
* Utilização do Supabase
* Criação e utilização de Views
* Criação e utilização de Functions
* Criação e utilização de Procedures
* Manipulação de dados
* Controle de estoque
* Variáveis de ambiente
* Versionamento com Git
* Publicação de projetos no GitHub

---

## Autor

**Vladimir Gustavo**

GitHub: [VladGus25](https://github.com/VladGus25/controle-estoque)
