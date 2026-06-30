# Atividade 08 - BDD e Automação com LocalEats

## 📋 Pré-requisitos

- Python 3.8+
- pip

## 🚀 Instalação

### 1. Criar ambiente virtual
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 2. Instalar dependências
```powershell
pip install -r requirements.txt
```

### 3. Instalar navegadores
```powershell
playwright install chromium
```

## 🧪 Executar os Testes

```powershell
pytest -v
```

## 📁 Estrutura

```
atividade-08/
├── features/              # Cenários BDD em Gherkin
├── tests/                 # Testes automatizados
├── evidencias/           # Screenshots e logs
└── README.md
```

## 📊 Funcionalidades Testadas

- ✅ Busca de restaurantes
- ✅ Navegação entre páginas
- ✅ Histórico de pedidos
- ✅ Visualização de restaurantes

## 🛠️ Tecnologias

- Python
- pytest
- pytest-bdd
- Playwright
