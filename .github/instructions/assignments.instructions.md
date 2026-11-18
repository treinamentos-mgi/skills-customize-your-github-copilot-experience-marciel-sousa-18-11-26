---
description: "Instruções para usar sempre que criar ou editar arquivos markdown de assignment, garantindo consistência e clareza para os alunos."
applyTo: "assignments/**/*.md"
---

# Diretrizes de Estrutura para Markdowns de Tarefas

Use estas diretrizes ao criar ou editar arquivos Markdown de tarefas em `assignments/`.

## 1. Uso do Template

- Cada atividade deve ficar em sua própria subpasta de `assignments/` e ser descrita em um arquivo `README.md`.
- Siga a estrutura e a ordem de seções de [`templates/assignment-template.md`](../../templates/assignment-template.md).
- Preserve as duas seções de tarefa presentes no template. Não remova nem pule seções obrigatórias.

## 2. Orientação das Seções

Mantenha os cabeçalhos exatamente como aparecem no template, incluindo os emojis. Não os traduza nem acrescente seções sem solicitação explícita.

- `# 📘 Atividade: [Título da Atividade]` — Use um título curto e descritivo no idioma da atividade.
- `## 🎯 Objetivo` — Resuma em uma ou duas frases o que o aluno aprenderá ou construirá.
- `## 📝 Tarefas` — Inclua as duas tarefas do template, cada uma com a seguinte estrutura:
   - `### 🛠️ [Título da Tarefa]` — Use um título específico e orientado à ação.
   - `#### Descrição` — Explique claramente o que o aluno deve fazer.
   - `#### Requisitos` — Mantenha a frase `O programa concluído deve:` e liste resultados esperados em itens objetivos e verificáveis.

Use linguagem clara e amigável ao aluno, mantenha o idioma consistente e inclua exemplos de entrada e saída em blocos de código quando ajudarem a esclarecer os requisitos.
