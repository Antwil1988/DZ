### Основные файлы

#### 1. [`models.py`](liba/models.py)
Содержит модели данных приложения:
- `Author` — модель автора книги
- `Book` — модель книги
- `Review` — модель отзыва о книге

#### 2. [`services.py`](liba/services.py)
Содержит бизнес-логику приложения

#### 3. [`management/commands/seed.py`](liba/management/commands/seed.py)
Команда для заполнения базы тестовыми данными.
python manage.py seed

#### 4. [Shell_SQL.txt](Shell_SQL.txt)
Содержит примеры SQL-запросов, которые можно выполнить в оболочке Django (manage.py shell)


