# Plano de Integração Externa

## 1. API Escolhida e Finalidade

- **API Externa:** AwesomeAPI (Economia / Cotação de Moedas).
- **Finalidade:** Obter as taxas de câmbio atualizadas de moedas estrangeiras (USD e EUR) em relação ao Real (BRL). Essa integração permite que o SubTracker converta e mostre em tempo real o valor total das assinaturas internacionais cadastradas pelo utilizador em Reais (R$), no Dashboard e nos relatórios de gastos (UC08 e UC10).

## 2. Endpoints Consumidos e Parâmetros

- **Método HTTP:** `GET`
- **URL / Endpoint:** `https://economia.awesomeapi.com.br/json/last/{MOEDA_ORIGEM}-{MOEDA_DESTINO}`
- **Exemplo de chamada múltipla (USD e EUR para BRL):**
  ```
  GET https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL
  ```
- **Moedas suportadas:** `USD` (Dólar Americano) e `EUR` (Euro), alinhadas ao domínio de `moeda` definido no Modelo de Dados.

## 3. Estrutura dos Dados Utilizados

- **Campo utilizado como cotação:** `bid` (preço de compra) — indicador mais adequado para estimar a conversão em Reais das assinaturas em moeda estrangeira.

**Estrutura de resposta mapeada:**
```json
{
  "USDBRL": {
    "code": "USD",
    "codein": "BRL",
    "name": "Dólar Americano/Real Brasileiro",
    "bid": "5.5042",
    "ask": "5.5058",
    "timestamp": "1728000000",
    "create_date": "2026-10-03 21:00:00"
  },
  "EURBRL": {
    "code": "EUR",
    "codein": "BRL",
    "name": "Euro/Real Brasileiro",
    "bid": "6.0215",
    "ask": "6.0230",
    "timestamp": "1728000000",
    "create_date": "2026-10-03 21:00:00"
  }
}
```

## 4. Autenticação, Limites e Estratégia de Cache

- **Autenticação:** não exige chave de API (endpoint público).
- **Limites de uso (rate limit):** a versão gratuita da AwesomeAPI impõe um limite de requisições por minuto, cujo valor exato deve ser confirmado em https://awesomeapi.com.br antes da entrega final, já que pode ser atualizado pelo provedor.
- **Estratégia de frequência e caching (otimização):**
  - Para evitar estouro do rate limit e reduzir a latência nos carregamentos do Dashboard, o backend Django utiliza o **cache em memória do próprio processo (`LocMemCache`)**, nativo do framework, com expiração de 1 hora — sem necessidade de serviço de infraestrutura adicional (ex: Redis).
  - Quando o utilizador acede ao Dashboard (UC08/UC10), o serviço `ExchangeRateService` verifica primeiro o cache:
    - **Cache Miss:** realiza a requisição `GET` à AwesomeAPI, atualiza o cache e retorna a cotação.
    - **Cache Hit:** retorna o valor em cache instantaneamente, dispensando chamadas HTTP externas desnecessárias.

## 5. Tratamento de Indisponibilidade e Timeout (Fallback)

Para assegurar a resiliência do sistema caso a AwesomeAPI esteja inacessível, apresente falha de rede ou atinja o rate limit, o serviço implementa o seguinte fluxo de contingência:

1. **Timeout HTTP definitivo:** a requisição HTTP externa possui um tempo limite estrito de 3 segundos.
2. **Estratégia de fallback dinâmico:**
   - **Nível 1 (última cotação em cache):** se a API falhar ou der timeout, o sistema utiliza o valor mais recente ainda presente no `LocMemCache` (mesmo que tecnicamente expirado), evitando nova chamada HTTP até a próxima tentativa bem-sucedida.
   - **Nível 2 (cotação estática de emergência):** se não houver nenhum valor em cache (ex: aplicação recém-reiniciada), o sistema utiliza um valor pré-configurado de segurança nas variáveis de ambiente (`USD_DEFAULT=5.50` e `EUR_DEFAULT=6.00`).
3. **Log de auditoria:** erros de comunicação são registados nos logs do servidor (`logger.error`) para monitorização da infraestrutura, sem interromper a navegação nem apresentar erros 500 ao utilizador final.

## 6. Referências da Documentação Oficial

- Documentação técnica da API: https://docs.awesomeapi.com.br/api-de-moedas
- Portal da API: https://awesomeapi.com.br
