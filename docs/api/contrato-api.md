# Contrato Inicial da API — SubTracker

## 1. Visão Geral e Diretrizes de Design

- **Base URL:** `/api/v1/`
- **Formato de Dados:** JSON (`application/json`)
- **Mecanismo de Autenticação:** `TokenAuthentication` do Django REST Framework via Header HTTP `Authorization: Token <token_key>`.
- **Padrão de Serialização de Relacionamentos (DRF):**
  - **Leitura (`GET`):** relacionamentos (ex: `categoria`) são expandidos como objetos estruturados para facilitar o consumo pelo cliente frontend sem necessidade de requisições adicionais. troque a palavra aninhados
  - **Escrita (`POST`/`PUT`):** os relacionamentos aceitam apenas o ID da chave primária (ex: `id_categoria: 1`).
- **Cálculo de Cota-Parte:** o campo `percentual_cota` da divisão de custos é calculado automaticamente pelo backend (100 ÷ número de pessoas vinculadas à assinatura, incluindo o próprio usuário dono), sendo recalculado a cada inclusão ou remoção de participante. Não é um campo aceito em requisições de escrita.
- **Tratamento de Segurança:** tentativas de acesso a recursos de outros utilizadores retornam código `404 Not Found` em vez de `403 Forbidden`, para evitar confusão de dados.
- **Padrão de Respostas de Erro:**
  ```json
  { "detail": "Mensagem explicativa do erro ou campos inválidos." }
  ```

## 2. Tabela Resumo dos Endpoints Expostos

| Recurso | Método HTTP | Endpoint | Descrição / Caso de Uso Relacionado | Autenticação |
| --- | --- | --- | --- | --- |
| Autenticação | POST | `/api/v1/auth/token/` | Autentica o utilizador e retorna o Token de Acesso. | Nenhuma |
| Assinaturas | GET | `/api/v1/assinaturas/` | Lista as assinaturas do utilizador (busca, paginação e filtros por categoria/moeda). | Token |
| Assinaturas | POST | `/api/v1/assinaturas/` | Cadastra uma nova assinatura (UC04). | Token |
| Assinaturas | GET | `/api/v1/assinaturas/{id}/` | Detalha uma assinatura específica com objetos expandidos. | Token |
| Assinaturas | PUT | `/api/v1/assinaturas/{id}/` | Atualiza uma assinatura existente (UC05). | Token |
| Assinaturas | DELETE | `/api/v1/assinaturas/{id}/` | Remove uma assinatura do sistema via exclusão física (UC06). | Token |
| Divisão de Custos | POST | `/api/v1/assinaturas/{id}/divisoes/` | Vincula uma pessoa cadastrada à assinatura; cota-parte calculada automaticamente (UC09). | Token |
| Divisão de Custos | DELETE | `/api/v1/assinaturas/{id}/divisoes/{id_divisao}/` | Remove o vínculo de divisão de custos entre uma pessoa e a assinatura (UC09). | Token |
| Categorias | GET | `/api/v1/categorias/` | Lista as categorias disponíveis no sistema. | Token |
| Pessoas Vinculadas | GET | `/api/v1/pessoas-vinculadas/` | Lista os contactos/pessoas vinculadas criados pelo utilizador. | Token |
| Pessoas Vinculadas | POST | `/api/v1/pessoas-vinculadas/` | Cadastra uma nova pessoa vinculada à conta do utilizador. | Token |
| Dashboard / Totais | GET | `/api/v1/dashboard/resumo/` | Retorna os indicadores consolidados de gastos do utilizador (UC08). | Token |

## 3. Detalhamento dos Endpoints e Exemplos JSON

### 3.1. Autenticação — Obtenção de Token

- **Endpoint:** `POST /api/v1/auth/token/`
- **Autenticação:** Nenhuma (Pública).

**Requisição**
```json
{
  "username": "gustavo@email.com",
  "password": "senhaSegura123"
}
```

**Resposta de Sucesso (`200 OK`)**
```json
{
  "token": "9944b09199c62bcf9418ad846d0e4e2c6ac22242"
}
```

### 3.2. Listar Assinaturas (Leitura com Objetos Expandidos)

- **Endpoint:** `GET /api/v1/assinaturas/`
- **Autenticação:** Requer Token (`Authorization: Token 9944b0...`).
- **Parâmetros Query String (opcionais):** `?categoria=1`, `?moeda=USD`, `?search=Netflix`, `?page=1`.

**Resposta de Sucesso (`200 OK`)**
```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id_assinatura": 12,
      "nome_servico": "Netflix",
      "valor": "55.90",
      "moeda": "BRL",
      "ciclo_cobranca": "MENSAL",
      "data_vencimento": "2026-10-15",
      "eh_free_trial": false,
      "data_limite_trial": null,
      "categoria": {
        "id_categoria": 1,
        "nome": "Streaming"
      },
      "pessoas_divisao": [
        {
          "id_divisao": 5,
          "id_pessoa": 3,
          "nome": "Lucas Silva",
          "percentual_cota": "50.00"
        }
      ]
    }
  ]
}
```

### 3.3. Cadastrar Assinatura (Escrita com ID Referencial)

- **Endpoint:** `POST /api/v1/assinaturas/`
- **Autenticação:** Requer Token.

**Requisição**
```json
{
  "id_categoria": 1,
  "nome_servico": "Spotify Premium",
  "valor": 21.90,
  "moeda": "BRL",
  "ciclo_cobranca": "MENSAL",
  "data_vencimento": "2026-10-20",
  "eh_free_trial": false
}
```

**Resposta de Sucesso (`201 Created`)**
```json
{
  "id_assinatura": 13,
  "id_categoria": 1,
  "nome_servico": "Spotify Premium",
  "valor": "21.90",
  "moeda": "BRL",
  "ciclo_cobranca": "MENSAL",
  "data_vencimento": "2026-10-20",
  "eh_free_trial": false,
  "data_limite_trial": null
}
```

### 3.4. Vincular Pessoa a uma Assinatura (UC09 — Divisão de Custos)

- **Endpoint:** `POST /api/v1/assinaturas/{id}/divisoes/`
- **Autenticação:** Requer Token.
- **Observação:** o campo `percentual_cota` não é enviado pelo cliente — o backend calcula automaticamente a parte igual entre todos os participantes vinculados à assinatura.

**Requisição**
```json
{
  "id_pessoa": 3,
  "tipo_divisao": "IGUALITARIA"
}
```

**Resposta de Sucesso (`201 Created`)**
```json
{
  "id_divisao": 5,
  "id_assinatura": 12,
  "id_pessoa": 3,
  "tipo_divisao": "IGUALITARIA",
  "percentual_cota": "50.00"
}
```

### 3.5. Remover Vínculo de Divisão de Custos

- **Endpoint:** `DELETE /api/v1/assinaturas/{id}/divisoes/{id_divisao}/`
- **Autenticação:** Requer Token.
- **Resposta de Sucesso:** `204 No Content`

### 3.6. Resumo do Dashboard (UC08)

- **Endpoint:** `GET /api/v1/dashboard/resumo/`
- **Autenticação:** Requer Token.

**Resposta de Sucesso (`200 OK`)**
```json
{
  "total_gastos_mensal_brl": "145.80",
  "total_assinaturas_ativas": 4,
  "proximos_vencimentos": [
    {
      "id_assinatura": 12,
      "nome_servico": "Netflix",
      "data_vencimento": "2026-10-15",
      "valor_em_brl": "55.90"
    }
  ]
}
```

## 4. Tabela de Códigos de Status HTTP Utilizados

| Código Status | Significado | Aplicação na API |
| --- | --- | --- |
| `200 OK` | Sucesso | Retornado em consultas (`GET`), atualizações (`PUT`) e autenticação aceita. |
| `201 Created` | Criado | Retornado após o cadastro bem-sucedido de novos recursos (`POST`). |
| `204 No Content` | Sem Conteúdo | Retornado após a exclusão de um recurso ou vínculo (`DELETE`). |
| `400 Bad Request` | Requisição Inválida | Falhas de validação nos dados enviados (ex: `valor <= 0`). |
| `401 Unauthorized` | Não Autorizado | Token ausente, expirado ou inválido no cabeçalho HTTP. |
| `404 Not Found` | Não Encontrado | Recurso inexistente ou pertencente a outro utilizador. |

## 5. Escopo Deliberado

- O **relatório de gastos (UC11)** é disponibilizado apenas pela interface web, não possuindo endpoint próprio na API REST — decisão consciente do grupo para manter a API focada nos dados estruturados do dashboard/resumo.
