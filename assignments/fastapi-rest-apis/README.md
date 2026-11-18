# 📘 Atividade: Construindo APIs REST com FastAPI

## 🎯 Objetivo

Construa uma API REST com FastAPI para consultar e gerenciar livros. Pratique rotas HTTP, parâmetros de caminho, validação de dados com Pydantic e códigos de status.

## 📝 Tarefas

### 🛠️ Criar rotas para consultar livros

#### Descrição

Complete o scaffold em `main.py` para criar uma API que disponibiliza informações de saúde do serviço e permite consultar uma coleção de livros. Instale as dependências com `python -m pip install fastapi uvicorn` e inicie a aplicação com `uvicorn main:app --reload`.

#### Requisitos

O programa concluído deve:

- Disponibilizar `GET /health`, retornando o JSON `{"status": "ok"}`.
- Disponibilizar `GET /books`, retornando a lista de livros inicial.
- Disponibilizar `GET /books/{book_id}`, usando um parâmetro de caminho para retornar um livro pelo ID.
- Retornar o código HTTP `404` quando o ID solicitado não existir.
- Permitir testar as rotas pela documentação interativa em `/docs`.

### 🛠️ Adicionar operações para gerenciar livros

#### Descrição

Amplie a API para permitir criar, atualizar e remover livros. Use os modelos Pydantic do scaffold para validar os dados enviados nas requisições.

#### Requisitos

O programa concluído deve:

- Disponibilizar `POST /books` para criar um livro com título e autor, atribuir um ID único e responder com o código HTTP `201`.
- Disponibilizar `PUT /books/{book_id}` para atualizar o título e o autor de um livro existente.
- Disponibilizar `DELETE /books/{book_id}` para remover um livro existente e responder com o código HTTP `204`, sem corpo na resposta.
- Retornar o código HTTP `404` ao tentar atualizar ou remover um livro inexistente.
- Usar os modelos Pydantic para validar os dados de entrada e retornar respostas JSON.