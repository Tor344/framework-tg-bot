# **framework-tg-bot**
![](https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Telegram_logo.svg/512px-Telegram_logo.svg.png)


# 🚀 framework-tg-bot

Фреймворк для разработки Telegram-ботов на базе **aiogram 3** с архитектурой модульного монолита.  
Подходит для создания масштабируемых ботов с разделением на независимые приложения (apps).

---

## 📦 Стек технологий

- **aiogram 3** — асинхронный Telegram framework  
- **FastAPI** — административная панель  
- **SQLAlchemy** — работа с базой данных  
- **Docker** — контейнеризация  

---

## ⚙️ Установка и запуск

### 🔧 Ручная настройка

1. Создайте файл `.env` в директории `config/`:

env
BOT_TOKEN=your_bot_token

### Установите и запустите проект:
```
git clone https://github.com/Tor344/framework-tg-bot.git
cd framework-tg-bot

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

python main.py
uvicorn admin.app:app --host 0.0.0.0 --port 8000
```
### ⚡ Автоматическая установка
```
git clone https://github.com/Tor344/framework-tg-bot.git
cd framework-tg-bot

python3 manager.py install
python3 manager.py start
🐳 Запуск через Docker
docker build -t my-bot-framework .

docker run -d \
  --name my_bot_run \
  -e BOT_TOKEN="your_bot_token" \
  my-bot-framework
  ```

### 🧩 Менеджер приложений (manager.py)

### Утилита для управления проектом и автоматизации развертывания.

### Основные команды:
📦 Работа с приложениями

    add-app — создать новое приложение в bot/apps/

    del-app — удалить приложение

⚙️ Управление системой

    install — установка зависимостей и настройка systemd

    uninstall — удаление настроек

▶️ Запуск

    start — запуск бота и админ-панели

## CI/CD Actions

В проекте предусмотрены GitHub Actions для упрощённого деплоя:

    start — запуск сервиса через systemd

    stop — остановка сервиса

    update_restart — обновление ветки main и перезапуск

## Архитектура

Проект построен по принципу модульного монолита:

bot/apps/ — функциональные модули (features)

handlers — обработчики Telegram

database — работа с БД

admin — FastAPI админка

middlewares — промежуточная логика

📌 Примечание

Проект находится в стадии развития и может изменяться.
Рекомендуется использовать как основу или шаблон для собственных решений.