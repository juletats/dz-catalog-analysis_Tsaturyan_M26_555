# dz-catalog-analysis-Tsaturyan-M26-555

Учебный проект: анализ каталога фильмов стримингового сервиса (`catalog_analysis.py`).

- Менеджер проекта: [uv](https://docs.astral.sh/uv/) (Python 3.12)
- Единственная зависимость (dev): [ruff](https://docs.astral.sh/ruff/) — проверка стиля PEP8
- Внешних библиотек для анализа данных (pandas, numpy и т.д.) в решении нет — вся логика реализована вручную

## Запуск

```bash
uv sync                  # установить зависимости
uv run catalog_analysis.py   # запустить отчет
uv run ruff check .          # проверка стиля
```
