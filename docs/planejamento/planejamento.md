# Planejamento

## 1. Integrantes e Responsabilidades (por Camada Técnica)

| Integrante | Camada Técnica / Responsabilidade | Principais Entregáveis |
| --- | --- | --- |
| Gustavo Oliveira | Liderança & Backend/Integrações | Configuração do Django, modelos de dados (Models), integração com a AwesomeAPI (ExchangeRateService + Cache) e deploy no Render. |
| Membro 2 | Frontend & UI/UX | Templates HTML5/Bootstrap 5, responsividade, componentes visuais das 5 telas e integração com as views do Django. |
| Membro 3 | API REST & Regras de Negócio | Endpoints no Django REST Framework (DRF), autenticação por Token, validações do rateio (Opção A) e serializadores. |
| Membro 4 | Segurança, Testes & QA | Testes unitários/integração (pytest/unittest), relatórios de análise estática/dinâmica (SAST/DAST) e documentação final. |

## 2. Cronograma e Marcos (Milestones)

- **Fase 1 (Especificação e Documentação):** 05/10/2026
- **Fase 2 (Desenvolvimento e Entrega Final):** 30/11/2026

```
[05/10] Fase 1 ──> [Sprint 1: Core & Models] ──> [Sprint 2: Views & Templates] ──> [Sprint 3: API REST & Rateio] ──> [Sprint 4: Security & Deploy] ──> [30/11] Entrega Final
```

| Marco / Milestone | Período / Data Limite | Foco de Entrega |
| --- | --- | --- |
| Marco 1: Setup & Core Data | 06/10 a 19/10/2026 | Repositório estruturado, Django configurado, Models criados e banco PostgreSQL ativo. |
| Marco 2: Interface & CRUDs | 20/10 a 02/11/2026 | Interface web funcional (Dashboard, telas de listagem, cadastro e autenticação). |
| Marco 3: API REST & Regras Avançadas | 03/11 a 16/11/2026 | Endpoints DRF, regras automáticas de rateio de custos e integração com AwesomeAPI. |
| Marco 4: Segurança, Deploy & QA | 17/11 a 27/11/2026 | Suíte de testes aprovada, varredura SAST/DAST concluída e deploy ativo no Render. |
| Marco Final: Apresentação | 28/11 a 30/11/2026 | Validação do checklist final e preparação do material de apresentação. |

## 3. Backlog / Lista de Tarefas (Fase 2)

1. **Configuração Inicial:** setup do projeto Django, ficheiro `.env` e ligação ao PostgreSQL.
2. **Modelagem de Dados:** criação das entidades `Usuario`, `Categoria`, `Assinatura`, `PessoaVinculada` e `DivisaoAssinatura` com migrações.
3. **Autenticação de Usuários:** fluxos de registo, login, logout e controlo de acesso.
4. **CRUD de Assinaturas:** formulários e telas de gestão de assinaturas recorrentes.
5. **Integração Câmbio (AwesomeAPI):** serviço de consulta com fallback e `LocMemCache` (1 hora).
6. **Módulo de Rateio de Custos:** funcionalidade de vinculação de pessoas e cálculo automatizado de frações de custo.
7. **Dashboard Financeiro:** totais consolidados, conversão visual BRL e alertas de vencimento.
8. **API REST própria:** serializadores, autenticação Token e documentação interativa.
9. **Testes & Qualidade:** testes de modelos, visões e endpoints de API.
10. **Segurança & Deploy:** execução de relatórios SAST/DAST e implantação no Render.

## 4. Estratégia de Execução e Comunicação

- **Metodologia:** Kanban adaptado através do GitHub Projects, com colunas `Backlog`, `In Progress`, `Review/PR` e `Done`.
- **Controlo de Código (Git):** padrão GitFlow simples com branch `main` protegida, desenvolvimento em branches por funcionalidade (`feat/...`) e necessidade de pelo menos 1 aprovação via Pull Request.

## 5. Matriz de Gestão de Riscos

| Risco Mapeado | Impacto | Mitigação / Plano de Ação | Responsável pelo Monitoramento |
| --- | --- | --- | --- |
| Indisponibilidade da API de Cotação | Alto | Utilização do `LocMemCache` interno e variáveis estáticas de fallback (`USD_DEFAULT`/`EUR_DEFAULT`). | Gustavo Oliveira |
| Atrasos na Integração Frontend/Backend | Médio | Contrato de API bem definido antecipadamente na Fase 1. | Fred Gabriel |
| Atraso no Deploy / Instabilidade no Render | Médio | Configuração do ambiente no Render realizada no início do Marco 4 (com antecedência). | Lucas de Jesus |
| Conflitos de Versão no Git | Baixo | Divisão estrita por camadas técnicas e obrigatoriedade de Pull Requests isolados. | Giovani Silva |
