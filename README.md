
# Электронный Журнал

Этот проект представляет собой систему электронного журнала для управления студентами и их оценками. Реализован с использованием FastAPI, SQLAlchemy и Alembic.

## Оглавление

- [Установка](#установка)
- [Настройка базы данных](#настройка-базы-данных)
- [Запуск приложения](#запуск-приложения)
- [API Эндпоинты](#api-эндпоинты)
- [Миграции](#миграции)
- [Контрибьюции](#контрибьюции)
- [Лицензия](#лицензия)

## Установка

1. Клонируйте репозиторий:
    ```sh
    git clone https://github.com/yourusername/electronic-journal.git
    cd electronic-journal
    ```

2. Создайте и активируйте виртуальное окружение:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Установите зависимости:
    ```sh
    pip install -r requirements.txt
    ```

## Настройка базы данных

1. Создайте файл `alembic.ini` на основе шаблона `alembic.ini.example` и настройте строку подключения к базе данных:
    ```ini
    sqlalchemy.url = sqlite:///./test.db
    ```

2. Настройте файл `env.py` в директории `alembic` для использования метаданных моделей:
    ```python
    from logging.config import fileConfig
    from sqlalchemy import engine_from_config
    from sqlalchemy import pool
    from alembic import context

    # Импортируем вашу базовую модель SQLAlchemy
    from database import Base

    # Устанавливаем метаданные для автоматической генерации миграций
    target_metadata = Base.metadata

    config = context.config

    if config.config_file_name is not None:
        fileConfig(config.config_file_name)

    def run_migrations_offline() -> None:
        url = config.get_main_option("sqlalchemy.url")
        context.configure(
            url=url,
            target_metadata=target_metadata,
            literal_binds=True,
            dialect_opts={"paramstyle": "named"},
        )

        with context.begin_transaction():
            context.run_migrations()

    def run_migrations_online() -> None:
        connectable = engine_from_config(
            config.get_section(config.config_ini_section, {}),
            prefix="sqlalchemy.",
            poolclass=pool.NullPool,
        )

        with connectable.connect() as connection:
            context.configure(
                connection=connection,
                target_metadata=target_metadata,
            )

            with context.begin_transaction():
                context.run_migrations()

    if context.is_offline_mode():
        run_migrations_offline()
    else:
        run_migrations_online()
    ```

## Запуск приложения

1. Инициализируйте базу данных:
    ```sh
    alembic upgrade head
    ```

2. Запустите сервер:
    ```sh
    uvicorn main:app --reload
    ```

3. Откройте браузер и перейдите по адресу [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs), чтобы увидеть автоматически сгенерированную документацию API.

## API Эндпоинты

### Студенты

- **GET /GetallStudents/**: Получить список всех студентов.
- **POST /AddStudents/**: Добавить нового студента.
- **GET /GetStudents/{student_id}**: Получить информацию о студенте по ID.
- **PATCH /UpdateStudents/{student_id}**: Обновить информацию о студенте.
- **DELETE /DeleteStudents/{student_id}**: Удалить студента.

### Оценки

- **POST /PostScore/**: Добавить новую оценку.
- **GET /GetScore/{score_id}**: Получить информацию о оценке по ID.
- **PATCH /UpdateScore/{score_id}**: Обновить информацию о оценке.
- **DELETE /DeleteScore/{score_id}**: Удалить оценку.

## Миграции

1. Создайте новую миграцию:
    ```sh
    alembic revision --autogenerate -m "Описание изменений"
    ```

2. Примените миграции:
    ```sh
    alembic upgrade head
    ```

