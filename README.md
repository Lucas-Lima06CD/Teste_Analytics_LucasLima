# Teste_Analytics_Lucas_Lima

Repositório da entrega do **Teste para Estagiário de Analytics**.

## Estrutura do repositório

```
Teste_Analytics_Lucas_Lima/
├── data/
│   └── vendas_simuladas.csv
├── docs/
│   └── respostas.md
├── scripts/
│   └── simulate_and_analyze.py
└── README.md
```

## Como executar

Pré-requisitos:

- Python 3.9+
- `pip`

Passos:

```bash
# 1) Crie e ative um ambiente (opcional, mas recomendado)
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# 2) Instale as dependências
pip install -r requirements.txt

# 3) Rode o script principal
python scripts/simulate_and_analyze.py
```

O script irá:
- Ler `data/vendas_simuladas.csv` (ou gerar um novo dataset caso você apague o existente);
- Calcular métricas simples (total de vendas por produto e por mês);
- Salvar saídas em `data/` como CSVs e exibir um sumário no console.

## Dependências

As dependências estão listadas em `requirements.txt`:
- pandas

## Suposições documentadas

- Dados simulados representam vendas diárias de um hortifruti entre janeiro e junho de 2024.
- Preços foram gerados aleatoriamente dentro de um intervalo plausível para varejo alimentar local (R$ 2,00 a R$ 9,00).
- Categorias foram definidas manualmente apenas para exemplificação.
- Não há sazonalidade complexa modelada; pequenas variações são impostas via aleatoriedade.
- Não existem devoluções, rupturas de estoque ou promoções explícitas no dataset base.

Caso novas suposições sejam feitas durante análises futuras, elas devem ser adicionadas aqui.

## Reproduzibilidade

- Semente aleatória (`random.seed(42)`) é definida no gerador de dados para permitir reprodutibilidade.
- Os scripts não dependem de credenciais, API externas ou arquivos fora do repositório.

## Autor

- **Lucas Lima**
- Contato: _adicione aqui seu e-mail ou LinkedIn, se desejar_
