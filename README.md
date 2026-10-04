# SubTracker

[![Status](https://img.shields.io/badge/status-em_desenvolvimento-yellow)]()
[![Versão](https://img.shields.io/badge/versão-0.1.0-blue)]()
[![Licença](https://img.shields.io/badge/licença-acadêmica-lightgrey)]()

**Instituição:** Centro Universitário de Brasília (UniCEUB)
**Curso:** Análise e Desenvolvimento de Sistemas
**Disciplina:** Desenvolvimento Web
**Turma / Semestre:** A / 4º Semestre
**Professor(a):** Felippe Pires Ferreira
**Status do projeto:** Em desenvolvimento (Fase 1 — Documentação e arquitetura)

---

## Sumário

- [1. Descrição do projeto](#1-descrição-do-projeto)
- [2. Funcionalidades](#2-funcionalidades)
- [3. Demonstração](#3-demonstração)
- [4. Tecnologias utilizadas](#4-tecnologias-utilizadas)
- [5. Arquitetura](#5-arquitetura)
- [6. Organização dos diretórios](#6-organização-dos-diretórios)
- [7. Participantes](#7-participantes)
- [8. Como executar](#8-como-executar)
- [9. Configuração](#9-configuração)
- [10. Testes](#10-testes)
- [11. Uso de inteligência artificial](#11-uso-de-inteligência-artificial)
- [12. Contribuição e fluxo de trabalho](#12-contribuição-e-fluxo-de-trabalho)
- [13. Histórico de versões](#13-histórico-de-versões)
- [14. Limitações e próximos passos](#14-limitações-e-próximos-passos)
- [15. Licença, referências e contato](#15-licença-referências-e-contato)

---

## 1. Descrição do projeto

O **SubTracker** é uma solução web desenvolvida para resolver a falta de controlo centralizado e a fragmentação financeira no acompanhamento de assinaturas e despesas recorrentes. Atualmente, os utilizadores dependem do acompanhamento manual de extratos bancários ou da memória para monitorizar serviços como plataformas de streaming, ferramentas de produtividade, armazenamento em nuvem e licenças de software, o que resulta frequentemente em cobranças esquecidas, acumulação de serviços não utilizados e falta de previsibilidade do orçamento mensal.

Diferenciando-se de aplicações tradicionais de mercado (como *Bobby* ou *Subscript*), o SubTracker foca-se na resolução de dois problemas reais e recorrentes através de funcionalidades chave inovadoras: a **divisão proporcional de custos entre pessoas** e a **conversão automática de câmbio em tempo real**.

A **divisão de custos** permite registar e gerir o rateio de serviços partilhados (como planos familiares de streaming, licenças de software em equipa ou contas de habititação) com familiares, amigos ou colegas. O utilizador pode visualizar com clareza o valor total do serviço e a parcela exata sob a responsabilidade de cada participante, eliminando conflitos e facilitando a cobrança das partes devidas.

Adicionalmente, o sistema aborda a complexidade das assinaturas internacionais com a **conversão dinâmica de câmbio**. Ao consumir cotações atualizadas em tempo real via API externa (AwesomeAPI), o SubTracker converte automaticamente pagamentos em moedas estrangeiras (como USD e EUR) para a moeda base do utilizador (BRL). Isto proporciona uma visão financeira precisa no *Dashboard*, protegendo o utilizador de variações cambiais e permitindo o planeamento exato do impacto real dessas assinaturas no seu orçamento diário.

### Objetivos

- **Objetivo geral:** Desenvolver uma plataforma web centralizada para o gerenciamento inteligente de assinaturas e despesas recorrentes, permitindo o controle financeiro, a divisão de custos entre pessoas e a conversão automática de moedas estrangeiras.
- **Objetivos específicos:**
  - Permitir o cadastro, edição, consulta e cancelamento de assinaturas informando valor, ciclo de cobrança (mensal/anual), categoria e data de vencimento.
  - Oferecer a funcionalidade de divisão proporcional do custo de assinaturas compartilhadas entre múltiplos participantes/pessoas vinculadas.
  - Converter dinamicamente valores de assinaturas em moeda estrangeira (USD e EUR) para Reais (BRL) através da integração em tempo real com a AwesomeAPI.
  - Apresentar um *Dashboard* financeiro consolidado com métricas de gastos totais, distribuição por categoria e alertas visuais de próximos vencimentos.
  - Garantir a persistência e segurança dos dados dos usuários através de autenticação e controle de acesso individualizados.

### Público-alvo

- **Estudantes e Jovens Adultos:** Pessoas que dividem custos de assinaturas de streaming, música ou jogos com familiares, amigos ou colegas de república/apartamento.
- **Consumidores de Serviços Internacionais:** Usuários que assinam ferramentas digitais, plataformas digitais ou serviços em moeda estrangeira (dólar/euro) e precisam prever o custo real em Reais no seu orçamento diário.
- **Profissionais Autônomos e Freelancers:** Pessoas que gerenciam múltiplas assinaturas de softwares e ferramentas de produtividade para trabalho e precisam controlar seus gastos recorrentes.
- **Organizadores de Finanças Pessoais:** Qualquer pessoa que busca centralizar e organizar suas despesas recorrentes mensais/anuais para evitar cobranças indesejadas e surpresas no orçamento.

---

## 2. Funcionalidades

| Funcionalidade | Descrição | Status |
| --- | --- | --- |
| Autenticação de Usuários | Cadastro, login, controle de sessão e gerenciamento de perfil individual. | Planejada |
| Cadastro de Assinaturas | CRUD completo de assinaturas (nome, valor, moeda, categoria, ciclo de cobrança e data de vencimento). | Planejada |
| Divisão de Custos | Vinculação de pessoas/participantes por assinatura e cálculo do rateio do valor para cada um. | Planejada |
| Conversão de Moeda | Consumo de API externa de câmbio (AwesomeAPI) com *caching* em memória (`LocMemCache`) para conversão de moedas (USD/EUR para BRL). | Planejada |
| Busca e Filtros | Pesquisa dinâmica e filtragem de assinaturas por nome, categoria e status (ativa/pausada). | Planejada |
| Dashboard & Relatórios | Visão geral financeira com totalizadores mensais, gráficos de gastos por categoria e resumo exportável. | Planejada |
| API REST própria | Endpoints documentados para autenticação, gerenciamento e consulta de assinaturas e rateios. | Planejada |

### Requisitos não funcionais

- **Desempenho:** O tempo de resposta das requisições da API REST não deve exceder 2 segundos em condições normais de uso, utilizando cache local de 1 hora para dados de câmbio externo.
- **Segurança:** Comunicação via HTTPS em produção, senhas criptografadas no banco de dados (`PBKDF2/Django`) e armazenamento seguro de credenciais e chaves via variáveis de ambiente.
- **Usabilidade:** Interface *web* responsiva, amigável e acessível, otimizada para navegação intuitiva em dispositivos móveis e *desktops*.
- **Disponibilidade:** Aplicação publicada no Render e acessível publicamente com taxa de disponibilidade (uptime) superior a 99% durante o período de avaliação.

---

## 3. Demonstração
> a preencher na Fase 2

---

## 4. Tecnologias utilizadas

| Camada | Tecnologia | Versão |
| --- | --- | --- |
| Linguagem | Python | 3.11+ |
| Backend | Django | 5.0+ |
| API REST | Django REST Framework | 3.14+ |
| Banco de dados | PostgreSQL (Produção) / SQLite (Desenvolvimento) | 16+ |
| Frontend | Templates Django + HTML5, CSS3, JavaScript (Bootstrap 5) | - |
| Testes | Pytest / Django Test Framework | 8.0+ |
| Infraestrutura | Render (Hospedagem) + GitHub Actions (CI/CD) | - |

---

## 5. Arquitetura

*O SubTracker adota uma arquitetura monolítica organizada em camadas bem definidas, promovendo a separação de responsabilidades, facilidade de manutenção e alinhamento com os princípios REST.*

```text
[Usuário] ──> [Frontend: Django Templates + JS] ──> [Backend: Django REST Framework] ──> [Banco de Dados: PostgreSQL]
                                                                  │
                                                                  ├──> [Cache: LocMemCache (Django)]
                                                                  └──> [API Externa: AwesomeAPI (Moedas)]
```

### Endpoints principais (API própria)
*Descritas no contrato inicial da API definido em `docs/api/`.*

| Método | Rota | Descrição |
| --- | --- | --- |
| `POST` | `/api/auth/register/` | Cadastro de novos usuários |
| `POST` | `/api/auth/login/` | Autenticação e geração de sessão/token |
| `GET` | `/api/subscriptions/` | Listar assinaturas do usuário autenticado (com busca e filtros) |
| `POST` | `/api/subscriptions/` | Criar nova assinatura |
| `GET` | `/api/subscriptions/{id}/` | Detalhar assinatura específica |
| `PUT` | `/api/subscriptions/{id}/` | Atualizar dados de uma assinatura |
| `DELETE` | `/api/subscriptions/{id}/` | Remover assinatura |
| `POST` | `/api/subscriptions/{id}/shares/` | Vincular pessoa e definir rateio/divisão de custo |
| `GET` | `/api/dashboard/summary/` | Retornar métricas financeiras consolidadas e cotações convertidas |

Documentação completa: [A documentação interativa com Swagger/ReDoc será disponibilizada na Fase 2 do projeto.]

---

## 6. Organização dos diretórios

```text

├── docs/
│   ├── api/
│   │   └── contrato-api.md
│   ├── integracao-externa/
│   │   └── plano-integracao-externa.md
│   ├── modelagem/
│   │   ├── arquitetura/
│   │   │   └── .gitkeep
│   │   ├── banco-de-dados/
│   │   │   ├── diagrama-er.pdf
│   │   │   └── modelo-logico.pdf
│   │   ├── casos-de-uso/
│   │   │   └── especificacoes-casos-de-uso.pdf
│   │   └── classes/
│   │       └── diagrama-de-classes.pdf
│   ├── planejamento/
│   │   └── .gitkeep
│   ├── prototipos/
│   │   └── prototipos-identidade-visual.md
│   └── seguranca/
│       └── .gitkeep
├── README.md

```

---

## 7. Participantes

| Nome | Matrícula | Função no projeto |
| --- | --- | --- |
| Gustavo Barbosa | [matrícula] | Liderança & Backend |
| Fred Gabriel | [matrícula] | Frontend & UI/UX |
| Lucas de Jesus | [matrícula] | Banco de Dados & Modelagem |
| Giovani Silva | [matrícula] | Testes & Documentação |

**Professor(a) responsável:** Felippe Pires Ferreira

---

## 8. Como executar
> a preencher na Fase 2

---

## 9. Configuração

| Variável | Obrigatória | Descrição | Exemplo |
| --- | --- | --- | --- |
| `SECRET_KEY` | Sim | Chave secreta de segurança do Django | `django-insecure-1234567890abcdef` |
| `DEBUG` | Sim | Modo de depuração (`True` em dev, `False` em produção) | `False` |
| `DATABASE_URL` | Sim | String de conexão com o banco de dados PostgreSQL | `postgresql://user:senha@host:5432/subtracker_db` |
| `ALLOWED_HOSTS` | Sim | Lista de domínios permitidos em produção | `subtracker.onrender.com,localhost,127.0.0.1` |
| `USD_DEFAULT` | Não | Valor padrão de emergência para conversão de Dólar (BRL) | `5.50` |
| `EUR_DEFAULT` | Não | Valor padrão de emergência para conversão de Euro (BRL) | `6.00` |

---

## 10. Testes
> a preencher na Fase 2

---

## 11. Uso de inteligência artificial

![Política de uso de IA — semáforo](images/semaforo.png)

### Declaração de uso

- **Houve uso de IA neste projeto?** Sim, a inteligência artificial foi utilizada pontualmente como ferramenta de apoio e consultoria técnica durante o planejamento e estruturação da documentação.
- **Ferramentas utilizadas:** Gemini e Claude.
- **Finalidade:** Esclarecimento de dúvidas técnicas sobre a sintaxe do Django, auxílio na formatação de tabelas e listas em Markdown e apoio na organização visual do documento README.md.
- **O que NÃO foi delegado à IA:** A concepção da ideia, a definição do problema, a regra de negócio do rateio de custos, o levantamento dos requisitos funcionais e não funcionais, a arquitetura do sistema e as decisões de modelagem de dados, todas elaboradas e validadas exclusivamente pelo grupo.

---

## 12. Contribuição e fluxo de trabalho

### Branches

- `main` — versão estável para avaliação
- `develop` — integração do grupo *(opcional)*
- `feat/[nome]` — nova funcionalidade
- `fix/[nome]` — correção de defeito
- `docs/[nome]` — alterações só de documentação

### Commits

Uso de mensagens curtas e no imperativo:

- `feat: adiciona cadastro de reservas`
- `fix: corrige validação de data`
- `docs: atualiza instruções de execução`

### Passos sugeridos

1. Criar uma branch a partir de `main`.
2. Implementar e testar localmente.
3. Abrir um *pull request* / *merge request* para revisão do grupo.
4. Só então integrar à branch principal.

**Issues e quadro de tarefas:** [link do GitHub Projects]

---

## 13. Histórico de versões

| Versão | Data | Descrição |
| --- | --- | --- |
| `0.1.0` | 03/10/2026 | Documentação inicial e especificação do projeto (Fase 1) |

---

## 14. Limitações e próximos passos

### Limitações Atuais
- **Fase Inicial de Planeamento:** A aplicação encontra-se na fase de especificação e modelação, sem código-fonte funcional implementado até ao momento[cite: 20].
- **Conversão Simples de Moeda:** A conversão contempla apenas cotações diretas para Real (BRL), dependendo da disponibilidade da API externa (AwesomeAPI).

### Próximos Passos (Fase 2)
- Implementar a estrutura base do projeto Django e configurar o banco de dados PostgreSQL[cite: 20].
- Desenvolver os modelos de dados (`User`, `Subscription`, `CostShare`) e as migrações iniciais.
- Criar os endpoints da API RESTful com autenticação e validações de negócio.
- Integrar a interface gráfica via Templates Django e Bootstrap para a gestão de assinaturas.
- Configurar o pipeline de CI/CD via GitHub Actions e realizar o deploy em produção no Render[cite: 20].

---

## 15. Licença, referências e contato

**Licença:** Uso exclusivamente acadêmico

### Documentação complementar

- **Índice da pasta `docs/`:** [`docs/README.pdf`](docs/README.pdf)
- **Casos de uso (diagrama + especificações):** [`docs/modelagem/casos-de-uso/especificacoes-casos-de-uso.pdf`](docs/modelagem/casos-de-uso/especificacoes-casos-de-uso.pdf)
- **Diagrama de classes:** [`docs/modelagem/classes/diagrama-de-classes.pdf`](docs/modelagem/classes/diagrama-de-classes.pdf)
- **Modelo conceitual (ER):** [`docs/modelagem/banco-de-dados/diagrama-er.pdf`](docs/modelagem/banco-de-dados/diagrama-er.pdf)
- **Modelo lógico:** [`docs/modelagem/banco-de-dados/modelo-logico.pdf`](docs/modelagem/banco-de-dados/modelo-logico.pdf)
- **Apresentação:** [`docs/apresentacao.pdf`](docs/)

### Referências

- **Django Software Foundation.** *Django documentation (v5.0).* Disponível em: <https://docs.djangoproject.com/>.
- **Django REST Framework.** *Django REST Framework documentation.* Disponível em: <https://www.django-rest-framework.org/>.
- **AwesomeAPI.** *API de Cotações de Moedas.* Disponível em: <https://docs.awesomeapi.com.br/api-de-moedas>.
- **Bootstrap.** *Bootstrap v5.3 Documentation.* Disponível em: <https://getbootstrap.com/docs/5.3/>.

### Contato

Dúvidas sobre o projeto: Abra uma *issue* no repositório GitHub do projeto.

**Agradecimentos:** Ao corpo docente, aos monitores da disciplina e ao UniCEUB pelo suporte acadêmico e fornecimento dos materiais de estudo.
