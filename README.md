# Quotes Parser

Парсер для сбора цитат с сайта quotes.toscrape.com

## Установка

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/your-username/quotes-parser.git
    ```

2. Создайте виртуальное окружение и активируйте его:
    ```bash
    python -m venv venv
    venv\Scripts\activate # Windows
    ```

3. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

## Использование

1. Запустите парсер:
    ```bash
    python parser.py
    ```

2. Результаты будут сохранены в файл `quotes.json`

## Структура данных
Каждая цитата содержит:
- Текст цитаты
- Автор
- Список тегов

## Анализ решения
Подробный анализ решения доступен в файле [analysis.md](analysis.md)