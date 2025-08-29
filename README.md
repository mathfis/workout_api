# 🏋️ Workout API - API de Competição de CrossFit

## 📋 Sobre o Projeto

A WorkoutAPI é uma API para gerenciamento de competições de CrossFit, desenvolvida com FastAPI para fornecer alta performance e facilidade de uso. A API permite o gerenciamento completo de atletas, categorias e centros de treinamento.

## 🚀 Funcionalidades

### ✅ Implementadas
- **CRUD Completo** para Atletas, Categorias e Centros de Treinamento
- **Query Parameters** para filtros avançados
- **Paginação Automática** com fastapi-pagination
- **Responses Customizados** com relacionamentos
- **Tratamento de Exceções** específico para erros de integridade
- **Validação de Dados** com Pydantic
- **Documentação Interativa** automática

### 📊 Endpoints Disponíveis

#### 🏃 Atletas (`/alunos`)
```http
GET    /alunos?nome=João&cpf=12345678900
GET    /alunos/{id}
POST   /alunos
PUT    /alunos/{id}
DELETE /alunos/{id}
```
```http
```

🏆 Categorias (/categorias)
```http
GET    /categorias?nome=Iniciante
GET    /categorias/{id}
POST   /categorias
PUT    /categorias/{id}
DELETE /categorias/{id}
```
🏟️ Centros de Treinamento (/centros)
```http
GET    /centros?nome=Academia&proprietario=João
GET    /centros/{id}
POST   /centros
PUT    /centros/{id}
DELETE /centros/{id}
```


🛠️ Tecnologias Utilizadas
- *Python 3.11+*
- *FastAPI* - Framework web moderno e rápido
- *SQLAlchemy* - ORM para banco de dados
- *SQLite* - Banco de dados para desenvolvimento
- *Pydantic* - Validação de dados e serialização
- *fastapi-pagination* - Paginação automática
- *Uvicorn* - Servidor ASGI

📦 Instalação e Configuração
Pré-requisitos
- Python 3.11 ou superior
- pip (gerenciador de pacotes Python)

--

#### 1. Clone o repositório

```bash
git clone <url-do-repositorio>
cd workout_api
```

#### 2. Crie e ative o ambiente virtual
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

#### 3.  Instale as dependências
```bash
pip install -r requirements.txt
```
#### 4. Execute a aplicação
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```



### 🌐 Acessando a API

A API estará disponível em:

- API Local: http://localhost:8000

- Documentação Interativa: http://localhost:8000/docs

- Documentação Alternativa: http://localhost:8000/redoc


### 📝 Exemplos de Uso
Criar um Atleta

```bash
curl -X POST "http://localhost:8000/alunos" \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "João Silva",
    "cpf": "12345678900",
    "idade": 25,
    "peso": 75.5,
    "altura": 1.80,
    "sexo": "M",
    "centro_treinamento_id": 1,
    "categoria_id": 1
  }'
```

Listar Atletas com Filtros

```bash
curl "http://localhost:8000/alunos?nome=João&page=1&size=10"
```
Buscar Atleta por ID
```bash
curl "http://localhost:8000/alunos/1"
```
### 🗃️ Estrutura do Banco de Dados

Diagrama de Entidade-Relacionamento
```text
CentroTreinamento (1) -- (N) Categoria (1) -- (N) Aluno
```

Tabelas
- centro_treinamento: Centros de treinamento
- categoria: Categorias de competição
- aluno: Atletas participantes

### ⚙️ Variáveis de Ambiente
Crie um arquivo .env na raiz do projeto:

```bash
DATABASE_URL=sqlite:///./workout.db
```

### 🚨 Tratamento de Erros
A API retorna códigos de status HTTP apropriados:

- 200 OK - Requisição bem-sucedida

- 201 Created - Recurso criado com sucesso

- 303 See Other - CPF duplicado (erro de integridade)

- 404 Not Found - Recurso não encontrado

- 422 Unprocessable Entity - Erro de validação

### 📊 Paginação
Todos os endpoints de listagem suportam paginação automática:

```http
GET /alunos?page=1&size=20
```
Resposta paginada:
```json
{
  "items": [...],
  "total": 100,
  "page": 1,
  "size": 20,
  "pages": 5
}
```
### 🔧 Desenvolvimento
Estrutura do Projeto
```text
workout_api/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── routes/
│   │   ├── alunos.py
│   │   ├── categorias.py
│   │   └── centros_treinamento.py
│   └── core/
│       └── config.py
├── requirements.txt
├── .env
└── README.md
```

Comandos Úteis

```bash
# Executar testes
python -m pytest

# Verificar qualidade do código
pylint app/

# Formatar código
black app/
```

###
🤝 Contribuição
1. Faça um fork do projeto

2. Crie uma branch para sua feature (git checkout -b feature/AmazingFeature)

3. Commit suas mudanças (git commit -m 'Add some AmazingFeature')

4. Push para a branch (git push origin feature/AmazingFeature)

5. Abra um Pull Request


## 📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

