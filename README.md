# SubTracker

[![Status](https://img.shields.io/badge/status-em_desenvolvimento-yellow)]()
[![Versão](https://img.shields.io/badge/versão-0.1.0-blue)]()
[![Licença](https://img.shields.io/badge/licença-acadêmica-lightgrey)]()

**Instituição:** Centro Universitário de Brasília (UniCEUB)
**Curso:** Análise e Desenvolvimento de Sistemas
**Disciplina:** Desenvolvimento Web
**Turma / Semestre:** [preencher]
**Professor(a):** Felippe Pires Ferreira
**Status do projeto:** Em desenvolvimento (Fase 1 — Documentação e arquitetura)

---

## Sumário
(mantém igual ao template)

---

## 1. Descrição do projeto

*Escreva aqui, com suas palavras, 2 a 4 parágrafos respondendo: qual problema de gestão de assinaturas/gastos recorrentes o SubTracker resolve? O que ele tem de diferente de apps como Bobby, Subscript etc.? (vocês já definiram dois diferenciais: divisão de custo entre pessoas + conversão de câmbio — explique o porquê de cada um valer a pena pro usuário.)*

### Objetivos

- **Objetivo geral:** [defina em uma frase o que o sistema entrega]
- **Objetivos específicos:**
  - [ex: permitir cadastro de assinaturas com valor, ciclo de cobrança e categoria]
  - [ex: permitir dividir o custo de uma assinatura entre múltiplos usuários]
  - [ex: converter automaticamente valores em moeda estrangeira via API de câmbio]
  - [adicione os demais que o grupo definir]

### Público-alvo

- [ex: estudantes que dividem assinaturas com colegas de república/família]
- [outros perfis que o grupo identificar]

---

## 2. Funcionalidades

| Funcionalidade | Descrição | Status |
| --- | --- | --- |
| Cadastro de assinaturas | [CRUD completo: nome, valor, categoria, ciclo de cobrança] | Planejada |
| Divisão de custos | [cadastro de participantes por assinatura + cálculo de quanto cada um deve] | Planejada |
| Conversão de moeda | [consumo de API externa de câmbio para assinaturas em dólar/outras moedas] | Planejada |
| Busca | [pesquisa por nome, categoria, status] | Planejada |
| Relatórios | [gasto mensal/anual, por categoria, exportável] | Planejada |
| API REST própria | [endpoints para terceiros consultarem dados de assinaturas] | Planejada |

### Requisitos não funcionais

- **Desempenho:** [defina um critério realista, ex: resposta da API em menos de X segundos]
- **Segurança:** [ex: HTTPS em produção, segredos via variáveis de ambiente]
- **Usabilidade:** [ex: interface responsiva]
- **Disponibilidade:** [ex: aplicação publicada e acessível durante o período de avaliação]

---

## 3. Demonstração
*(preencher na Fase 2, com prints/GIF reais da aplicação)*

---

## 4. Tecnologias utilizadas

| Camada | Tecnologia | Versão |
| --- | --- | --- |
| Linguagem | Python | [definir] |
| Backend | Django | [definir] |
| API REST | Django REST Framework | [definir] |
| Banco de dados | [PostgreSQL/SQLite — definir qual usarão em produção] | [definir] |
| Frontend | [Templates Django / outro — definir] | — |
| Testes | [pytest, etc. — definir] | — |
| Infraestrutura | [Docker? GitHub Actions? — definir] | — |

---

## 5. Arquitetura

*Descreva aqui as camadas da aplicação e por que o grupo tomou essas decisões técnicas (isso precisa corresponder ao diagrama UML de componentes que vocês vão anexar em `docs/arquitetura/`).*

```text
[Usuário] → [Interface / Frontend] → [API / Backend Django] → [Banco de dados]
```

### Endpoints principais (API própria)
*Preencher conforme o contrato inicial da API definido em `docs/api/`.*

| Método | Rota | Descrição |
| --- | --- | --- |
| `GET` | `/api/subscriptions/` | Listar assinaturas |
| `POST` | `/api/subscriptions/` | Criar assinatura |
| `GET` | `/api/subscriptions/{id}/` | Detalhar assinatura |
| `PUT` | `/api/subscriptions/{id}/` | Atualizar assinatura |
| `DELETE` | `/api/subscriptions/{id}/` | Remover assinatura |

Documentação completa: [link Swagger/Redoc — Fase 2]

---

## 6. Organização dos diretórios
(adaptar a árvore do template conforme a estrutura real que vocês montarem — já criamos `docs/visao`, `docs/casos-de-uso`, `docs/arquitetura`, `docs/banco-de-dados`, `docs/api`, `docs/prototipos`, `docs/planejamento`, `docs/diagramas`, `docs/seguranca`)

---

## 7. Participantes

| Nome | Matrícula | Função no projeto |
| --- | --- | --- |
| Gustavo [sobrenome] | [matrícula] | [ex: coordenação / backend] |
| [colega 2] | [matrícula] | [função] |
| [colega 3] | [matrícula] | [função] |
| [colega 4] | [matrícula] | [função] |

**Professor(a) responsável:** Felippe Pires Ferreira

---

## 8. Como executar
*(preencher conforme o setup real do projeto Django, quando o código existir — Fase 2)*

---

## 9. Configuração

| Variável | Obrigatória | Descrição | Exemplo |
| --- | --- | --- | --- |
| `SECRET_KEY` | Sim | Chave secreta do Django | `[gerar localmente]` |
| `DEBUG` | Sim | Modo debug (False em produção) | `False` |
| `DATABASE_URL` | Sim | Conexão com o banco | `postgresql://user:senha@host:5432/db` |
| `EXCHANGE_API_KEY` | Depende da API escolhida | Chave da API de câmbio | `[gerar localmente]` |
| `ALLOWED_HOSTS` | Sim | Domínios permitidos em produção | `seudominio.com` |

---

## 10. Testes
*(preencher na Fase 2)*

---

## 11. Uso de inteligência artificial

![Política de uso de IA — semáforo](images/semaforo.png)

### Declaração de uso

- **Houve uso de IA neste projeto?** [respondam honestamente — se usaram Claude/ChatGPT pra consultoria/dúvidas técnicas na Fase 1, mas não para gerar o conteúdo da especificação, digam isso explicitamente]
- **Ferramentas utilizadas:** [ex: Claude — para dúvidas técnicas e organização, não para gerar requisitos/casos de uso]
- **Finalidade:** [ex: esclarecimento de dúvidas sobre Django/Git, revisão de estrutura de documentos]
- **O que NÃO foi delegado à IA:** definição do problema, objetivos, casos de uso, modelo de dados, arquitetura e demais decisões de projeto, que foram elaboradas pelo grupo

---

## 12. Contribuição e fluxo de trabalho
(mantém igual ao template, ajustando nomes de branch se o grupo preferir)

---

## 13. Histórico de versões

| Versão | Data | Descrição |
| --- | --- | --- |
| `0.0.1` | [data] | Estrutura inicial do repositório |

---

## 14. Limitações e próximos passos
*(preencher conforme o grupo for avançando)*

---

## 15. Licença, referências e contato

**Licença:** Uso exclusivamente acadêmico
