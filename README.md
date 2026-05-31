#  Sistema de Controle de Estoque

Sistema de controle de estoque desenvolvido em Python com integração ao PostgreSQL.  
O projeto tem como objetivo praticar desenvolvimento backend, banco de dados relacional e organização de projetos.

---

##  Status do Projeto

-> Conexão com banco de dados concluída  
X CRUD de produtos em desenvolvimento  
X Menu interativo em construção  

---

##  Objetivo

Este projeto tem fins educacionais e de portfólio, com foco em:

- Conexão entre Python e PostgreSQL
- Operações CRUD (Create, Read, Update, Delete)
- Estruturação de projetos backend
- Uso de variáveis de ambiente (.env)
- Boas práticas de organização de código

---

##  Tecnologias Utilizadas

- Python 3
- PostgreSQL
- psycopg2
- python-dotenv
- Git / GitHub

---

##  Estrutura do Projeto

controle-estoque/
│
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md
│
├── sql/
│ └── create_tables.sql
│
└── src/
├── database.py
├── main.py
└── produto.py (em desenvolvimento)


---

## ▶️ Execução do Projeto

Execute o arquivo principal:

bash

python src/main.py

Se a conexão estiver correta, será exibido:

Conexão realizada com sucesso!