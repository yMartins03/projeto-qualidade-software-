# Testes funcionais automatizados LocalEats

Projeto da Atividade PBL da Aula 10, com testes funcionais automatizados do sistema LocalEats.

## Tecnologias usadas

- Python
- Playwright
- Pytest
- Page Object Model

## Instalação

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
playwright install
```

## Execução dos testes

```bash
pytest
```

## Geração inicial com Codegen

```bash
playwright codegen https://local-eats-unisenac.vercel.app/
```

## Estrutura

```text
pages
  base_page.py
  restaurantes_page.py
  detalhes_restaurante_page.py
  carrinho_page.py
  checkout_page.py

tests
  test_01_lucas_navegacao_restaurantes.py
  test_02_henrique_detalhes_restaurante.py
  test_03_adriel_detalhes_cardapio.py
  test_04_derick_fluxo_checkout.py

codegen
  codigo_codegen_inicial.md

evidencias
  prints gerados durante a execução
```

## Entrega principal

O arquivo principal da atividade é:

```text
aula-10-testes-funcionais-automatizados.md
```
