# 📘 Atividade: Testando APIs REST com FastAPI

## 🎯 Objetivo

Escreva testes automatizados para uma API REST criada com FastAPI. Use `pytest` e `TestClient` para verificar respostas, códigos HTTP e validação de dados sem iniciar um servidor manualmente.

## 📝 Tarefas

### 🛠️ Testar respostas de sucesso

#### Descrição

Use o teste de exemplo em `test_main.py` como referência e crie testes para as rotas que listam e consultam livros. A API que será testada está em `main.py`.

#### Requisitos

O programa concluído deve:

- Criar um `TestClient` usando a aplicação FastAPI importada de `main.py`.
- Verificar que `GET /health` responde com código HTTP `200` e o JSON `{"status": "ok"}`.
- Verificar que `GET /books` responde com código HTTP `200` e inclui os livros iniciais.
- Verificar que `GET /books/1` responde com código HTTP `200` e os dados do livro de ID `1`.
- Executar os testes com `pytest -q`.

### 🛠️ Testar erros HTTP e validação

#### Descrição

Amplie os testes para cobrir um livro inexistente e a rota de criação. Envie requisições com dados válidos e inválidos para observar como a API responde.

#### Requisitos

O programa concluído deve:

- Verificar que `GET /books/999` responde com código HTTP `404`.
- Verificar que `POST /books` com título e autor responde com código HTTP `201` e retorna os dados do livro criado.
- Verificar que `POST /books` sem um campo obrigatório responde com código HTTP `422`.
- Confirmar os dados relevantes no JSON de cada resposta, além do código HTTP.
- Manter os testes independentes: cada teste deve verificar seu próprio resultado sem depender da ordem de execução.

Para instalar as dependências e executar os testes:

```bash
python -m pip install fastapi pytest httpx
pytest -q
```