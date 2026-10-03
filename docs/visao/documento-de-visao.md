# Documento de Visão — SubTracker

## 1. Contexto e Problema

Hoje em dia a gente vive cercado de assinatura. É streaming, nuvem, academia, aplicativo de trabalho... Quando você vai ver, tem dezenas de cobranças caindo todo mês no cartão no automático e você nem percebe.
Além disso, é super comum o pessoal dividir plano familiar ou custos de moradia entre amigos e colegas de quarto. A real necessidade do SubTracker aparece exatamente quando a fatura chega no fim do mês.
Uma lista gigante de pequenos débitos automáticos picados em várias datas e moedas diferentes, deixando qualquer um perdido sem saber pra onde o dinheiro está indo.

Percebemos que o problema principal não é só o valor total da conta, mas sim a bagunça na hora de acompanhar esses gastos. Na prática, o usuário esbarra em quatro dificuldades principais:

- **Esquecimento e renovações indesejadas:** o usuário assina um período de teste (free trial) ou um serviço temporário, esquece de cancelar a tempo e é cobrado automaticamente.
- **Acúmulo de cobranças invisíveis:** várias assinaturas pequenas de R$ 15 a R$ 40 que, somadas, pesam o orçamento mensal sem que a pessoa perceba.
- **Falta de controle na divisão de contas:** dificuldade e atrito na hora de lembrar e cobrar quem divide o plano familiar (ex: ter que cobrar R$ 10 todo mês dos amigos).
- **Oscilação de câmbio em serviços internacionais:** cobranças em dólares ou euros (como plataformas de dev, jogos ou ferramentas de IA) que pegam o usuário de surpresa na fatura por causa da variação do câmbio e das taxas de IOF.

## 2. Justificativa

Vale a pena resolver esse problema porque ele afeta diretamente a saúde financeira e a organização pessoal dos usuários. Sem uma ferramenta dedicada como o SubTracker, o custo é sempre ser pego de surpresa no fim do mês: as pessoas continuam pagando por serviços que não utilizam mais simplesmente porque esqueceram da existência deles ou perderam o dia exato da renovação. Além disso, o usuário perde tempo tentando controlar isso em planilhas manuais e ultrapassadas que rapidamente ficam desatualizadas. O SubTracker surge para centralizar, automatizar alertas visuais de vencimento, calcular gastos futuros acumulados e garantir que o usuário retome o controle total sobre suas finanças recorrentes de forma simples e intuitiva.

## 3. Objetivos

### Objetivo Geral

Desenvolver uma aplicação web para centralizar, gerenciar e dar visibilidade aos gastos com assinaturas e serviços recorrentes, permitindo que o usuário controle prazos, valores e divisões de custos em um só lugar.

### Objetivos Específicos

- **Gestão Centralizada de Assinaturas:** permitir o cadastro, edição e cancelamento (CRUD) de serviços recorrentes, registrando dados como valor, ciclo de cobrança (mensal/anual), categoria e data de vencimento.
- **Alertas Visuais no Dashboard** *(dor: esquecimento)*: exibir alertas destacados no painel principal indicando assinaturas com vencimento nos próximos dias e períodos de teste (free trial) prestes a expirar.
- **Visão Geral e Totalizadores** *(dor: acúmulo invisível)*: Uma tela principal que mostra o gasto mensal e anual em um só lugar, permitindo enxergar exatamente para onde o dinheiro está indo.
- **Divisão de Custos com Terceiros** *(dor: divisão de contas)*: permitir o vínculo de outras pessoas a uma assinatura cadastrada, calculando automaticamente a parte de cada um para facilitar o controle de pagamentos compartilhados.
- **Suporte a Múltiplas Moedas** *(dor: oscilação de câmbio)*: permitir o cadastro de assinaturas internacionais em moedas estrangeiras (como USD), consultando uma API externa de câmbio para obter o valor atual aproximado em BRL no momento da visualização.

## 4. Público-Alvo

- **Estudantes e Jovens Adultos:** pessoas que utilizam vários serviços digitais (streaming, estudos, ferramentas) e compartilham assinaturas familiares e despesas de moradia com amigos.
- **Profissionais e Freelancers:** usuários que mantêm assinaturas de softwares e ferramentas de trabalho recorrentes (SaaS, armazenamento em nuvem, ferramentas de IA).

## 5. Stakeholders

- **Equipe de Desenvolvimento (Grupo do Projeto):** responsável por planejar, projetar, codificar e testar a aplicação web, incluindo as tarefas de administração e manutenção da plataforma.
- **Professor/Avaliador:** responsável por orientar, avaliar os entregáveis acadêmicos, a arquitetura da aplicação e o cumprimento do escopo do projeto.

## 6. Escopo

### Dentro do Escopo

- **Autenticação e Gestão de Usuários:** cadastro, login, logout e gerenciamento de perfil do usuário.
- **Gestão de Assinaturas (CRUD Completo):** cadastro, visualização, edição e exclusão de assinaturas e gastos recorrentes (nome, valor, moeda, ciclo de cobrança, categoria, data de vencimento e status).
- **Dashboard Financeiro e Alertas Visuais:** painel principal apresentando o valor total consolidado dos gastos (mensal/anual), total por categoria e destaques visuais para renovações próximas e prazos de teste (free trial) a vencer.
- **Divisão Simples de Custos:** funcionalidade para vincular nome/e-mail de terceiros à assinatura e calcular a parte individualmente de cada pessoa (controle apenas informativo de quem divide a conta).
- **Conversão Estimada de Câmbio:** suporte ao cadastro em moeda estrangeira (ex: USD), consultando uma API externa de cotação para obter o valor atual aproximado em BRL(REAL) no momento da visualização da assinatura, sem histórico.
- **Busca, Filtros e Relatório:** consulta de assinaturas por nome, status ou categoria, além da geração/exibição de relatórios demonstrativos de gastos.
- **API REST Própria:** endpoints REST para consulta e consumo dos dados das assinaturas e totais.

### Fora do Escopo

- **Processamento de Pagamentos e Gateway:** não haverá integração com sistemas financeiros (PagSeguro, Mercado Pago, PIX) para realizar pagamentos ou transferências reais entre usuários.
- **Envio Automático de E-mails/Push Notifications:** não haverá disparo externo de mensagens (os alertas de vencimento serão estritamente visuais na tela do dashboard).
- **Leitura Automática de Faturas/Open Finance:** não haverá importação automática de dados via leitura de e-mails, PDF de faturas ou APIs bancárias.
- **Histórico/Gráfico de Variação Cambial:** não haverá histórico ou gráfico de oscilação de moedas ao longo do tempo. Apenas a cotação estimada no momento da consulta.
- **Aplicativo Mobile Nativo:** a aplicação será exclusivamente responsiva (acessível via navegadores em desktops e dispositivos móveis).
- **Múltiplos Workspaces/Organizações:** a plataforma será focada na gestão individual do usuário e seus vínculos diretos de divisão de contas, sem separação por empresas ou equipes independentes.

## 7. Restrições

- **Tecnológicas:**
  - Desenvolvimento obrigatório utilizando Python com o framework Django e Django REST Framework (DRF) para a API REST própria.
  - Utilização de banco de dados relacional (SQLite para ambiente de desenvolvimento local e PostgreSQL para produção/hospedagem).
  - Uso de serviços de hospedagem web gratuitos (como Render ou Railway) para deploy do projeto sem custos financeiros adicionais para o grupo.
- **De Prazo e Regras:**
  - Prazos de entrega fixos e não negociáveis estabelecidos pelo calendário acadêmico para as entregas da Fase 1 (Documentação/Arquitetura) e Fase 2 (Implementação/Deploy/Apresentação).
- **De Equipe:**
  - Disponibilidade de desenvolvimento limitada à carga horária e horários livres dos integrantes do grupo ao longo do semestre letivo.
- **Acadêmicas/Institucionais:**
  - Repositório deve seguir o template oficial fornecido pelo professor, documentação deve ser versionada publicamente no GitHub, segredos e credenciais não podem ser versionados (devem ser fornecidos via variáveis de ambiente).

## 8. Premissas

- **Disponibilidade da API Externa:** assume-se que a API pública de cotação de moedas (ex: AwesomeAPI) permanecerá gratuita, estável e acessível via HTTPS durante o ciclo de desenvolvimento e apresentação do projeto.
- **Acesso do Usuário:** assume-se que os usuários finais possuem conexão com a internet e utilizam navegadores web modernos com suporte a JavaScript (Google Chrome, Firefox, Edge, Safari).
- **Dados Fictícios de Teste:** assume-se que os dados cadastrados na aplicação durante os testes e demonstrações serão fictícios ou inseridos manualmente pelos próprios usuários para fins de avaliação.

## 9. Riscos Iniciais e Ações de Mitigação

1. **Risco Técnico — Indisponibilidade ou oscilação da API externa de câmbio**
   - *Impacto:* erro ou lentidão ao carregar as assinaturas que dependem de conversão em moeda estrangeira.
   - *Mitigação:* implementar tratamento de exceções (try/except) nas chamadas HTTP com um valor de câmbio fallback (cotação padrão pré-definida) caso a API externa não responda a tempo.
2. **Risco de Escopo — Aumento indevido do escopo (Scope Creep)**
   - *Impacto:* tentativa de adicionar funcionalidades complexas (ex: envio de e-mails, gráficos temporais) comprometendo o prazo de entrega.
   - *Mitigação:* manter rigorosamente os limites definidos na seção "Fora do Escopo" e registrar ideias extras apenas na seção de melhorias futuras (Roadmap).
3. **Risco de Equipe — Desalinhamento na divisão de tarefas ou atraso em entregas individuais**
   - *Impacto:* acúmulo de tarefas na reta final das entregas das fases do projeto.
   - *Mitigação:* realizar reuniões semanais de alinhamento, utilizar um quadro Kanban (como GitHub Projects) para acompanhamento transparente das tarefas e definir prazos internos anteriores à data limite do professor.

## 10. Critérios de Sucesso

### Critérios Acadêmicos e Técnicos

- **Deploy e Acessibilidade:** aplicação web publicada em servidor de hospedagem (ex: Render/Railway) e acessível publicamente via HTTPS até a data final da apresentação.
- **API REST Própria:** endpoints REST próprios (Django REST Framework) respondendo corretamente às requisições com os códigos de status HTTP adequados (ex: `200 OK`, `201 Created`, `400 Bad Request`, `404 Not Found`).
- **Consumo de API Externa e Resiliência:** integração funcional com a API de câmbio (ex: AwesomeAPI) para buscar cotações em tempo real ao carregar a página, possuindo tratamento de erros e valor de fallback para evitar a queda da aplicação em caso de indisponibilidade externa.
- **Análise de Segurança (SAST/DAST):** execução e documentação das etapas de análise estática e dinâmica de segurança conforme exigido na especificação do projeto.
- **Qualidade de Código e Repositório:** repositório no GitHub estruturado segundo o template fornecido, sem exposição de credenciais ou segredos em código público (utilização estrita de `.env`).

### Critérios Funcionais e de Produto

- **Fluxo de Gestão de Assinaturas (CRUD Completo):** usuário consegue cadastrar, visualizar, editar, filtrar e excluir uma assinatura, com as mudanças aparecendo na hora na tela.
- **Consolidação Financeira no Dashboard:** cálculo automático e correto do valor total gasto no mês e no ano no painel principal, incluindo o somatório de diferentes categorias.
- **Visibilidade de Vencimentos e Testes:** destaque visual claro no dashboard para assinaturas com vencimento nos próximos 7 dias e alertas para períodos de teste (free trial) prestes a expirar.
- **Divisão Transparente de Custos:** ao vincular terceiros a uma assinatura, a plataforma calcula e exibe de forma precisa a parte individual de cada participante.
- **Relatório Demonstrativo:** geração e visualização de relatório demonstrativo de gastos com dados filtrados por categoria ou período.

