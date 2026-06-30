# Pasta de Evidências

Esta pasta deve conter:

- Screenshots da execução dos testes
- Logs de execução do pytest
- Relatórios HTML gerados
- Vídeos de execução (opcional)

## Como gerar evidências

### Screenshots automáticos

Os testes podem ser configurados para capturar screenshots em falhas.

### Relatório HTML

Execute os testes com:

```bash
pytest --html=evidencias/report.html --self-contained-html
```

### Logs detalhados

Execute os testes com:

```bash
pytest -v > evidencias/execution.log 2>&1
```
