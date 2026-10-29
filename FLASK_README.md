# Interface Flask — Controle de Estoque

Interface web para o sistema de controle de estoque, usando as mesmas
conexões com Supabase e Redis do projeto original.

## Estrutura adicionada

```
controle_estoque/
├── src/
│   └── app.py              ← servidor Flask (novo)
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── produtos.html
│   ├── produto_form.html
│   ├── relatorio.html      ← VIEW
│   ├── calcular.html       ← FUNCTION
│   ├── movimentacao.html   ← PROCEDURE
│   └── historico.html
└── requirements.txt
```

## Como rodar

1. Instalar dependências:
```
pip install -r requirements.txt
```

2. Garantir que o `.env` existe na raiz com:
```
SUPABASE_URL=...
SUPABASE_KEY=...
REDIS_HOST=...
REDIS_PORT=6379
REDIS_USERNAME=default
REDIS_PASSWORD=...
```

3. Iniciar o servidor Flask:
```
python src/app.py
```

4. Acessar no navegador:
```
http://localhost:5000
```
