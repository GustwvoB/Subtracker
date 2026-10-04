# Protótipos e Identidade Visual — SubTracker

## 1. Nome do Projeto e Proposta Visual

- **Nome Oficial:** SubTracker.
- **Proposta Visual:** Dashboard Clean & Tech SaaS. A interface prioriza o minimalismo funcional com fundo claro (para legibilidade no dia a dia), cartões de resumo com cantos suavemente arredondados, contrastes marcantes nos call-to-actions (CTAs) e gráficos limpos para visualização rápida de custos e vencimentos.
- **Ferramenta de Prototipagem:** Figma.

## 2. Paleta de Cores

A paleta combina o Roxo/Violeta (tecnologia, gestão moderna de SaaS/assinaturas) com o Azul Profundo (confiança e estabilidade financeira), complementada por tons neutros e cores de feedback operacional.

| Aplicação / Função | Nome da Cor | Código Hex | Descrição / Uso |
| --- | --- | --- | --- |
| Primária (Marca/Destaque) | Roxo SaaS (Electric Purple) | `#6C5CE7` | Botões principais, links ativos, elementos em foco. |
| Secundária (Apoio) | Azul Finanças (Deep Navy) | `#2D3436` | Títulos, cabeçalhos de tabelas, elementos institucionais. |
| Fundo de Tela (Background) | Cinza Claro (Soft Background) | `#F8F9FA` | Fundo geral da aplicação (reduz fadiga visual). |
| Superfície / Cartões | Branco Puro (Card Surface) | `#FFFFFF` | Fundo dos cards do Dashboard, modais e tabelas. |
| Texto Principal | Grafite Escuro (Dark Neutral) | `#1E293B` | Textos de corpo, rótulos e valores principais. |
| Alerta / Próximo Vencimento | Laranja Alerta (Warning Orange) | `#E17055` | Notificação de assinaturas prestes a vencer. |
| Sucesso / Status Ativo | Verde Concluído (Success Green) | `#00B894` | Status de assinaturas ativas, badge de pago. |

## 3. Tipografia

Utilização do ecossistema gratuito Google Fonts, garantindo alta legibilidade e suporte nativo em navegadores web e ferramentas de prototipagem como Figma.

- **Fonte Primária (Títulos e Destaques):** `Poppins` (Semibold / Bold)
  - Aplicação: Títulos de páginas (H1, H2), numéricos de destaques no Dashboard (métricas financeiras) e botões de ação principal.
- **Fonte Secundária (Texto de Corpo e Tabelas):** `Inter` (Regular / Medium)
  - Aplicação: Formulários, dados de tabelas, rótulos de filtros, menus laterais e descrições.

## 4. Logotipo e Assinatura Visual

- **Conceito da Marca:** um símbolo minimalista composto pela sobreposição de dois cartões/camadas estilizadas (representando a gestão de assinaturas recorrentes) formando a letra "S", acompanhado do logotipo em texto (`Poppins Bold`).
- **Variantes de Aplicação:**
  1. **Principal (Horizontal):** ícone em Roxo (`#6C5CE7`) + texto "Sub" em Grafite Escuro (`#1E293B`) e "Tracker" em Roxo (`#6C5CE7`). Utilizado na barra de navegação superior/lateral.
  2. **Monocromática:** versão em Branco Puro (`#FFFFFF`) para aplicação sobre fundos escuros ou cabeçalhos contrastantes.
  3. **Favicon / Ícone Simplificado:** apenas o símbolo estilizado em "S" para abas do navegador e ícones de atalho.

## 5. Mapeamento dos Protótipos de Telas Essenciais

Para contemplar os fluxos centrais do sistema, definiu-se a prototipagem interativa no Figma das 5 telas centrais:

1. **Tela 1 — Autenticação (Login e Cadastro / UC01 e UC02):**
   Layout centralizado com formulário limpo, campos para e-mail/senha, validações visuais de erro e botão de ação primário em Roxo (`#6C5CE7`).

2. **Tela 2 — Dashboard Principal (Visão Geral Financeira / UC08):**
   Cards no topo com o total gasto no mês (R$), total de assinaturas ativas e conversão automatizada de moedas estrangeiras em Reais (USD/EUR). Gráfico de gastos por categoria e lista das próximas assinaturas com vencimento iminente.

3. **Tela 3 — Gerenciamento de Assinaturas (Listagem e Busca / UC07):**
   Tabela organizada contendo ícone do serviço, nome da assinatura, valor, moeda, categoria, data de vencimento e status. Barra de pesquisa em tempo real e filtros dinâmicos por categoria/status.

4. **Tela 4 — Formulário de Cadastro/Edição de Assinatura (UC04 e UC05):**
   Modal ou tela dedicada com campos estruturados: Nome do serviço, Categoria (Select), Valor, Moeda (`BRL`, `USD`, `EUR`), Ciclo de Cobrança (Mensal/Anual) e Data de Vencimento.

5. **Tela 5 — Divisão de Custos / Pessoas Vinculadas (UC09):**
   Interface visual permitindo selecionar uma assinatura (ex: Netflix Family) e cadastrar/vincular pessoas, com a cota-parte calculada e exibida automaticamente para cada participante.
