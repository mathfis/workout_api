# 🏋️ Workout API - API de Competição de CrossFit

## 🎯 Visão Geral e Objetivo da Refatoração
A WorkoutAPI é um Microservice RESTful para gerenciamento de competições de CrossFit. Este repositório está em processo de refatoração para se tornar um projeto de portfólio de nível profissional, focado em Arquitetura Orientada a Domínio (SoC), Qualidade de Código e Containerização.

## O Processo de Refatoração
O projeto original, que possuía uma estrutura monolítica, foi completamente reestruturado. A refatoração tem como foco garantir os seguintes resultados:

Arquitetura: Aplicar o padrão de Separação de Responsabilidades (SoC), implementando as camadas de Serviço e Repositório para isolar a Lógica de Negócio da Persistência.

Qualidade de Código: Implementar Tipagem Rigorosa (Type Hinting) e gerenciar configurações com Pydantic Settings.

Containerização: Criar uma solução completa de Docker Compose (API + PostgreSQL).

_______________________________________________________________________

## 🏗️ Estrutura Arquitetural Atual (Refatoração Concluída: 1/3)

A primeira etapa da refatoração, a organização estrutural e modular, está concluída. O código foi rearranjado para separar as preocupações em camadas lógicas.

<br>

### 📂 Estrutura de Diretórios
A estrutura reflete agora uma arquitetura de microservice, pronta para receber a lógica de código nas novas camadas:

```bash
workout_api/
├── app/                  # Código-fonte do Microservice
│   ├── api/
│   │   └── routers/v1/   # Camada de Apresentação (Antigo routes/)
│   ├── services/         # Camada de Lógica de Negócio (NOVA: Vazia)
│   ├── repositories/     # Camada de Persistência (NOVA: Vazia)
│   ├── database/         
│   │   ├── connection.py # Conexão com o DB (Antigo database.py)
│   │   └── models/       # Modelos SQLAlchemy (Antigo models.py)
│   ├── schemas/          # Modelos de Dados Pydantic (Antigo schemas.py)
│   └── core/             # Configurações e Exceções
│       └── config.py     # Gerenciamento de Configurações
└── requirements.txt
```

<br>

### 🎯 Motivação da Estrutura

| Camada | Diretório | Motivo da Separação (SoC) |
| :--- | :--- | :--- |
| **Routers** | `app/api/routers/` | Garantir que o endpoint apenas receba a requisição e delegue, mantendo o código limpo e focado em HTTP. |
| **Services** | `app/services/` | Centralizar as regras de negócio complexas, como validações e orquestração de operações. |
| **Repositories** | `app/repositories/` | Abstrair o acesso ao banco de dados (SQLAlchemy), isolando a lógica de negócio da tecnologia de persistência. |

<br>

## 🛠️ Tecnologias Atuais e Próximos Passos

| Categoria | Tecnologia | Status no Projeto |
| :--- | :--- | :--- |
| **Web Framework** | Fast API | Em uso |
| **Persistência** | SQL Alchemy ORM | Em uso (SQL Lite) |
| **Arquitetura** | Separação de Responsabilidades (SoC) | **Estrutura de Diretórios Implementada** |

<br>

### ➡️ Próximos Passos no Processo de Refatoração
Refatoração do Core: Implementar Pydantic Settings no app/core/config.py e criar exceções de negócio customizadas.

Implementação de Camadas: Mover a lógica de negócio e persistência dos routers para as camadas de Service e Repository.

Containerização: Criar o Dockerfile e o docker-compose.yml para PostgreSQL.

## Qualidade do Código

**Pydantic Settings**: Gerenciamento seguro de configuração, garantindo que as variáveis de ambiente (como DATABASE_URL) sejam lidas com tipagem rigorosa e priorizando as configurações do ambiente Docker.



