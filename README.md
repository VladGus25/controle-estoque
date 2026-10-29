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

A interface web foi desenvolvida com **Flask**, substituindo o menu de terminal por um dashboard acessível pelo navegador.

---

## Funcionalidades

- Cadastro de produtos
- Listagem de produtos
- Edição de produtos
- Exclusão de produtos
- Entrada de produtos no estoque
- Saída de produtos do estoque
- Consulta do relatório de estoque
- Cálculo do valor total do estoque
- Consulta do histórico de movimentações
- Validação das movimentações de estoque
- Dashboard com visão geral do estoque
- Cache de consultas com Redis

---

## Tecnologias utilizadas

- **Python**
- **Flask**
- **PostgreSQL**
- **Supabase**
- **Redis**
- **Git**
- **GitHub**
- **python-dotenv**

---

## Banco de dados

### SGBD

O projeto utiliza **PostgreSQL**, hospedado através do **Supabase**.

### Principais tabelas

O banco de dados possui as seguintes tabelas principais:

- `categoria` — armazena as categorias dos produtos.
- `produto` — armazena as informações dos produtos.
- `movimentacao_estoque` — registra as entradas e saídas realizadas no estoque.

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

```
Aplicação (Flask)
    ↓
Rota /relatorio
    ↓
vw_relatorio_estoque
    ↓
Resultado apresentado na interface web
```

### Function

```
Aplicação (Flask)
    ↓
Rota /calcular
    ↓
calcular_valor_estoque
    ↓
Valor calculado
    ↓
Resultado apresentado na interface web
```

### Procedure

```
Aplicação (Flask)
    ↓
Rota /movimentacao
    ↓
executar_movimentacao_estoque
    ↓
Atualização do estoque
    ↓
Registro da movimentação
```

---

## Cache com Redis

A listagem de produtos utiliza **Redis** como camada de cache.

- Na primeira consulta, os dados são buscados no Supabase e armazenados no Redis por 5 minutos.
- Nas consultas seguintes, os dados são retornados diretamente do Redis, sem acessar o banco.
- O cache é invalidado automaticamente ao cadastrar, editar, excluir um produto ou registrar uma movimentação.

A interface indica visualmente a origem dos dados: **Redis Cache** ou **Supabase**.

---

## Estrutura do projeto

```
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
│   ├── views/
│   │   └── views.sql
│   └── README.md
│
├── src/
│   ├── app.py              ← servidor Flask (interface web)
│   ├── conexao.py          ← conexão com Supabase
│   ├── redis_conexao.py    ← conexão com Redis
│   └── teste_redis.py      ← teste de conexão Redis
│
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── produtos.html
│   ├── produto_form.html
│   ├── relatorio.html
│   ├── calcular.html
│   ├── movimentacao.html
│   └── historico.html
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Como executar

### 1. Clonar o repositório

```
git clone https://github.com/VladGus25/controle-estoque.git
```

### 2. Entrar na pasta

```
cd controle-estoque
```

### 3. Instalar as dependências

```
pip install -r requirements.txt
```

### 4. Configurar o Supabase e Redis

Criar um arquivo `.env` na raiz do projeto contendo:

```
SUPABASE_URL=sua_url_do_supabase
SUPABASE_KEY=sua_chave_do_supabase
REDIS_HOST=seu_host_redis
REDIS_PORT=6379
REDIS_USERNAME=default
REDIS_PASSWORD=sua_senha_redis
```

As credenciais devem permanecer privadas e o arquivo `.env` não deve ser enviado ao GitHub.

### 5. Configurar o banco de dados

Executar os scripts SQL disponíveis na pasta `database`, na seguinte ordem:

1. `tables/tables.sql`
2. `inserts/inserts.sql`
3. `views/views.sql`
4. `functions/functions.sql`
5. `procedures/procedures.sql`

### 6. Executar a aplicação

```
python src/app.py
```

### 7. Acessar no navegador

```
http://localhost:5000
```

---

## Objetivos de aprendizagem

O projeto foi desenvolvido com o objetivo de praticar e demonstrar conhecimentos em:

- Desenvolvimento de aplicações CRUD
- Integração entre Python e PostgreSQL
- Utilização do Supabase
- Criação e utilização de Views
- Criação e utilização de Functions
- Criação e utilização de Procedures
- Manipulação de dados
- Controle de estoque
- Cache de dados com Redis
- Interface web com Flask
- Variáveis de ambiente
- Versionamento com Git
- Publicação de projetos no GitHub

---

## Autor

**Vladimir Gustavo**

GitHub: [VladGus25](https://github.com/VladGus25)