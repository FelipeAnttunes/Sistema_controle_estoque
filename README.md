# Sistema de Controle de Estoque

Sistema de controle de estoque desenvolvido em Python com integração ao PostgreSQL.

O projeto foi criado com fins de estudo e portfólio para praticar desenvolvimento backend, banco de dados relacionais e operações CRUD utilizando Python.

## Funcionalidades

* Cadastro de produtos
* Listagem de produtos
* Atualização de produtos
* Exclusão de produtos
* Conexão com PostgreSQL
* Utilização de variáveis de ambiente (.env)
* Menu interativo via terminal

## Tecnologias Utilizadas

* Python 3
* PostgreSQL
* psycopg2
* python-dotenv
* Git
* GitHub

## Estrutura do Projeto

```text
controle-estoque/
│
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
│
├── sql/
│   └── create_tables.sql
│
└── src/
    ├── database.py
    ├── produto.py
    └── main.py
```

## Banco de Dados

Tabela utilizada:

```sql
CREATE TABLE produtos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    marca VARCHAR(100),
    quantidade INT NOT NULL DEFAULT 0,
    valor NUMERIC(10,2) NOT NULL,
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Configuração

### 1. Clonar o repositório

```bash
git clone <url-do-repositorio>
```

### 2. Criar ambiente virtual

```bash
python -m venv venv
```

### 3. Ativar ambiente virtual

Windows:

```bash
venv\Scripts\activate
```

### 4. Instalar dependências

```bash
pip install -r requirements.txt
```

### 5. Criar arquivo .env

Utilize o arquivo `.env.example` como referência:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=controle_estoque
DB_USER=postgres
DB_PASSWORD=sua_senha
```

### 6. Criar banco de dados

```sql
CREATE DATABASE controle_estoque;
```

Execute também o script:

```text
sql/create_tables.sql
```

## Executando o Projeto

```bash
python src/main.py
```

## Menu do Sistema

```text
1 - Cadastrar Produto
2 - Listar Produtos
3 - Atualizar Produto
4 - Deletar Produto
5 - Sair
```

## Objetivos de Aprendizado

* Integração Python com PostgreSQL
* Operações CRUD
* Manipulação de banco de dados relacional
* Uso de variáveis de ambiente
* Organização de projetos backend
* Versionamento com Git e GitHub

## Autor

Luiz Felipe Antunes

Projeto desenvolvido para fins de estudo e construção de portfólio.
