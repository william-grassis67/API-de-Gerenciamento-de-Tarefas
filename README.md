# API de Gerenciamento de Tarefas

API REST desenvolvida com Python e FastAPI para praticar os fundamentos do desenvolvimento backend, incluindo criação de rotas HTTP, validação de dados, operações CRUD e tratamento de erros.

## Tecnologias utilizadas

- **Python 3.14+** — linguagem de programação.
- **FastAPI** — framework para construção de APIs REST.
- **Pydantic** — validação e estruturação dos dados.
- **Uvicorn** — servidor ASGI utilizado para executar a aplicação.

## Funcionalidades

- [x] Estrutura inicial da aplicação FastAPI.
- [ ] Listar todas as tarefas.
- [ ] Cadastrar novas tarefas.
- [ ] Consultar uma tarefa por ID.
- [ ] Excluir tarefas por ID.
- [ ] Validar dados recebidos.
- [ ] Tratar erros HTTP, incluindo 404 para tarefas inexistentes.

> As funcionalidades devem ser marcadas como concluídas conforme forem implementadas.

## Como executar o projeto

### 1. Clone o repositório

```bash
git clone URL_DO_SEU_REPOSITORIO
cd NOME_DO_REPOSITORIO
```

Substitua `URL_DO_SEU_REPOSITORIO` e `NOME_DO_REPOSITORIO` pelos dados do seu repositório.

### 2. Crie um ambiente virtual

```bash
python3 -m venv .venv
```

### 3. Ative o ambiente virtual

No Fedora ou em outras distribuições Linux:

```bash
source .venv/bin/activate
```

### 4. Instale as dependências

```bash
python -m pip install "fastapi[standard]"
```

### 5. Inicie a API

Certifique-se de que o arquivo principal se chama `main.py`.

```bash
python -m fastapi dev main.py
```

A aplicação será executada localmente, normalmente na porta `8000`.

## Documentação e testes

Com o servidor em execução, acesse:

- **Documentação interativa:** http://127.0.0.1:8000/docs
- **Documentação alternativa:** http://127.0.0.1:8000/redoc
- **Endpoint inicial:** http://127.0.0.1:8000/

Também é possível testar as requisições usando `curl` no terminal.

## Endpoints planejados

| Método HTTP | Endpoint | Descrição |
|---|---|---|
| GET | `/` | Retorna uma mensagem inicial |
| GET | `/tarefas` | Lista todas as tarefas |
| POST | `/tarefas` | Cadastra uma tarefa |
| GET | `/tarefas/{id}` | Consulta uma tarefa pelo ID |
| DELETE | `/tarefas/{id}` | Exclui uma tarefa pelo ID |

Os endpoints representam o escopo planejado do exercício; confirme sua implementação antes de considerar a API completa.

## Modelo de dados

Cada tarefa utiliza a seguinte estrutura:

```json
{
  "titulo": "Estudar Python e FastAPI",
  "concluida": false
}
```

- `titulo`: título da tarefa, do tipo string.
- `concluida`: indica se a tarefa foi concluída, do tipo booleano, com valor padrão `false`.

O campo `id` será gerado pela aplicação quando uma tarefa for cadastrada.

## Estrutura do projeto

```text
minha-api/
├── .venv/
├── main.py
├── .gitignore
└── README.md
```

O diretório `.venv/` contém o ambiente virtual e não deve ser enviado ao Git.

## Próximas melhorias

- Implementar atualização de tarefas com PUT ou PATCH.
- Persistir os dados em um banco de dados PostgreSQL.
- Criar testes automatizados com pytest.
- Implementar autenticação e autorização.
- Organizar a aplicação em módulos.
- Preparar a API para deploy.

## Objetivo educacional

Este projeto faz parte dos meus estudos de Python e desenvolvimento backend, com foco na construção de APIs REST, boas práticas de programação e aprendizado progressivo de tecnologias utilizadas no mercado.

---

**Autor:** William Roque

**Tecnologias:** Python · FastAPI · Pydantic · Uvicorn
