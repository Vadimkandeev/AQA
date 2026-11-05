# Cinescope API autotests

Учебный проект автотестов Cinescope, построенный на API-классах и единой HTTP-сессии.

## Структура

- `api/` — агрегатор API-клиентов (`ApiManager`)
- `clients/` — API-классы авторизации, пользователей, жанров, фильмов и отзывов
- `custom_requester/` — общий HTTP-клиент
- `payments/` — API-класс платежной системы
- `tests/api_client/` — актуальные тесты API-классов
- `tests/api_payments/` — заготовка для будущих тестов платежной системы
- `utils/` — генераторы тестовых данных

Старые итерации тестов на прямых запросах и UI-тесты в эту копию не включены.

## Установка

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Для macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Переменные окружения

Создай локальный файл `.env` на основе `.env.example` и укажи учетные данные тестового администратора:

```env
ADMIN_EMAIL=...
ADMIN_PASSWORD=...
```

Файл `.env` исключен из Git и не должен попадать в репозиторий.

## Запуск

```bash
pytest
```

Только актуальные API-тесты:

```bash
pytest tests/api_client
```

Платежные тесты:

```bash
pytest tests/api_payments
```
