# Guia Rápido de Execução

## Passo a Passo Completo

### 1. Instalar Python

Certifique-se de ter Python 3.8+ instalado:

```bash
python --version
```

### 2. Criar ambiente virtual

```bash
# Windows PowerShell
python -m venv venv
.\venv\Scripts\Activate.ps1

# Windows CMD
python -m venv venv
.\venv\Scripts\activate.bat

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Instalar navegadores Playwright

```bash
playwright install chromium
```

### 5. Executar todos os testes

```bash
pytest
```

### 6. Executar com relatório HTML

```bash
pytest --html=evidencias/report.html --self-contained-html
```

## Comandos Úteis

### Executar teste específico

```bash
pytest tests/test_busca_restaurantes.py
```

### Executar com mais detalhes

```bash
pytest -v -s
```

### Executar apenas um cenário

```bash
pytest tests/test_busca_restaurantes.py::test_busca_válida_retorna_resultados
```

### Executar em paralelo (mais rápido)

```bash
pytest -n auto
```

### Ver lista de testes sem executar

```bash
pytest --collect-only
```

## Troubleshooting

### Erro: ModuleNotFoundError

```bash
pip install -r requirements.txt
```

### Erro: Playwright não encontrado

```bash
pip install playwright
playwright install chromium
```

### Testes falhando

1. Verifique se o site está acessível: https://local-eats-unisenac.vercel.app/
2. Verifique conexão com internet
3. Aumente timeouts se necessário (editar testes)

## Dicas

- Use `-v` para ver detalhes dos testes
- Use `-s` para ver prints durante execução
- Use `--tb=short` para tracebacks menores
- Use `-x` para parar no primeiro erro
- Use `-k "palavra"` para executar testes que contenham "palavra" no nome
